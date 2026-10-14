"""Pure tutorial state transitions. No screen or Ren'Py dependencies.
All mutations return fresh dictionaries so Ren'Py rollback/save retains snapshots.
Demo costs are game budgets, not claims about real vehicle performance.
"""
import copy
import heapq
import math


C2_PEOPLE = {"hero":"陈知远", "partner":"林晚宁", "father":"陈建川", "mother":"周慧敏"}

def c2_upgrade(s,cfg):
    """Add needs to older demo saves without replaying purchases or daily charges."""
    n=copy.deepcopy(s)
    n.setdefault("people", {k:copy.deepcopy(cfg["needs"]["initial"]) for k in C2_PEOPLE})
    for person in n["people"].values():
        person.setdefault("stress", cfg["needs"]["initial"]["stress"])
    n.setdefault("sleep_on_time", {k:True for k in n["people"]})
    n.setdefault("slept_day", None)
    n.setdefault("stress_events", [])
    n.setdefault("supply", {"water":True,"grid":True})
    n.setdefault("water_used",0); n.setdefault("mains_water_used",0)
    return n

def c2_needs_cost(s,cfg,plan=None):
    p=plan or s["plan"]; v=c2_preview(s,cfg,p); result={}
    for key in C2_PEOPLE:
        main=key=="hero" or (key=="partner" and p["companion"])
        job=p["destination"] if main else p["home"][key]
        if main and v["stops"]:
            effort=math.ceil(v["minutes"]/30) if p["transport"]=="walk" else 3
            extra=(6+effort,8+effort,5) if p["transport"]=="walk" else (5,7,3)
        elif job in ("basement","gate","地下室检查","院门检查"):
            extra=(10,14,10)
        elif job=="清点": extra=(5,7,4)
        else: extra=(0,0,0)
        base=cfg["needs"]["base_slot"]
        result[key]={name:base[name]+extra[i] for i,name in enumerate(("satiety","hydration","hygiene"))}
        result[key]["wash"] = job in ("洗漱","wash")
        stress = cfg["stress"]["base_slot"]
        if main and v["stops"]: stress += cfg["stress"]["outside_extra"]
        elif job in ("basement","gate","地下室检查","院门检查","清点"):
            stress += cfg["stress"]["work_extra"]
        if job in ("rest", "休息"): stress -= cfg["stress"]["rest_relief"]
        elif job in ("relax", "阅读放松"): stress -= cfg["stress"]["leisure_relief"]
        result[key]["stress_delta"] = stress
    return result

def c2_water(n,litres):
    if n["supply"]["water"]:
        n["mains_water_used"]+=litres
        return 1.0
    used=min(n["resources"]["water"],litres)
    n["resources"]["water"]-=used; n["water_used"]+=used
    return used/float(litres) if litres else 1.0

def c2_new_state(cfg):
    return dict(day=6, period="上午", active=True, resources=copy.deepcopy(cfg["initial"]),
                opening_food=cfg["initial"]["food"], bought_food=0, tutorial=0,
                hints=True, plan=dict(destination="market", transport="walk", companion=False,
                                     quantity=1, extra=False, home={"father":"休息","mother":"休息","partner":"休息"}),
                pending=None, reports=[], completed=[], settled_day=None, shortage=0, people={k:copy.deepcopy(cfg["needs"]["initial"]) for k in C2_PEOPLE},
                supply={"water":True,"grid":True}, water_used=0, mains_water_used=0,
                sleep_on_time={k:True for k in C2_PEOPLE}, slept_day=None, stress_events=[])

def c2_attach_routes(cfg,routing):
    n=copy.deepcopy(cfg)
    n["routing"]=copy.deepcopy(routing)
    n["nodes"]=copy.deepcopy(routing["nodes"])
    n["nodes"].update(copy.deepcopy(routing["places"]))
    return n

