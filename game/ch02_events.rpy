# Staged H03/S05/S06 calls. The v0.3.0 tutorial and its Day7 endpoint stay intact.
# Caller supplies narrative snapshot and actual preparation flags, never demo stocks.
default c2_story = None

init python:
    exec(compile(renpy.file("ch02_events.py").read().decode("utf-8"), "ch02_events.py", "exec"), globals())

label ch02_rescue_decision:
    if c2_story is not None and c2_story["rescue_plan"] is not None:
        return
    $ current_scene_title = "我们去接，还是等他们来"
    $ current_scene_location = "庐州城郊 · 安全屋餐厅"
    $ current_scene_time = "Day %d，午间" % c2_story["day"]
    $ quick_menu = True
    $ phone_mode = False
    n "林晚宁靠在餐厅门边打电话。母亲在厨房洗碗，水声盖住了电话里一小段话。"
    n "晚宁母亲说：我们这边还正常，楼下买菜也买得到。"
    char_partner "我知道。你们先来住几天，又不是让你们搬个家。"
    n "晚宁父亲说：那也得收拾。你妈这会儿还往包里塞东西呢。"
    char_partner "带点药、证件和换洗的就好。其他的以后再说。"
    n "晚宁母亲说：你们这两天刚到，先歇歇。我们又不是不认识路，晚几天自己过去就行。"
    char_partner "你说呢？我们去接，还是等他们过来？"
    menu:
        "我们去接，别让他们自己折腾了。":
            $ c2_story = c2e_choose_rescue(c2_story, "pickup")
            char_protagonist "东西后面再拿。咱们开车过去，人接来就踏实了。"
            char_partner "妈，我们来接。你别再往包里加东西了，拉链都快合不上了吧？"
            n "晚宁母亲问：你还没看见就知道了？"
            char_partner "我还能不知道你。"
            n "她笑了一下，把约好的时间记在手机上。"
        "这两天先收拾家里，等他们晚点过来。":
            $ c2_story = c2e_choose_rescue(c2_story, "self_arrival")
            char_protagonist "他们说得也有道理。客房还乱着，让他们晚几天来吧。"
            char_partner "那出门前给我打电话，车找好了吗？"
            n "晚宁父亲说：找车不难。你把位置再发一遍，我们收拾完就过去。"
            char_partner "好，我发。别光看地址，到了最后那两个路口问我。"
            n "她把安全屋的位置发过去，随后把手机放到餐桌边。"
    return

label ch02_gate_event(gate_repaired=False, gate_watch_ready=False):
    if c2_story is not None and "CH02-S05-resolved" in c2_story["seen_events"]:
        return
    $ c2_story = c2e_gate_open(c2_story)
    $ current_scene_title = "院门"
    $ current_scene_time = "Day 12，晚间"
    $ current_scene_location = "庐州城郊 · 安全屋院口"
    $ phone_mode = False
    $ quick_menu = True
    n "晚宁抓起玄关上的钥匙；你追到门边时，外侧门闩已经被她拉开。"
    char_partner "我得去接他们。"
    char_protagonist "晚宁，你看着我，先别往外走。"
    char_partner "之前也是先等等。现在还等什么？"
    n "她用肩推开院门。门扇向外晃开一道能让人通过的缺口。院外传来鞋底拖过路面的声音。"
    menu:
        "留在她身边，让父亲合门":
            $ c2_story = c2e_gate_resolve(c2_story, "stay", gate_repaired, gate_watch_ready)
            char_protagonist "爸，关门。我在这里。"
            n "你站到她身侧，没有去抢手机。父亲从内侧抵住门扇，母亲伸手接住落在台阶上的钥匙。"
            char_partner "我不能把他们留在那里。"
            char_protagonist "电话还没打完。先回去，我跟你再问一遍。"
            if c2_story["gate_status"] == "secured":
                n "门重新合上。外面的脚步停在另一侧，沿墙离开。"
            else:
                n "门沿拖住地面，父亲第二次用力才合住。缺口处一道模糊人影逼近，母亲先退入房门，你将晚宁带回玄关。"
        "先合院门，让母亲陪她回屋":
            $ c2_story = c2e_gate_resolve(c2_story, "close", gate_repaired, gate_watch_ready)
            char_protagonist "妈，带晚宁进屋。爸，帮我一把。"
            n "晚宁仍握着手机，母亲站在她身边，一遍遍叫她的名字。你们试着拉回门扇。"
            if c2_story["gate_status"] == "secured":
                n "父亲提前避开盲区，门合住。"
            else:
                n "门外的人影挤进缺口。你们放开外门，退向住宅。"
    char_mother "慢点，晚宁，坐这儿。阿姨在呢。"
    n "她终于停住，喘息很轻。手机还在手里，屏幕亮着父亲最后发来的位置。"
    return

screen c2e_chapter_end(outcome):
    modal True
    add Solid(ui_bg)
    text "第二章 · 风暴前夜" xpos 210 ypos 242 size 24 color ui_muted
    text ("好结局" if outcome == "good" else "坏结局") xpos 210 ypos 330 size 68
    text ("六个人留在灯下。" if outcome == "good" else "门口的拖鞋，没有等到它们的主人。") xpos 210 ypos 460 size 25 color ui_muted
    if outcome == "good":
        textbutton "进入第三章    →" action Return("continue") xpos 205 ypos 704 style "menu_primary"
    else:
        text "本周目结束" xpos 210 ypos 550 size 20 color ui_muted
        textbutton "返回主菜单    →" action Return("menu") xpos 205 ypos 704 style "menu_primary"

label ch02_storm_epilogue:
    # Only narrative result: the future caller must settle real resources first.
    $ c2_story_next = c2e_handoff(c2_story)
    $ current_scene_title = "第二章结算"
    $ current_scene_time = "Day 12，深夜"
    $ current_scene_location = "庐州城郊 · 安全屋"
    $ phone_mode = False
    $ quick_menu = True
    if c2_story_next["chapter_outcome"] == "good":
        n "晚宁母亲把小台灯挪到桌中间。父亲从玄关回来，关上屋里的门。"
        char_father "外面的灯没了，别再出去。"
        n "晚宁父亲说：我刚从窗边看了一眼，路上还有车。"
        char_mother "先坐。水在这儿，杯子自己拿。"
        n "晚宁伸手替母亲拉了把椅子。六个人围着那一点光坐下来，桌面比吃晚饭时挤。"
        n "晚宁母亲说：早知道这样，你们叫的时候我就该走了。还想着带那点菜。"
        char_partner "都到了，就别说了。"
        n "她把父母的手机也接上充电线。你听见楼外的广播断断续续地响，没有去调大自己的手机。"
    elif not c2_story["intrusion"]:
        n "父亲把门钥匙放在桌上。晚宁坐在母亲旁边，手机停在最后一个通话记录。你端来水，她没有伸手。"
        char_mother "先放这儿。"
        n "你把杯子放下，坐到她另一边。屋外还有动静，桌边没有人说话。"
    else:
        n "住宅门后垫着临时阻挡物。父亲留在玄关，你在楼梯边停下。晚宁的手机从手里滑到膝上，屏幕朝上亮着。母亲坐在旁边，伸手捡起它。"
        char_father "别下来了。"
        n "楼下传来一下碰撞。你没有再往前走。"
    if c2_story_next["chapter_outcome"] == "bad":
        n "玄关摆着两双拖鞋，都是为他们提前拿出来的。"
    $ c2_story = c2_story_next
    call screen c2e_chapter_end(c2_story["chapter_outcome"])
    return _return
