# Native SLG tutorial screens. Uses the existing industrial colour system.
default c2 = None

init python:
    import json
    C2_CFG = json.loads(renpy.file("ch02_demo.json").read().decode("utf-8"))
    exec(compile(renpy.file("ch02_model.py").read().decode("utf-8"), "ch02_model.py", "exec"), globals())
    C2_CFG = c2_attach_routes(C2_CFG, json.loads(renpy.file(C2_CFG["routing_file"]).read().decode("utf-8")))

    def c2_map_click(key):
        if key in ("home","market","pharmacy","gate"):
            c2_select("basement" if key=="home" else key)
        else:
            renpy.show_screen("c2_location",place=key)
            renpy.restart_interaction()

    def c2_route_image(stops,mode):
        if not stops or C2_CFG.get("closed_edges") or any(e["state"]!="open" for e in C2_CFG["routing"]["edges"]):
            return None
        return "images/ch02/town_route_"+mode+"_"+"_".join(stops)+".png"

    def c2_edit(key, value):
        global c2
        c2 = copy.deepcopy(c2)
        c2["plan"][key] = value
        if key == "companion" and value:
            c2["plan"]["home"]["partner"] = "休息"
        renpy.retain_after_load()
        renpy.restart_interaction()

    def c2_home(person, job):
        global c2
        c2 = copy.deepcopy(c2)
        c2["plan"]["home"][person] = job
        renpy.retain_after_load()
        renpy.restart_interaction()

    def c2_select(destination):
        global c2
        if c2["hints"] and c2["period"] == "上午":
            if c2["tutorial"] == 0:
                renpy.notify("先点击左侧食品，查看已有储备。")
                return
            if destination != "market":
                renpy.notify("这次先去超市。下午可以自由安排。")
                return
        c2 = copy.deepcopy(c2)
        c2["plan"]["destination"] = destination
        if c2["tutorial"] == 1:
            c2["tutorial"] = 2
        renpy.retain_after_load()
        renpy.restart_interaction()

    def c2_food_seen():
        global c2
        if c2["tutorial"] == 0:
            c2 = copy.deepcopy(c2)
            c2["tutorial"] = 1
            renpy.retain_after_load()

    def c2_skip():
        global c2
        c2 = copy.deepcopy(c2)
        c2["hints"] = False
        c2["tutorial"] = 3
        renpy.retain_after_load()
        renpy.restart_interaction()

style c2_action:
    background Solid("#2a353a")
    hover_background Solid("#405044")
    selected_background Solid("#465640")
    insensitive_background Solid("#222a2e")
    padding (12, 8)
style c2_action_text:
    size 19
    color "#d9e1d9"
    insensitive_color "#65716e"
    selected_color ui_accent
style c2_primary is c2_action:
    background Solid(ui_accent)
    hover_background Solid("#dce7a2")
style c2_primary_text is c2_action_text:
    color "#24352b"
    hover_color "#18251c"

screen c2_header():
    add Solid(ui_bg)
    text "02  /  风暴前夜" xpos 40 ypos 25 size 28
    text ("距离危机正式爆发剩余：%d天" % (12-c2["day"])) xpos 590 ypos 23 size 29 color ui_accent
    text ("Day %d · %s" % (c2["day"],c2["period"])) xpos 44 ypos 72 size 18 color ui_muted
    text (("供水正常" if c2["supply"]["water"] else "供水中断")+" / "+("市电正常" if c2["supply"]["grid"] else "市电中断")+" / 网络可用") xpos 590 ypos 71 size 17 color ui_muted
    textbutton "存读档 / 设置" action ShowMenu("pause_menu") xpos 1330 ypos 25 style "c2_action"
    add Solid(ui_line) xpos 40 ypos 113 xsize 1520 ysize 1