def c2_path(cfg,start,end,mode="walk"):
    routing=cfg["routing"]
    if mode not in ("walk","suv","ev"): raise ValueError("未知交通方式")
    places=routing["places"]
    closed=set(cfg.get("closed_edges",[]))
    normal=not closed and all(e["state"]=="open" for e in routing["edges"])
    if normal and start in places and end in places:
        return routing["distance_matrices"][mode][start][end]/1000.0, list(routing["path_matrices"][mode][start][end])
    a=places[start]["endpoints"][mode] if start in places else start
    b=places[end]["endpoints"][mode] if end in places else end
    graph={key:[] for key in routing["nodes"]}
    for edge in routing["edges"]:
        if mode not in edge["modes"] or edge["state"]!="open" or edge["id"] in closed: continue
        graph[edge["from"]].append((edge["to"],edge["length_m"]))
        graph[edge["to"]].append((edge["from"],edge["length_m"]))
    queue=[(0,a,[a])]; visited=set()
    while queue:
        distance,node,path=heapq.heappop(queue)
        if node==b: return distance/1000.0,path
        if node in visited: continue
        visited.add(node)
        for nxt,length in graph[node]:
            if nxt not in visited: heapq.heappush(queue,(distance+length,nxt,path+[nxt]))
    raise ValueError("此交通方式的道路不通")

def c2_preview(s,cfg,plan=None):
    p=plan or s["plan"]
    dest=p["destination"]
    stops=[dest] if dest in ("market","pharmacy") else []
    if p["extra"] and stops: stops.append("pharmacy" if dest=="market" else "market")
    km=0; route=[]; last="home"; route_error=None; moving_minutes=0; carried=0
    t=cfg["transport"][p["transport"]]
    for stop in stops+["home"]:
        try:
            d,path=c2_path(cfg,last,stop,p["transport"]); km+=d; route+=path if not route else path[1:]; last=stop
            speed=t.get("laden_speed",t["speed"]) if p["transport"]=="walk" and carried else t["speed"]
            moving_minutes+=d/speed*60
            if stop in stops:
                item=cfg["food_pack"] if stop=="market" else cfg["care_pack"]
                carried+=p["quantity"]*item["weight"]
        except ValueError as exc:
            route_error=str(exc); route=[]; km=0; break
    t=cfg["transport"][p["transport"]]
    q=p["quantity"]
    cost=weight=0
    for stop in stops:
        item=cfg["food_pack"] if stop=="market" else cfg["care_pack"]
        cost+=q*item["price"]; weight+=q*item["weight"]
    capacity=t["capacity"]*(2 if p["transport"]=="walk" and p["companion"] else 1)
    minutes=math.ceil(moving_minutes)+len(stops)*30 if stops else 90
    return dict(stops=stops,route=route,km=round(km,2),minutes=minutes,cost=cost,weight=weight,
                capacity=capacity,fuel=round(km*t["fuel_per_km"],2),ev=round(km*t["ev_per_km"],2),route_error=route_error)

def c2_errors(s,cfg):
    p=s["plan"]; v=c2_preview(s,cfg); res=s["resources"]; errors=[]
    if v.get("route_error"): errors.append(v["route_error"])
    if s["pending"]: errors.append("已有行动正在执行。")
    if s["period"] not in ("上午","下午"): errors.append("今日行动已经结束。")
    if p["quantity"]<1 or not isinstance(p["quantity"],int): errors.append("请选择有效购买数量。")
    if p["companion"] and p["home"]["partner"]!="休息": errors.append("晚宁已随行，不能同时安排留家任务。")
    if p["destination"] not in ("market","pharmacy","basement","gate","rest","wash","relax"): errors.append("请选择可用任务。")
    if v["cost"]>res["cash"]: errors.append("资金不足：减少购买数量。")
    if v["weight"]>v["capacity"]: errors.append("载货超限：减少数量或换车。")
    if v["minutes"]>cfg["slot_minutes"]: errors.append("超过本时段时间：缩短路线。")
    if v["fuel"]>res["fuel"]: errors.append("燃油不足：更换交通方式。")
    if v["ev"]>res["ev"]: errors.append("电量不足：更换交通方式。")
    if s["hints"] and s["period"]=="上午":
        if s["tutorial"]<2: errors.append("请先查看食品，再在地图上选择便民商店。")
        if p["destination"]!="market": errors.append("首次外出先去便民商店。")
        if p["home"]["mother"]!="清点": errors.append("请安排母亲清点已有库存。")
    return errors

