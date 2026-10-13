# Unified industrial UI with first chapter art and second chapter SLG.
define ui_bg = "#171c20"
define ui_panel = "#242c31"
define ui_line = "#3c484e"
define ui_muted = "#98a6aa"
define ui_ink = "#e6ebe7"
define ui_accent = "#c9d98a"

init python:
    def reading_size():
        return max(persistent.reading_font_size, 36) if renpy.variant("small") else persistent.reading_font_size

style default:
    font "fonts/NotoSansSC-Regular.otf"
    size 22
    color ui_ink

style button:
    background Solid("#242c3100")
    hover_background Solid("#364239")
    padding (20, 14)

style button_text:
    size 22
    color ui_muted
    hover_color ui_ink
    selected_color ui_accent

style menu_action:
    background Solid("#242c31")
    hover_background Solid("#354037")
    xsize 430
    ysize 86
    padding (26, 20)

style menu_action_text:
    size 27
    color ui_ink
    hover_color ui_accent

style menu_primary:
    background Solid(ui_accent)
    hover_background Solid("#dce7a2")
    xsize 430
    ysize 100
    padding (26, 24)

style menu_primary_text:
    size 30
    color "#253329"
    hover_color "#14261a"

style quick_button_text:
    size 18
    color ui_muted
    hover_color ui_accent
    selected_color ui_accent

style quick_button:
    padding (18, 6)
    background None
    hover_background None

style bar:
    ysize 10
    left_bar Solid(ui_accent)
    right_bar Solid(ui_line)
    thumb None

screen top_chrome():
    add Solid(ui_bg) xpos 0 ypos 0 xsize 1600 ysize 92
    add Solid("#303a40") xpos 78 ypos 90 xsize 1444 ysize 1
    add Solid(ui_accent) xpos 78 ypos 32 xsize 6 ysize 25
    add Solid(ui_accent) xpos 89 ypos 23 xsize 6 ysize 34
    add Solid(ui_accent) xpos 100 ypos 28 xsize 6 ysize 29
    text "APOCALYPSE" xpos 127 ypos 22 size 25 kerning 2
    text "未 雨 绸 缪" xpos 130 ypos 57 size 12 color ui_muted
    add Solid(ui_line) xpos 330 ypos 27 xsize 1 ysize 40
    text ("CHAPTER 02" if c2 else "CHAPTER 01") xpos 374 ypos 25 size 13 color ui_muted kerning 3
    text ("风 暴 前 夜" if c2 else "晦 暗 阴 云") xpos 374 ypos 49 size 16

screen bottom_chrome(status="一切尚且如常。"):
    add Solid("#303a40") xpos 78 ypos 870 xsize 1444 ysize 1
    text status xpos 80 ypos 879 size 12 color ui_muted
    text "APOCALYPSE / 01" xpos 1375 ypos 879 size 12 color ui_muted

screen main_menu():
    tag menu
    add Solid(ui_bg)
    use top_chrome
    use bottom_chrome
    text "01 + 02" xpos 654 ypos 202 size 100 color "#8fa09f0b"
    add Solid(ui_accent) xpos 166 ypos 237 xsize 7 ysize 7
    text "2030 · 龙国" xpos 184 ypos 227 size 16 color ui_muted kerning 2
    text "未 雨 绸 缪" xpos 166 ypos 278 size 16 color ui_accent kerning 3
    text "晦暗" xpos 155 ypos 329 size 102 kerning 11
    text "阴云" xpos 221 ypos 447 size 102 kerning 11
    text "CLOUDS BEFORE THE FALL" xpos 166 ypos 587 size 13 color ui_muted kerning 4
    text "灾难发生之前，没有人会知道，自己刚刚度过的\n究竟是怎样寻常的一天。" xpos 166 ypos 637 size 17 color "#b7c2c0" line_spacing 12
    text "沪海市  ─────  庐州市" xpos 166 ypos 744 size 14 color ui_muted
    vbox:
        xpos 1005
        ypos 264
        spacing 10
        text "完整整合版 · 第一章 / 第二章教程" size 14 color ui_muted
        textbutton "01    开始阅读             →" action Start() style "menu_primary"
        textbutton "02    继续阅读             →" action Continue() style "menu_action"
        textbutton "03    读取存档             →" action ShowMenu("load") style "menu_action"
        textbutton "04    记录档案             →" action ShowMenu("achievements") style "menu_action"
        textbutton "第二章 · B线教程（演示）" action Start("ch02_b_start") style "c2_action" xsize 430 text_size 19
        hbox:
            spacing 8
            textbutton "阅读设置" action ShowMenu("preferences") text_size 17
            textbutton "美术资源" action ShowMenu("resource_gallery") text_size 17
            if not renpy.variant("mobile"):
                textbutton "退出程序" action Quit(confirm=True) text_size 17