screen c2_board():
    modal True
    $ res = c2["resources"]
    $ p = c2["plan"]
    $ preview = c2_preview(c2,C2_CFG)
    $ errors = c2_errors(c2,C2_CFG)
    use c2_header
    frame:
        xpos 40 ypos 140 xsize 245 ysize 554
        background Solid(ui_panel)
        padding (18,18)
        vbox:
            spacing 5
            text "家庭储备" size 23
            text "演示数值 / 非正式库存" size 13 color ui_muted
            textbutton ("资金    ¥ %d" % res["cash"]) action Show("c2_inventory") style "c2_action" xfill True
            button:
                action Show("c2_inventory")
                background None padding (0,0) xfill True
                use c2_resource_bar("食品", "food", "人日", "每日 −4人日 / 约%.1f天" % (res["food"]/4.0))
            use c2_resource_bar("应急水", "water", "L", "日饮水8L / 正常供水优先")
            use c2_resource_bar("护理用品", "care", "单位", "按对应任务使用")
            use c2_resource_bar("燃油", "fuel", "L", "本次计划 −%.2f L" % preview["fuel"])
            use c2_resource_bar("电车电量", "ev", "%", "本次计划 −%.2f%%" % preview["ev"])
            use c2_resource_bar("家庭储能", "battery", "%", "市电正常时不日常扣减")
            text "储备条为演示参考刻度\n实际数量可超过满条" size 12 color ui_muted
    text "庐州城郊 / 社区道路" xpos 335 ypos 145 size 23
    text "拖动查看 · 滚轮平移 · 点击地点安排" xpos 335 ypos 175 size 14 color ui_muted
    use c2_town_map(route_image=c2_route_image(preview["stops"],p["transport"]))
    if c2["period"] == "下午":
        hbox:
            xpos 335 ypos 618 spacing 12
            textbutton "地下室检查" action Function(c2_select,"basement") style "c2_action" selected (p["destination"]=="basement")
            textbutton "院门检查" action Function(c2_select,"gate") style "c2_action" selected (p["destination"]=="gate")
            textbutton "主角休息" action Function(c2_select,"rest") style "c2_action" selected (p["destination"]=="rest")
            textbutton "主角洗漱" action Function(c2_select,"wash") style "c2_action" selected (p["destination"]=="wash")
    elif c2["hints"]:
        frame:
            xpos 325 ypos 615 xsize 855 ysize 85
            background Solid("#354337")
            padding (16,12)
            vbox:
                spacing 6
                text ("教学 · "+["点击左侧食品，了解家庭储备。","在地图上点击便民商店。","选交通与队员，再在下方安排母亲清点库存。","确认全家安排后出发。"][min(c2["tutorial"],3)]) size 19 color ui_accent
                text "查看与修改计划不会推进时间；确认执行后才进入行动。" size 15
    frame:
        xpos 1205 ypos 140 xsize 355 ysize 554
        background Solid(ui_panel)
        padding (18,16)
        vbox:
            spacing 10
            text "行动计划" size 23
            text ("目的地："+{"market":"便民商店","pharmacy":"卫生服务点","basement":"地下室","gate":"院门","rest":"留家休息","wash":"留家洗漱"}[p["destination"]]) size 20
            text "主角负责本次行动" size 16 color ui_muted
            textbutton ("%s 晚宁%s" % ("✓" if p["companion"] else "○", "同行" if preview["stops"] else "协作")) action Function(c2_edit,"companion",not p["companion"]) style "c2_action"
            if preview["stops"]:
                text "交通方式" size 17 color ui_muted
                hbox:
                    spacing 6
                    for key in ("walk","suv","ev"):
                        textbutton C2_CFG["transport"][key]["name"] action Function(c2_edit,"transport",key) selected (p["transport"]==key) style "c2_action" text_size 15
                hbox:
                    spacing 12
                    text "每站购买" size 18 yalign 0.5
                    textbutton "−" action Function(c2_edit,"quantity",max(1,p["quantity"]-1)) style "c2_action"
                    text str(p["quantity"]) size 23 yalign 0.5
                    textbutton "+" action Function(c2_edit,"quantity",p["quantity"]+1) style "c2_action"
                if c2["period"] == "下午":
                    textbutton ("%s 顺路访问另一家店" % ("✓" if p["extra"] else "○")) action Function(c2_edit,"extra",not p["extra"]) style "c2_action" text_size 16
                text ("往返 %.2f km · 约 %d 分钟" % (preview["km"],preview["minutes"])) size 18
                text ("采购预算 ¥%d\n载货 %d / %d kg" % (preview["cost"],preview["weight"],preview["capacity"])) size 18
                text ("全程消耗 %.2f L / %.2f%%电" % (preview["fuel"],preview["ev"])) size 16 color ui_muted
            else:
                text "留家任务 / 约90分钟\n无需车辆和采购支出" size 18
            if errors:
                text errors[0] size 16 color "#e2b091" xsize 315
            else:
                text "安排可执行" size 16 color ui_accent
    hbox:
        xpos 40 ypos 709 spacing 12
        for key,name in (("hero","陈知远"),("partner","林晚宁"),("father","陈建川"),("mother","周慧敏")):
            frame:
                xsize 282 ysize 167 background Solid(ui_panel) padding (12,12)
                vbox:
                    spacing 4
                    textbutton name action Show("c2_person",person=key) style "c2_action" text_size 18 padding (0,0) background None
                    use c2_person_bars(key)
                    if key=="hero" or (key=="partner" and p["companion"]):
                        text "参与主行动" size 15 color ui_accent
                        $ cost = c2_needs_cost(c2,C2_CFG)[key]
                        text ("本时段 饱腹−%d / 饮水−%d" % (cost["satiety"],cost["hydration"])) size 12 color ui_muted
                    else:
                        text ("留家："+p["home"][key]) size 14 color ui_muted
                        hbox:
                            spacing 4
                            textbutton "休息" action Function(c2_home,key,"休息") style "c2_action" text_size 13 padding (5,4)
                            textbutton "清点" action Function(c2_home,key,"清点") style "c2_action" text_size 13 padding (5,4) selected (p["home"][key]=="清点")
                            if c2["period"] == "下午":
                                textbutton "检查" action Function(c2_home,key,"地下室检查" if key!="father" else "院门检查") style "c2_action" text_size 13 padding (5,4)
                                textbutton "洗漱" action Function(c2_home,key,"洗漱") style "c2_action" text_size 13 padding (5,4) selected (p["home"][key]=="洗漱")
    textbutton "确认执行  →" action Return("execute") sensitive (not errors) xpos 1220 ypos 736 xsize 340 ysize 65 style "c2_primary"
    hbox:
        xpos 1210 ypos 812 spacing 8
        textbutton "查看说明" action Show("c2_help") style "c2_action" text_size 15
        if c2["period"]=="上午" and c2["hints"]:
            textbutton "跳过提示" action Function(c2_skip) style "c2_action" text_size 15
    text "编辑安排不耗时 / 确认后执行全家本时段任务" xpos 40 ypos 885 size 12 color ui_muted

