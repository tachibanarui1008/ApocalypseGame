# Staged S05/S06 calls. The v0.3.0 tutorial and its Day7 endpoint stay intact.
# Caller supplies narrative snapshot and actual preparation flags, never demo stocks.
default c2_story = None

init python:
    exec(compile(renpy.file("ch02_events.py").read().decode("utf-8"), "ch02_events.py", "exec"), globals())

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
    char_protagonist "我陪着你。但先回屋，我们不能这样上路。"
    char_partner "之前也是先等等。现在还等什么？"
    n "她用肩推开院门。门扇向外晃开一道能让人通过的缺口。院外传来鞋底拖过路面的声音。"
    menu:
        "留在她身边，让父亲合门":
            $ c2_story = c2e_gate_resolve(c2_story, "stay", gate_repaired, gate_watch_ready)
            char_protagonist "爸，关门。我在这里。"
            n "你站到她身侧，没有去抢手机。父亲从内侧抵住门扇，母亲伸手接住落在台阶上的钥匙。"
            char_partner "我不能把他们留在那里。"
            char_protagonist "我们把位置留着。你不需要一个人出去。"
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
    char_mother "晚宁，看着我。你先坐下，脚下有台阶。"
    n "她终于停住，喘息很轻。手机还在手里，屏幕亮着父亲最后发来的位置。"
    return

label ch02_storm_epilogue:
    # Validate before displaying; c2e_handoff copies instead of changing this snapshot.
    $ c2_story_next = c2e_handoff(c2_story)
    $ current_scene_title = "守住里面"
    $ current_scene_time = "Day 12，深夜"
    $ current_scene_location = "庐州城郊 · 安全屋"
    $ phone_mode = False
    $ quick_menu = True
    if c2_story["parents_status"] == "safe":
        n "晚宁父亲从窗边退开，母亲把小台灯挪到桌中间。六个人坐得比晚饭时近。"
        char_partner "爸妈在这儿。大家都在。"
        char_protagonist "嗯。今晚先不出去。"
    elif c2_story["parents_status"] == "unknown":
        n "晚宁写下最后位置与同行者号码，没有把那张纸放进抽屉。"
        char_partner "明天还要问。"
        char_protagonist "明天一起问。"
    elif not c2_story["intrusion"]:
        n "父亲把钥匙放到桌上，没问是谁先拿走的。晚宁坐在母亲旁边，手中是黑了屏的手机。"
        char_protagonist "今晚我在这里。"
        n "她没有回答。母亲替她把水杯放近了一点。"
    else:
        n "住宅门后垫着临时阻挡物。父亲在玄关，你留在楼梯边。楼下传来一下短促的碰撞，随后安静了。"
        char_father "别下来了。先守住屋里的门。"
    n "远处广播断续，但并未完全消失。桌上放着两张清单：一张记物资，另一张记人和未完成的事。"
    n "最后一行由你写成：明早先确认院里。"
    n "第二章·风暴前夜　终"
    $ c2_story = c2_story_next
    return