def c2_begin(s,cfg):
    errors=c2_errors(s,cfg)
    if errors: raise ValueError("\n".join(errors))
    n=copy.deepcopy(s); v=c2_preview(s,cfg); p=copy.deepcopy(s["plan"])
    aid=str(s["day"])+s["period"]
    if aid in [x["id"] for x in s["reports"]]: raise ValueError("该行动已结算")
    n["pending"]=dict(id=aid,plan=p,preview=v,purchases=[],visited=[],cash_spent=0,food_added=0)
    n["resources"]["fuel"]=round(n["resources"]["fuel"]-v["fuel"],2)
    n["resources"]["ev"]=round(n["resources"]["ev"]-v["ev"],2)
    return n

def c2_purchase_errors(s,cfg,stop,q):
    p=s["pending"]
    if not p or stop not in p["preview"]["stops"]: return ["无有效到店任务。"]
    if stop in p["visited"]: return ["本次到店已处理，不能重复购买。"]
    if not isinstance(q,int) or q<0: return ["购买数量无效。"]
    if s["hints"] and s["period"]=="上午" and q<1: return ["首次采购至少购买一个食品包。"]
    item=cfg["food_pack"] if stop=="market" else cfg["care_pack"]
    carried=sum(x["weight"] for x in p["purchases"])
    errors=[]
    if q*item["price"]>s["resources"]["cash"]: errors.append("资金不足。")
    if carried+q*item["weight"]>p["preview"]["capacity"]: errors.append("剩余载货空间不足。")
    return errors

def c2_buy(s,cfg,stop,q):
    errors=c2_purchase_errors(s,cfg,stop,q)
    if errors: raise ValueError("\n".join(errors))
    n=copy.deepcopy(s); p=n["pending"]
    item=cfg["food_pack"] if stop=="market" else cfg["care_pack"]
    p["visited"].append(stop); cost=q*item["price"]
    n["resources"]["cash"]-=cost; p["cash_spent"]+=cost
    food=q*item.get("food",0); p["food_added"]+=food
    p["purchases"].append(dict(stop=stop,quantity=q,food=food,care=q*item.get("care",0),weight=q*item["weight"]))
    return n

def c2_finish(s,cfg):
    if not s["pending"]: return copy.deepcopy(s)
    n=c2_upgrade(s,cfg); p=n["pending"]
    if p["id"] in [x["id"] for x in n["reports"]]: n["pending"]=None; return n
    if set(p["visited"])!=set(p["preview"]["stops"]): raise ValueError("尚有地点未处理")
    for purchase in p["purchases"]:
        n["resources"]["food"]+=purchase["food"]; n["resources"]["care"]+=purchase["care"]
    n["bought_food"]+=p["food_added"]
    jobs=[p["plan"]["destination"]]+list(p["plan"]["home"].values())
    for job in jobs:
        if job in ("basement","地下室检查") and "地下室检查" not in n["completed"]: n["completed"].append("地下室检查")
        if job in ("gate","院门检查") and "院门检查" not in n["completed"]: n["completed"].append("院门检查")
        if job=="清点" and "库存清点" not in n["completed"]: n["completed"].append("库存清点")
    p["needs_cost"]=c2_needs_cost(n,cfg,p["plan"])
    p["needs_before"]=copy.deepcopy(n["people"])
    for key,cost in p["needs_cost"].items():
        for name in ("satiety","hydration","hygiene"):
            n["people"][key][name]=max(0,n["people"][key][name]-cost[name])
        n["people"][key]["stress"] = min(100,max(0,n["people"][key]["stress"]+cost["stress_delta"]))
        if cost["wash"]:
            ratio=c2_water(n,cfg["needs"]["wash_water_l"])
            n["people"][key]["hygiene"]=min(100,n["people"][key]["hygiene"]+round(cfg["needs"]["wash_restore"]*ratio))
    p["needs_after"]=copy.deepcopy(n["people"])
    n["reports"].append(copy.deepcopy(p)); n["pending"]=None
    n["period"]="下午" if s["period"]=="上午" else "晚间"
    n["tutorial"]=3
    n["plan"]=dict(destination="basement",transport="walk",companion=False,quantity=1,extra=False,
                   home={"father":"休息","mother":"休息","partner":"休息"})
    return n