screen c2_inventory():
    modal True
    zorder 110
    add Solid("#10181de8")
    frame:
        align (0.5,0.5) xsize 850 background Solid(ui_panel) padding (35,30)
        vbox:
            spacing 20
            text "家庭物资 / 消耗说明" size 30
            text ("现有食品：%g 人日，约可供四人 %g 天。" % (c2["resources"]["food"],c2["resources"]["food"]/4.0)) size 23 color ui_accent
            text "1人日口粮供1人吃1天；今晚四人合计消耗4人日。\n早餐只介绍规则，晚间统一扣除，不会扣两次。" size 21 line_spacing 8
            text ("应急饮水：%d L。供水正常，日常生活不扣应急水。\n家庭储能保持满电；回家电车夜间使用市电充满。" % c2["resources"]["water"]) size 21 line_spacing 8
            text "开燃油车按路线耗油，剩余燃油不会自动补回。\n建材和护理用品按对应任务消耗；工具通常重复使用。" size 21 line_spacing 8
            text "每人有饱腹、饮水、卫生三项状态（0—100）。\n工作与生活降低状态；晚间用口粮和饮水恢复，洗漱恢复卫生。" size 19 line_spacing 6
            text C2_CFG["notice"] size 16 color ui_muted xsize 770
            textbutton "知道了 / 返回安排" action [Function(c2_food_seen),Hide("c2_inventory")] style "c2_primary"

