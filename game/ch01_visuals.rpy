# Chapter one presentation, sharing the unified native UI and save model.
default c1_picture = "BG-01"
default c1_person = None

init python:
    import json
    C1_ASSETS = json.loads(renpy.file("data/ch01_assets.json").read().decode("utf-8"))
    C1_NAMES = json.loads(renpy.file("data/ch01_asset_names.json").read().decode("utf-8"))
    C1_PRESENTATION = json.loads(renpy.file("data/ch01_presentation.json").read().decode("utf-8"))
    C1_INDOORS = ("BG-02","BG-05","BG-24","BG-13","BG-21","BG-19","EX-01","VAR-03","VAR-05")

    def c1_scene(identifier):
        global c1_picture, c1_person
        c1_picture = C1_PRESENTATION[identifier]["initial"]
        c1_person = None

    def c1_before(identifier, index, speaker=None):
        global c1_picture, c1_person
        for picture in C1_PRESENTATION[identifier]["cues"].get(str(index),[]):
            c1_picture = picture
        c1_person = {"林晚宁":"CHAR-02","伴侣":"CHAR-02","陈建川":"CHAR-03","父亲":"CHAR-03","周慧敏":"CHAR-04","母亲":"CHAR-04"}.get(speaker)

screen c1_art():
    if c1_picture in C1_ASSETS:
        add Transform(C1_ASSETS[c1_picture], xysize=(1600,900), fit="cover")
        if c1_person and c1_picture in C1_INDOORS and not phone_mode:
            $ height = int(650 * {"CHAR-02":165,"CHAR-03":173,"CHAR-04":160}[c1_person] / 178)
            add Transform(C1_ASSETS[c1_person], xysize=(int(height*2/3),height)) xpos 1220 ypos 660 xanchor 0.5 yanchor 1.0
    else:
        add Solid("#101719")

screen resource_gallery():
    tag menu
    default selected_asset = "BG-01"
    add Solid(ui_bg)
    use menu_header("第一章美术 / 全部42项资源")
    add Transform(C1_ASSETS[selected_asset],xysize=(1020,590),fit="contain") xpos 80 ypos 225
    text C1_NAMES[selected_asset] xpos 90 ypos 825 size 18 color ui_accent
    viewport:
        xpos 1140 ypos 235 xsize 350 ysize 570
        mousewheel True draggable True
        vbox:
            spacing 6
            for aid in C1_ASSETS:
                textbutton C1_NAMES[aid] action SetScreenVariable("selected_asset",aid) selected (selected_asset==aid) xsize 310 text_size 18
    use bottom_chrome("背景 / 人物 / CG / 变体均保留，可滚动选择。")