screen scene_chrome():
    if not c2:
        use c1_art
    else:
        add Solid(ui_bg)
    use top_chrome
    add Solid("#171c20d9") xpos 78 ypos 105 xsize 1444 ysize 93
    text current_scene_time xpos 104 ypos 124 size 15 color ui_muted kerning 2
    text current_scene_title xpos 103 ypos 157 size 25 kerning 3
    text current_scene_location xpos 1110 ypos 141 size 16 color ui_muted xsize 380 text_align 1.0

screen say(who, what):
    use scene_chrome
    if phone_mode:
        window:
            id "window"
            xpos 855
            ypos 248
            xsize 590
            ysize 550
            background Solid("#e2e6dc")
            padding (32, 26)
            vbox:
                spacing 24
                text phone_speaker id "who" color "#5c7062" size 20
                add Solid("#a2b5a3") xsize 520 ysize 1
                viewport:
                    xsize 515 ysize 400
                    mousewheel True draggable True
                    text what id "what" color "#263a2e" size reading_size() xsize 515 line_spacing 9
    else:
        window:
            id "window"
            xpos 104
            ypos 642
            xsize 1392
            ysize 177
            background Solid("#242c31ec")
            padding (32, 20)
            vbox:
                spacing 14
                text (who if who else "旁白") id "who" size 20 color ui_accent
                viewport:
                    xsize 1270 ysize 105
                    mousewheel True draggable True
                    text what id "what" size reading_size() xsize 1270 line_spacing 10
    add Solid(ui_bg) xpos 0 ypos 819 xsize 1600 ysize 81
    use quick_menu
    use bottom_chrome(current_scene_title)

screen quick_menu():
    if quick_menu:
        hbox:
            xpos 88
            ypos 830
            spacing 24
            textbutton "← 回退" action Rollback() style "quick_button"
            textbutton "回看" action ShowMenu("history") style "quick_button"
            textbutton "存档" action ShowMenu("save") style "quick_button"
            textbutton "读档" action ShowMenu("load") style "quick_button"
            textbutton "自动" action Preference("auto-forward", "toggle") style "quick_button"
            textbutton "菜单 →" action ShowMenu("pause_menu") style "quick_button"
        text "SPACE / ENTER 继续" xpos 1280 ypos 840 size 13 color "#6e8186"

screen choice(items):
    use scene_chrome
    text "你决定……" xpos 155 ypos 245 size 28
    vbox:
        xpos 155
        ypos 314
        spacing 13
        for i, item in enumerate(items):
            button:
                action item.action
                xsize 1250
                ysize 118
                background Solid(ui_panel)
                hover_background Solid("#3b483b")
                padding (27, 17)
                hbox:
                    spacing 27
                    text ("ABCD"[i]) size 16 color ui_accent yalign 0.5
                    vbox:
                        spacing 8
                        text item.caption size 26
                        text story_choice_descriptions.get(item.caption, "") size 20 color ui_muted
    textbutton "菜单 →" action ShowMenu("pause_menu") xpos 1280 ypos 827 text_size 20
    use bottom_chrome("第一次选择")

screen menu_header(title):
    use top_chrome
    text title xpos 120 ypos 137 size 32 kerning 3
    textbutton "← 返回" action Return() xpos 1350 ypos 135 text_size 18

screen pause_menu():
    tag menu
    add Solid(ui_bg)
    use menu_header("阅读暂停")
    vbox:
        xpos 120
        ypos 248
        spacing 18
        textbutton "继续阅读" action Return() style "menu_primary"
        textbutton "保存进度" action ShowMenu("save") style "menu_action"
        textbutton "读取存档" action ShowMenu("load") style "menu_action"
        textbutton "阅读设置" action ShowMenu("preferences") style "menu_action"
        textbutton "返回主菜单" action MainMenu(confirm=True) style "menu_action"

screen save():
    tag menu
    use file_slots("保存阅读进度")
screen load():
    tag menu
    use file_slots("读取阅读进度")
screen file_slots(title):
    add Solid(ui_bg)
    use menu_header(title)
    grid 3 2:
        xpos 120
        ypos 247
        spacing 22
        for i in range(1, 7):
            button:
                action FileAction(i)
                xsize 435
                ysize 230
                background Solid(ui_panel)
                hover_background Solid("#344239")
                padding (24, 22)
                vbox:
                    spacing 18
                    text ("存档 %02d" % i) size 17 color ui_accent
                    text FileTime(i, format="%Y-%m-%d  %H:%M", empty="空存档") size 21
                    text FileSaveName(i) size 17 color ui_muted xsize 370
                    if FileLoadable(i):
                        add FileScreenshot(i) xsize 144 ysize 80
    hbox:
        xpos 120
        ypos 774
        spacing 18
        textbutton "自动存档" action FilePage("auto")
        textbutton "快速存档" action FilePage("quick")
        textbutton "手动存档" action FilePage("1")
    use bottom_chrome("阅读记录保存在本机")