screen c2_help():
    modal True
    zorder 110
    add Solid("#10181de8")
    frame:
        align (0.5,0.5) xsize 820 background Solid(ui_panel) padding (35,30)
        vbox:
            spacing 20
            text "操作说明" size 30
            text "1. 点地图地点，选择任务。\n2. 安排主角与可选同行者；其他家人留家。\n3. 选步行或车辆，核对往返、载货和预算。\n4. 确认执行，到店采购，返回后入库。\n5. 下午可检查地下室、院门或去药店。\n6. 晚间统一盘点消耗。" size 22 line_spacing 12
            text "提示可以跳过；跳过不会自动购买或赠送物资。" size 17 color ui_muted
            textbutton "返回" action Hide("c2_help") style "c2_primary"

screen c2_purchase(stop):
    modal True
    default quantity = c2["pending"]["plan"]["quantity"]
    $ item = C2_CFG["food_pack"] if stop=="market" else C2_CFG["care_pack"]
    $ errors = c2_purchase_errors(c2,C2_CFG,stop,quantity)
    $ carried = sum(x["weight"] for x in c2["pending"]["purchases"])
    use c2_header
    text "到店采购" xpos 140 ypos 180 size 19 color ui_accent
    text ("便民商店" if stop=="market" else "卫生服务点") xpos 140 ypos 230 size 55
    text "门仍开着。柜台后有人低头核对刚送到的货。" xpos 140 ypos 330 size 22 color ui_muted
    frame:
        xpos 840 ypos 185 xsize 620 ysize 570 background Solid(ui_panel) padding (32,30)
        vbox:
            spacing 22
            text ("耐储食品包" if stop=="market" else "基础护理用品包") size 29
            text ("每包12人日口粮 / 6 kg" if stop=="market" else "每包1护理单位 / 2 kg") size 21 color ui_muted
            text ("单价 ¥%d · 当前资金 ¥%d" % (item["price"],c2["resources"]["cash"])) size 23
            hbox:
                spacing 22
                textbutton "−" action SetScreenVariable("quantity",max(0,quantity-1)) style "c2_action"
                text str(quantity) size 30 yalign 0.5
                textbutton "+" action SetScreenVariable("quantity",quantity+1) style "c2_action"
            text ("合计 ¥%d\n剩余携带空间 %d kg / 本次购买 %d kg" % (quantity*item["price"],c2["pending"]["preview"]["capacity"]-carried,quantity*item["weight"])) size 22 line_spacing 12
            text (errors[0] if errors else "付款后装载，返回安全屋再计入家庭库存。") size 18 color ("#e2b091" if errors else ui_accent) xsize 540
            textbutton ("付款并装载" if quantity else "不购买 / 继续路线") action Return(quantity) sensitive (not errors) style "c2_primary"
            text "本页为教程演示价格与包容量。" size 14 color ui_muted

screen c2_result():
    modal True
    $ report = c2["reports"][-1]
    use c2_header
    frame:
        align (0.5,0.52) xsize 1000 background Solid(ui_panel) padding (40,35)
        vbox:
            spacing 22
            text "行动完成 / 已回到安全屋" size 33
            text ("到访："+(" → ".join(C2_CFG["nodes"][x]["name"] for x in report["preview"]["stops"]) or "安全屋 / 留家任务")) size 23
            text ("支出 ¥%d · 食品增加 %d 人日\n燃油消耗 %.2f L · 电车消耗 %.2f%%" % (report["cash_spent"],report["food_added"],report["preview"]["fuel"],report["preview"]["ev"])) size 23 line_spacing 10
            text ("家庭记录："+("、".join(c2["completed"]) or "暂无检查记录")) size 22
            text "工作已消耗饱腹与饮水；晚间统一扣口粮并恢复。" size 18 color ui_muted
            textbutton ("进入下午 / 自由安排" if c2["period"]=="下午" else "进入晚间盘点") action Return() style "c2_primary"

