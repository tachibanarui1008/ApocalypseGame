from pathlib import Path
from fractions import Fraction
import json, math, csv, heapq, hashlib, shutil
from PIL import Image, ImageDraw
r=Path(__file__).resolve().parents[1]
import argparse
parser=argparse.ArgumentParser(description='从原地图道路预算生成模式路网、距离矩阵与透明路线层')
parser.add_argument('--export-dir',type=Path,default=r/'docs/chapters/ch02/distance_exports')
out=parser.parse_args().export_dir
layout=json.loads((r/'docs/chapters/ch01/assets/TOWN_LAYOUT.json').read_text(encoding="utf-8"))
# Independent game distance budgets for named road corridors, in metres.
# Coordinates locate their endpoints on the established schematic; no metres/pixel scale.
budgets=[[2200],[1500,1100,1450,1000],[420],[760],[220,1200,360],[70],[40,330],[1300],[1050,180],[980],[900],[560],[480],[1480],[210],[480],[460,650]]
assert len(budgets)==len(layout['roads_visual'])
segments=[]
for index,road in enumerate(layout['roads_visual']):
 assert len(budgets[index])==len(road['points'])-1
 for part,(a,b) in enumerate(zip(road['points'],road['points'][1:])):
  segments.append(dict(a=tuple(a),b=tuple(b),length_m=budgets[index][part],id=f'R{index+1:02d}-{part+1}',modes=['walk','suv','ev'],kind='road',source='既有地图道路中心线'))
# POIs are entrances; markers are separate display locations, never distance coordinates.
places={
 'home':dict(name='安全屋',marker_xy=[305,981],walk=[279,1072],car=[279,1106],status='已有',description='步行从住宅门口出发；车辆从院门出发。'),
 'gate':dict(name='院门',marker_xy=[350,1110],walk=[279,1106],car=[279,1106],status='已有',description='安全屋院门及搬运入口。'),
 'pv_field':dict(name='墙外空地',marker_xy=[365,1010],walk=[363,1040],car=[370,1040],status='拟设',description='墙外场地位置草案，不代表土地已获使用许可。'),
 'neighbor':dict(name='邻居家',marker_xy=[280,775],walk=[280,849],car=[280,870],status='已有住宅／人物待定',description='既有西南住宅的一户，车辆停在巷道入口。'),
 'market':dict(name='便民商店',marker_xy=[960,872],walk=[990,888],car=[990,910],status='已有',description='本轮食品采购使用既有便民商店，不另画一个超市。'),
 'farm':dict(name='农田取货点',marker_xy=[109,922],walk=[109,940],car=[149,870],status='已有农田／取货功能拟设',description='沿用西侧农田，未来农产品交易的地点草案。'),
 'pharmacy':dict(name='卫生服务点',marker_xy=[967,522],walk=[998,549],car=[998,565],status='已有／用品柜台拟设',description='本轮基础护理用品从这里领取，不将图上设施改名为独立药店。'),
 'parcel':dict(name='快递代收点',marker_xy=[1345,845],walk=[1330,790],car=[1330,790],status='拟设',description='物流道路旁的代收功能位置草案。'),
 'fuel':dict(name='加油补能点',marker_xy=[1300,580],walk=[1330,590],car=[1330,590],status='拟设',description='物流道路旁预留补能位置，本轮未开放交易。'),
 'hardware':dict(name='五金取货柜台',marker_xy=[1260,350],walk=[1268,358],car=[1200,358],status='拟设于维修区',description='维修区北侧取货功能，不凭底图假定已存在独立五金店。'),
 'workshop':dict(name='维修作坊',marker_xy=[1289,476],walk=[1268,399],car=[1200,399],status='已有',description='车辆到道路侧入口，步行到作坊门口。'),
 'station':dict(name='地铁终点站',marker_xy=[820,435],walk=[820,592],car=[820,680],status='已有',description='步行到站前广场南口；驾车到公交换乘侧，不穿越站房。'),
 'freight':dict(name='货运站门区',marker_xy=[1406,700],walk=[1370,790],car=[1370,790],status='已有',description='只计算公众门区，站内装卸区和股道不开放通行。'),
 'port':dict(name='港口陆侧入口',marker_xy=[1553,991],walk=[1550,1130],car=[1550,1130],status='已有',description='经铁路下穿到陆侧入口，不进入岸线和仓储内部。'),
}
access=[
 ([279,1072],[279,1106],35,['walk'],'住宅门口至院门'),
 ([279,1106],[370,1120],100,['walk','suv','ev'],'院门至住宅巷道'),
 ([363,1040],[370,1040],20,['walk'],'墙外场地步行接入'),
 ([280,849],[280,870],35,['walk'],'邻居院门步行接入'),
 ([990,888],[990,910],40,['walk'],'商店门口步行接入'),
 ([998,549],[998,565],30,['walk'],'卫生服务点步行接入'),
 ([149,870],[149,930],90,['walk'],'农田入口步行路径'),
 ([149,930],[109,930],40,['walk'],'农田入口步行路径'),
 ([109,930],[109,940],10,['walk'],'农田入口步行路径'),
 ([1268,358],[1200,358],85,['walk'],'五金柜台步行接入'),
 ([1268,399],[1200,399],85,['walk'],'维修作坊步行接入'),
 ([820,592],[820,610],40,['walk'],'站前广场步行接入'),
]
for i,(a,b,length,modes,label) in enumerate(access):segments.append(dict(a=tuple(a),b=tuple(b),length_m=length,id=f'A{i+1:02d}',modes=modes,kind='access',source=label))