screen history():
    tag menu
    add Solid(ui_bg)
    use menu_header("对白回看")
    viewport:
        xpos 120
        ypos 235
        xsize 1370
        ysize 590
        mousewheel True
        draggable True
        scrollbars "vertical"
        yinitial 1.0
        vbox:
            spacing 27
            for h in _history_list:
                vbox:
                    spacing 8
                    text (h.who if h.who else "旁白") size 16 color ui_accent
                    text h.what size 24 xsize 1240 line_spacing 10
            if not _history_list:
                text "尚无已阅读的对白。" size 22 color ui_muted
    use bottom_chrome("回看不会改变当前剧情位置")

screen preferences():
    tag menu
    add Solid(ui_bg)
    use menu_header("阅读设置")
    vbox:
        xpos 120
        ypos 242
        spacing 35
        text "文字出现速度" size 23
        bar value Preference("text speed") xsize 760
        text "自动阅读停留" size 23
        bar value Preference("auto-forward time") xsize 760
        text "文字大小" size 23
        bar value FieldValue(persistent, "reading_font_size", range=12, offset=21) xsize 760
        if not renpy.variant("mobile"):
            hbox:
                spacing 30
                textbutton "窗口模式" action Preference("display", "window")
                textbutton "全屏模式" action Preference("display", "fullscreen")
    text ("轻触继续\n底部按钮打开菜单\n回看中上下滑动" if renpy.variant("touch") else "点击或空格继续\n鼠标滚轮向上回退\nEsc打开阅读菜单") xpos 1050 ypos 330 size 20 line_spacing 17 color ui_muted
    use bottom_chrome("设置只影响阅读方式")

screen achievements():
    tag menu
    add Solid(ui_bg)
    use menu_header("记录档案")
    vbox:
        xpos 120
        ypos 253
        spacing 20
        for aid, title, description in ACHIEVEMENTS:
            frame:
                xsize 1320
                ysize 125
                background Solid(ui_panel)
                padding (30, 25)
                vbox:
                    spacing 12
                    if aid in persistent.unlocked_achievements:
                        text title size 27 color ui_accent
                        text description size 18 color ui_muted
                    else:
                        text "？？？" size 27
                        text "这段故事尚未被记录。" size 18 color ui_muted
    use bottom_chrome("记录跨周目保留")

screen chapter_end(route):
    modal True
    $ title, tagline, aid, kicker = ENDINGS[route]
    add Transform(C1_ASSETS[{"A":"CG-01","D":"CG-02","B":"CG-03","C":"CG-03"}[route]],xysize=(1600,900),fit="cover")
    add Solid("#171c20c8")
    use top_chrome
    text kicker xpos 210 ypos 242 size 16 color ui_muted kerning 2
    text title xpos 204 ypos 313 size 78 kerning 8
    text tagline xpos 210 ypos 448 size 26 color ui_muted
    text ("成就解锁 · " + title) xpos 210 ypos 548 size 20 color ui_accent
    if route in ("B", "C"):
        text "第二章《风暴前夜》已解锁。" xpos 210 ypos 596 size 21
        if route == "B":
            text "下一天，从家庭清单开始。" xpos 210 ypos 637 size 17 color ui_muted
        else:
            text "C线第二章尚待接入。" xpos 210 ypos 637 size 17 color ui_muted
    if route == "B":
        textbutton "进入第二章    →" action Return("continue") xpos 205 ypos 704 style "menu_primary"
        textbutton "返回主菜单" action Return() xpos 205 ypos 820 text_size 18
    else:
        textbutton "返回主菜单    →" action Return() xpos 205 ypos 704 style "menu_primary"
    use bottom_chrome("第一章 · " + title)

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#11191ddf")
    frame:
        align (0.5, 0.5)
        xsize 690
        background Solid(ui_panel)
        padding (40, 40)
        vbox:
            spacing 35
            text message size 25 xsize 600
            hbox:
                spacing 35
                textbutton "确认" action yes_action
                textbutton "取消" action no_action

screen notify(message):
    zorder 100
    frame:
        xalign 0.5
        ypos 105
        background Solid(ui_accent)
        padding (25, 12)
        text message size 18 color "#253329"
    timer 2.5 action Hide("notify")