screen c2_settlement():
    modal True
    use c2_header
    frame:
        align (0.5,0.54) xsize 1050 background Solid(ui_panel) padding (40,35)
        vbox:
            spacing 20
            text "Day 6 / 晚间盘点" size 34
            text ("食品：%g 原有 ＋ %g 采购 − %g 消耗 ＝ %g 人日" % (c2["opening_food"],c2["bought_food"],c2["food_used"],c2["resources"]["food"])) size 26 color ui_accent
            text "四人全天口粮：4人 × 1天；吃饭和饮水恢复人物状态。" size 21
            text ("应急水 %g L · 家庭储能 %g%%\n电车 %.1f%% → %.1f%% · 燃油 %.2f L" % (c2["resources"]["water"],c2["resources"]["battery"],c2["ev_before_charge"],c2["resources"]["ev"],c2["resources"]["fuel"])) size 22 line_spacing 8
            text ("今日记录："+("、".join(c2["completed"]) or "采购与休息")) size 21
            if c2["shortage"]:
                text ("口粮不足：缺少%d人日，已记录缺餐。" % c2["shortage"]) size 21 color "#e2b091"
            text ("饮水合计：自来水 %g L / 应急储水 %g L（含洗漱）。" % (c2["mains_water_used"],c2["water_used"])) size 19 color ui_muted
            hbox:
                spacing 20
                for key,name in C2_PEOPLE.items():
                    vbox:
                        xsize 215 spacing 6
                        text name size 18
                        use c2_person_bars(key, width=205)
            if c2.get("water_shortage",0):
                text ("饮水不足：缺少%g L，人物饮水未充分恢复。" % c2["water_shortage"]) size 18 color "#e2b091"
            text "今日消耗已记账。" size 17 color ui_muted
            textbutton "休息 / 进入Day 7" action Return() style "c2_primary"

screen c2_day7():
    modal True
    use c2_header
    text "准备仍在继续。" xpos 220 ypos 280 size 55
    text "Day 6教程完成，库存、油电与检查记录已保留。\n后续支线与其余准备日尚待接入。" xpos 220 ypos 395 size 25 line_spacing 15 color ui_muted
    textbutton "保存进度" action ShowMenu("save") xpos 220 ypos 530 style "c2_action"
    textbutton "返回主菜单" action Return() xpos 220 ypos 610 style "c2_primary"

transform c2_travel_point(ax,ay,bx,by,duration):
    xpos ax ypos ay
    linear duration xpos bx ypos by

screen c2_travel(points,mode):
    modal True
    default segment = 0
    default speed = 1.0
    use c2_header
    text "在路上 / 往返路线" xpos 300 ypos 155 size 27
    use c2_town_map(route_image=c2_route_image(c2["pending"]["preview"]["stops"],mode), points=points, segment=segment, mode=mode, duration=speed)
    if segment < len(points)-1:
        timer speed action SetScreenVariable("segment",segment+1)
    else:
        timer 0.01 action Return()
    text "正在按计划前往目的地。" xpos 335 ypos 660 size 20 color ui_muted
    textbutton "加速" action SetScreenVariable("speed",0.15) xpos 800 ypos 705 style "c2_action"
    textbutton "跳过动画" action Return() xpos 950 ypos 705 style "c2_primary"