def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def intersection(s,t):
 a=s['a'];b=s['b'];c=t['a'];d=t['b'];ab=(b[0]-a[0],b[1]-a[1]);cd=(d[0]-c[0],d[1]-c[1]);den=cross(ab,cd)
 if not den:return None
 ac=(c[0]-a[0],c[1]-a[1]);u=Fraction(cross(ac,cd),den);v=Fraction(cross(ac,ab),den)
 if 0<=u<=1 and 0<=v<=1:return (Fraction(a[0])+u*ab[0],Fraction(a[1])+u*ab[1])
 return None

def on(p,s):
 a=s['a'];b=s['b'];return cross((p[0]-a[0],p[1]-a[1]),(b[0]-a[0],b[1]-a[1]))==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
allpoints={tuple(p[k]) for p in places.values() for k in ('walk','car')}
allpoints.add((1480,1130)) # Explicit underpass breakpoint; rail itself never joins the road graph.
for s in segments:allpoints.update((s['a'],s['b']))
for s in segments:
 for t in segments:
  p=intersection(s,t)
  if p:allpoints.add(p)
assert all(all(v.denominator==1 if isinstance(v,Fraction) else True for v in p) for p in allpoints)
allpoints={tuple(int(v) for v in p) for p in allpoints}
nodes={};edges=[]
def nid(p):return 'road_'+str(p[0])+'_'+str(p[1])
for s in segments:
 pts=[p for p in allpoints if on(p,s)]
 a=s['a'];b=s['b'];delta=(b[0]-a[0],b[1]-a[1]);sq=delta[0]**2+delta[1]**2
 pts.sort(key=lambda p:(p[0]-a[0])*delta[0]+(p[1]-a[1])*delta[1])
 ts=[Fraction((p[0]-a[0])*delta[0]+(p[1]-a[1])*delta[1],sq) for p in pts]
 # Split the independent corridor budget at its junctions, preserving total metres.
 positions=[round(float(t*s['length_m'])) for t in ts]
 for i,(p,q) in enumerate(zip(pts,pts[1:])):
  for xy in (p,q):nodes[nid(xy)]={'name':'','xy':list(xy)}
  edges.append(dict(id=s['id']+f'-{i+1:02d}',source_corridor=s['id'],**{'from':nid(p),'to':nid(q)},length_m=positions[i+1]-positions[i],modes=s['modes'],kind=s['kind'],state='open',source=s['source'],underpass=s['id']=='R05-3'))
for key,p in places.items():
 p['endpoints']={'walk':nid(tuple(p.pop('walk'))),'suv':nid(tuple(p['car'])),'ev':nid(tuple(p.pop('car')))}
 for n in set(p['endpoints'].values()):assert n in nodes,(key,n)
 p['xy']=list(p['marker_xy'])

def path(start,end,mode,closed=()):
 graph={n:[] for n in nodes}
 for e in edges:
  if mode not in e['modes'] or e['id'] in closed or e['state']!='open':continue
  graph[e['from']].append((e['to'],e['length_m']));graph[e['to']].append((e['from'],e['length_m']))
 a=places[start]['endpoints'][mode];b=places[end]['endpoints'][mode];queue=[(0,a,[a])];seen=set()
 while queue:
  dist,n,route=heapq.heappop(queue)
  if n==b:return dist,route
  if n in seen:continue
  seen.add(n)
  for next_,length in graph[n]:
   if next_ not in seen:heapq.heappush(queue,(dist+length,next_,route+[next_]))
 return None,[]
