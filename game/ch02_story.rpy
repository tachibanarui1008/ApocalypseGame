# Chapter two: one fully playable B-route tutorial day.
label ch02_b_start:
    $ c2 = c2_new_state(C2_CFG)
    $ chapter_route = "B"
    $ quick_menu = True
    $ current_scene_title = "桌上的两张清单"
    $ current_scene_time = "Day 6，早晨"
    $ current_scene_location = "庐州城郊 · 安全屋"
    $ phone_mode = False
    n "早餐还没有收走，父亲已经把两张纸放在桌上。一张是购物小票，另一张写了又划掉。"
    char_mother "吃的买了一些。先看看，别又买一堆放不下的。我们四个人，每天都要吃。"
    char_father "附近商店走过去就行。搬得多就开车，别提到半路又回来找车。水电现在还正常，备用的先留着。"
    char_partner "把每天用的和准备留下的记清楚吧。我把附近的路找出来。"
    char_mother "出门干活会饿，也会口渴。各自的饮水别忘了，回家脏了就洗一洗。"
    n "手机上的地图还正常加载。院外有人骑车经过，铃声隔着玻璃传进来。"
    $ quick_menu = False
    jump ch02_plan

label ch02_plan:
    $ current_scene_time = "Day 6，" + c2["period"]
    call screen c2_board
    $ c2 = c2_begin(c2,C2_CFG)
    $ c2_stops = list(c2["pending"]["preview"]["stops"])
    $ c2_last = "home"
    while c2_stops:
        $ c2_stop = c2_stops.pop(0)
        $ c2_points = c2_path(C2_CFG,c2_last,c2_stop,c2["pending"]["plan"]["transport"])[1]
        call screen c2_travel(c2_points,c2["pending"]["plan"]["transport"])
        $ current_scene_title = "货架之间" if c2_stop == "market" else "柜台前"
        $ current_scene_location = C2_CFG["nodes"][c2_stop]["name"]
        if c2_stop == "market":
            n "便民商店门口有几辆电动车。店员正在把新到的货摆上架，纸箱还没有拆完。"
            char_protagonist "先买能放的。今天不一定要把所有东西买齐。"
        else:
            n "卫生服务点的工作人员隔着柜台核对清单。旁边的几个人都在看手机，偶尔有人抬头问一句。"
            n "你选择了家里能够用得上的基础护理用品。"
        call screen c2_purchase(c2_stop)
        $ c2 = c2_buy(c2,C2_CFG,c2_stop,_return)
        $ c2_last = c2_stop
    if c2_last != "home":
        $ c2_points = c2_path(C2_CFG,c2_last,"home",c2["pending"]["plan"]["transport"])[1]
        call screen c2_travel(c2_points,c2["pending"]["plan"]["transport"])
    else:
        $ current_scene_location = "安全屋"
        if c2["pending"]["plan"]["destination"] == "basement":
            n "地下室带着一点凉意。母亲指了指靠墙的几只箱子，最下面的纸板有些软。"
            n "你记下位置。这是检查记录，搬运、防潮与后续工程还需要另行安排。"
        elif c2["pending"]["plan"]["destination"] == "gate":
            n "院门打开时，下沿拖过地面。父亲蹲下看了看铰链。"
            char_father "先记下来。得备好材料，再找个时间一起修。"
        elif c2["pending"]["plan"]["destination"] == "wash":
            n "水龙头仍能放出清水。你洗掉身上的灰尘，换好干净衣服。"
        elif c2["pending"]["plan"]["destination"] == "relax":
            n "你把手机扣在桌上，翻了几页书。暂时不用追着一条条消息往下看。"
        else:
            n "你留在家里休息了一会儿。窗外的道路仍然有人经过。"
    if "地下室检查" in c2["pending"]["plan"]["home"].values() and "地下室检查" not in c2["completed"] and c2["pending"]["plan"]["destination"] != "basement":
        n "留家的家人发现，地下室墙边的一只纸箱底部有些软。位置记在清单上，搬运和防潮还需要另行安排。"
    if "院门检查" in c2["pending"]["plan"]["home"].values() and "院门检查" not in c2["completed"] and c2["pending"]["plan"]["destination"] != "gate":
        char_father "院门下面又蹭地了。我看过铰链，得先备些材料。今天只检查，还没修。"
    $ c2 = c2_finish(c2,C2_CFG)
    $ current_scene_location = "庐州城郊 · 安全屋"
    call screen c2_result
    if c2["period"] == "下午":
        jump ch02_plan
    jump ch02_evening

label ch02_evening:
    $ c2 = c2_settle(c2,C2_CFG)
    $ current_scene_title = "今天买回来的东西"
    $ current_scene_time = "Day 6，晚间"
    char_mother "今天吃掉多少，也记一下。不能只记买回来的。"
    char_partner "车在院里充着电。明天可以接着用。"
    char_father "有油的那辆不会自己补回来。出门之前看一眼。"
    n "父亲把清单折好，放在桌角。外面的街灯亮起来了。"
    call screen c2_settlement
    $ c2 = c2_sleep(c2,C2_CFG)
    $ c2 = c2_next_day(c2)
    call screen c2_day7
    $ c2 = None
    return