screen c2_town_map(route_image=None, points=None, segment=0, mode="walk", duration=1.0):
    default map_zoom = 0.48
    default hover_place = None
    default map_x = ui.adjustment(value=0)
    default map_y = ui.adjustment(value=148)
    $ image_w = int(1800*map_zoom)
    $ image_h = int(1380*map_zoom)
    $ canvas_w = max(855,image_w)
    $ canvas_h = max(400,image_h)
    $ ox = (canvas_w-image_w)//2
    $ oy = (canvas_h-image_h)//2
    hbox:
        xpos 900 ypos 164 spacing 6
        textbutton "−" action SetLocalVariable("map_zoom",max(0.28,round(map_zoom-0.12,2))) style "c2_action" text_size 14
        textbutton "＋" action SetLocalVariable("map_zoom",min(1.2,round(map_zoom+0.12,2))) style "c2_action" text_size 14
        textbutton "全图" action [SetLocalVariable("map_zoom",0.28),SetLocalVariable("map_x",ui.adjustment(value=0)),SetLocalVariable("map_y",ui.adjustment(value=0))] style "c2_action" text_size 14
        textbutton "街区" action [SetLocalVariable("map_zoom",0.48),SetLocalVariable("map_x",ui.adjustment(value=0)),SetLocalVariable("map_y",ui.adjustment(value=148))] style "c2_action" text_size 14
        textbutton "地点表" action Show("c2_distance_table") style "c2_action" text_size 14
    viewport:
        xpos 325 ypos 210 xsize 855 ysize 400
        xadjustment map_x yadjustment map_y
        draggable True mousewheel True arrowkeys True
        child_size (canvas_w,canvas_h)
        fixed:
            xsize canvas_w ysize canvas_h
            add Solid("#20292a")
            add Transform("images/ch02/town_map_game.png",zoom=map_zoom) xpos ox ypos oy
            if route_image:
                add Transform(route_image,zoom=map_zoom) xpos ox ypos oy
            for key in [k for k in C2_CFG["routing"]["matrix_order"] if (map_zoom >= 0.65 or k not in ("gate","pv_field")) and (map_zoom >= 0.4 or k not in ("hardware","parcel","fuel"))]:
                $ node = C2_CFG["routing"]["places"][key]
                $ px = int(ox+node["marker_xy"][0]*map_zoom)
                $ py = int(oy+node["marker_xy"][1]*map_zoom)
                $ is_selected = c2["plan"]["destination"]==key or (key=="home" and c2["plan"]["destination"]=="basement")
                imagebutton:
                    xpos px-18 ypos py-18
                    padding (0,0)
                    background None hover_background None selected_background None
                    idle ("images/ch02/poi/"+key+"_idle.png")
                    hover ("images/ch02/poi/"+key+"_hover.png")
                    selected_idle ("images/ch02/poi/"+key+"_selected.png")
                    selected_hover ("images/ch02/poi/"+key+"_selected.png")
                    insensitive ("images/ch02/poi/"+key+"_idle.png")
                    selected is_selected
                    sensitive (points is None)
                    hovered SetLocalVariable("hover_place",key)
                    unhovered SetLocalVariable("hover_place",None)
                    action Function(c2_map_click,key)
                if points is None and (key in ("home","market","pharmacy") or hover_place==key):
                    text node["name"]:
                        xpos px+22 ypos py-10
                        size 16
                        color (ui_accent if is_selected or hover_place==key else "#aab9ad")
                        outlines [(2,"#20292a",0,0)]
            if points and segment < len(points)-1:
                $ a = C2_CFG["routing"]["nodes"][points[segment]]["xy"]
                $ b = C2_CFG["routing"]["nodes"][points[segment+1]]["xy"]
                add ("images/ch02/marker_"+mode+".png") at c2_travel_point(int(ox+a[0]*map_zoom-20),int(oy+a[1]*map_zoom-20),int(ox+b[0]*map_zoom-20),int(oy+b[1]*map_zoom-20),duration)

screen c2_location(place):
    modal True
    zorder 110
    $ loc = C2_CFG["routing"]["places"][place]
    $ walk_m = C2_CFG["routing"]["distance_matrices"]["walk"]["home"][place]
    $ car_m = C2_CFG["routing"]["distance_matrices"]["suv"]["home"][place]
    add Solid("#10181de8")
    frame:
        align (0.5,0.5) xsize 850 background Solid(ui_panel) padding (35,30)
        vbox:
            spacing 20
            text loc["name"] size 30
            text ("从安全屋出发 / 步行 %d m / 驾车 %d m" % (walk_m,car_m)) size 23 color ui_accent
            text loc["description"] size 21 xsize 770
            text ("地点状态："+loc["status"]) size 18 color ui_muted
            text "距离按可通行道路计算。车辆到停车入口，步行到门口。\n本轮教程暂未开放这里的采购或长支线。" size 20 line_spacing 10
            textbutton "返回地图" action Hide("c2_location") style "c2_primary"