keys=list(places);matrices={};paths={}
for mode in ('walk','suv','ev'):
 matrices[mode]={};paths[mode]={}
 for a in keys:
  matrices[mode][a]={};paths[mode][a]={}
  for b in keys:
   length,route=path(a,b,mode);assert length is not None,(mode,a,b)
   matrices[mode][a][b]=length;paths[mode][a][b]=route
   if a==b:assert length==0
 for a in keys:
  for b in keys:
   assert matrices[mode][a][b]==matrices[mode][b][a]
   for c in keys:assert matrices[mode][a][c]<=matrices[mode][a][b]+matrices[mode][b][c]
routing=dict(schema_version=1,version='0.4',unit='m',distance_basis='虚构游戏道路分段预算；坐标只用于原图定位，不是地图像素到现实距离的比例尺。',
 source_image='docs/chapters/ch01/assets/TOWN_MAP.png',source_image_sha256=hashlib.sha256((r/'docs/chapters/ch01/assets/TOWN_MAP.png').read_bytes()).hexdigest(),
 image_size=[1800,1380],matrix_order=keys,nodes=nodes,places=places,edges=edges,distance_matrices=matrices,path_matrices=paths,
 corridor_budgets=[dict(id=s['id'],a=list(s['a']),b=list(s['b']),length_m=s['length_m'],modes=s['modes'],kind=s['kind'],source=s['source'])for s in segments],
 notes=['矩阵为入口间最短可通行路径；不是直线距离。','步行可使用图中住宅接入和站前步行路径；车辆停在道路或停车入口。','同址车辆入口（安全屋与院门）允许非对角线0米。','车辆的停车至柜台步行包含在地点办理时间中，不计入车辆油电里程。','关闭下穿或道路后应重新求路；缓存矩阵只对应正常开放路网。','图中未明确绘出的功能点标为拟设，不因此认定已存在建筑、库存或土地使用权。'])
(r/'game/data/ch02_routes.json').write_text(json.dumps(routing,ensure_ascii=False,indent=2)+'\n', encoding="utf-8", newline="\n")
(r/'docs/chapters/ch02/TOWN_ROUTES_V0.4.json').write_text(json.dumps(routing,ensure_ascii=False,indent=2)+'\n', encoding="utf-8", newline="\n")
out.mkdir(parents=True,exist_ok=True)
for mode,title in [('walk','步行'),('suv','驾车')]:
 for target in [out/f'地点距离矩阵_{title}.csv',r/f'docs/chapters/ch02/DISTANCE_{mode}.csv']:
  with target.open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.writer(f);w.writerow(['入口间最短道路距离（米）']+[places[x]['name'] for x in keys])
   for a in keys:w.writerow([places[a]['name']]+[matrices[mode][a][b] for b in keys])
shutil.copy2(r/'game/data/ch02_routes.json',out/'城镇路网与距离矩阵.json')
shutil.copy2(r/'docs/chapters/ch01/assets/TOWN_MAP.png',r/'game/images/ch02/town_map.png')
assert (r/'game/images/ch02/town_map.png').read_bytes()==(r/'docs/chapters/ch01/assets/TOWN_MAP.png').read_bytes()
# Transparent route layers over the UNMODIFIED original map, not a replacement drawing.
for mode in ('walk','suv','ev'):
 for stops in [['market'],['pharmacy'],['market','pharmacy'],['pharmacy','market']]:
  im=Image.new('RGBA',(1800,1380),(0,0,0,0));d=ImageDraw.Draw(im);last='home'
  for stop in stops+['home']:
   _,route=path(last,stop,mode)
   for a,b in zip(route,route[1:]):
    d.line((tuple(nodes[a]['xy']),tuple(nodes[b]['xy'])),fill='#ffffff',width=15)
    d.line((tuple(nodes[a]['xy']),tuple(nodes[b]['xy'])),fill='#cb7a23',width=8)
   last=stop
  im.save(r/'game/images/ch02'/('town_route_'+mode+'_'+'_'.join(stops)+'.png'))
print('原图原样接入；',len(nodes),'路口/入口，',len(edges),'分段，',len(places),'地点；三种方式196项矩阵均通过对称与三角不等式检查。')
print('安全屋出发：')
for key in keys:print(places[key]['name'],matrices['walk']['home'][key],matrices['suv']['home'][key])

# Refresh the independent game skin after geometric route exports.
import runpy
runpy.run_path(str(r/"tools/style_town_map.py"))["build_style"](r)