def c2_settle(s,cfg):
    if s["settled_day"]==s["day"]: return copy.deepcopy(s)
    if s["period"]!="晚间" or s["pending"]: raise ValueError("请先完成今日行动")
    n=c2_upgrade(s,cfg); n["before_dinner"]=n["resources"]["food"]
    used=min(n["resources"]["food"],cfg["population"])
    n["resources"]["food"]-=used; n["food_used"]=used; n["shortage"]=cfg["population"]-used
    n["needs_before_meal"]=copy.deepcopy(n["people"])
    water_ratio=c2_water(n,cfg["population"]*cfg["needs"]["daily_water_l"])
    n["water_shortage"]=round(cfg["population"]*cfg["needs"]["daily_water_l"]*(1-water_ratio),2)
    for person in n["people"].values():
        person["satiety"]=min(100,person["satiety"]+round(cfg["needs"]["meal_restore"]*used/cfg["population"]))
        person["hydration"]=min(100,person["hydration"]+round(cfg["needs"]["drink_restore"]*water_ratio))
    if n["shortage"] or n["water_shortage"]:
        for person in n["people"].values():
            person["stress"] = min(100,person["stress"]+cfg["stress"]["shortage_extra"])
    n["ev_before_charge"]=n["resources"]["ev"]
    if n["supply"]["grid"]: n["resources"]["ev"]=100
    n["settled_day"]=n["day"]
    return n

def c2_next_day(s):
    if s["settled_day"]!=s["day"]: raise ValueError("本日未结算")
    n=copy.deepcopy(s); n["sleep_on_time"]={k:True for k in n["people"]}; n["day"]+=1; n["period"]="上午"; n["opening_food"]=n["resources"]["food"]; n["bought_food"]=0; n["water_used"]=0; n["mains_water_used"]=0; return n


def c2_sleep(s,cfg):
    """Sleep follows dinner once; opening the summary is not itself sleep."""
    n=c2_upgrade(s,cfg)
    if n["slept_day"] == n["day"]: return n
    if n["settled_day"] != n["day"] or n["period"] != "晚间" or n["pending"]:
        raise ValueError("先完成当日行动和晚间结算")
    n["stress_before_sleep"]={key:person["stress"] for key,person in n["people"].items()}
    for key,person in n["people"].items():
        if n["sleep_on_time"].get(key,True):
            person["stress"]=max(0,person["stress"]-cfg["stress"]["sleep_relief"])
    n["slept_day"]=n["day"]
    return n


def c2_stress_event(s,cfg,event_id,changes):
    """Explicit story effects, once per world event; never infers a diagnosis."""
    if not isinstance(event_id,str) or not event_id: raise ValueError("压力事件需唯一标记")
    n=c2_upgrade(s,cfg)
    if event_id in n["stress_events"]: return n
    for key,delta in changes.items():
        if key not in n["people"] or isinstance(delta,bool) or not isinstance(delta,(int,float)) or not math.isfinite(delta):
            raise ValueError("压力事件人物或变化无效")
        n["people"][key]["stress"]=min(100,max(0,n["people"][key]["stress"]+delta))
    n["stress_events"].append(event_id)
    return n