screen c2_distance_table():
    modal True
    zorder 110
    add Solid("#10181de8")
    frame:
        align (0.5,0.5) xsize 900 background Solid(ui_panel) padding (30,25)
        vbox:
            spacing 12
            text "安全屋出发 / 地点距离表" size 29
            text "单位：米。步行到门口，车辆到停车或道路入口。" size 18 color ui_muted
            fixed:
                xsize 820 ysize 26
                text "地点" xpos 0 size 19 color ui_accent
                text "步行（米）" xpos 380 size 19 color ui_accent
                text "驾车（米）" xpos 570 size 19 color ui_accent
            viewport:
                xsize 820 ysize 405 mousewheel True draggable True
                vbox:
                    spacing 4
                    for key in C2_CFG["routing"]["matrix_order"]:
                        fixed:
                            xsize 820 ysize 24
                            text C2_CFG["routing"]["places"][key]["name"] xpos 0 size 19
                            text str(C2_CFG["routing"]["distance_matrices"]["walk"]["home"][key]) xpos 380 size 19
                            text str(C2_CFG["routing"]["distance_matrices"]["suv"]["home"][key]) xpos 570 size 19
            text "全部地点之间的矩阵另存于数据文件；地图不按现实比例绘制。" size 16 color ui_muted
            textbutton "返回地图" action Hide("c2_distance_table") style "c2_primary"


screen c2_person_bars(person, width=252):
    vbox:
        spacing 3
        for key,label in (("satiety","饱腹"),("hydration","饮水"),("hygiene","卫生")):
            $ amount = c2["people"][person][key]
            hbox:
                spacing 7
                text label size 13 xsize 30
                bar:
                    value StaticValue(amount,100)
                    xsize (width-76) ysize 8 yalign 0.5
                    left_bar Solid("#d69a76" if amount<30 else "#aabd88")
                    right_bar Solid("#394440")
                    thumb None left_gutter 0 right_gutter 0
                text str(amount) size 12 xsize 32 text_align 1.0

screen c2_resource_bar(label, key, unit, note):
    $ amount = c2["resources"][key]
    $ reference = C2_CFG["bar_reference"][key]
    vbox:
        spacing 3
        text ("%s  %g %s" % (label,amount,unit)) size 17
        bar:
            value StaticValue(min(amount,reference),reference)
            xsize 207 ysize 8
            left_bar Solid("#d69a76" if amount<reference*0.2 else "#aabd88")
            right_bar Solid("#394440")
            thumb None left_gutter 0 right_gutter 0
        text note size 12 color ui_muted

screen c2_person(person):
    modal True
    zorder 110
    $ cost = c2_needs_cost(c2,C2_CFG)[person]
    add Solid("#10181de8")
    frame:
        align (0.5,0.5) xsize 800 background Solid(ui_panel) padding (35,30)
        vbox:
            spacing 20
            text (C2_PEOPLE[person]+" / 生活状态") size 30
            use c2_person_bars(person, width=700)
            text ("本时段预计：饱腹 −%d / 饮水 −%d / 卫生 −%d" % (cost["satiety"],cost["hydration"],cost["hygiene"])) size 21
            text "饱腹与饮水：每个时段自然下降，工作有额外消耗。\n晚间按现有口粮与饮水恢复；不足时不能充分恢复。\n卫生：生活和工作逐渐降低，可安排洗漱（用水6L）。\n低于30时条形变为警示色；这版暂不加入疾病惩罚。" size 20 line_spacing 10
            text "数值与消耗均为演示配置。点人物名字可重新查看。" size 16 color ui_muted
            textbutton "返回安排" action Hide("c2_person") style "c2_primary"

label after_load:
    if c2 is not None:
        $ c2 = c2_upgrade(c2,C2_CFG)
    return
