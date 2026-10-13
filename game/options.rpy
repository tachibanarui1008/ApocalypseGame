init -20 python:
    gui.init(1600, 900)

define config.name = "未雨绸缪 · 整合版"
define config.version = "0.3.0"
define build.name = "ApocalypseGame"
define config.save_directory = "Weiyuchoumou-Unified-V03"
define config.window_title = "未雨绸缪 · 整合版"
define config.developer = True
define config.check_conflicting_properties = True
define config.game_menu_action = ShowMenu("pause_menu")
define config.rollback_enabled = True
define config.history_length = 500
define config.has_music = False
define config.has_sound = False
define config.has_voice = False
define config.default_text_cps = 30
define config.default_afm_time = 12

define gui.text_font = "fonts/NotoSansSC-Regular.otf"
define gui.name_text_font = "fonts/NotoSansSC-Regular.otf"
define gui.interface_text_font = "fonts/NotoSansSC-Regular.otf"
define gui.text_size = 27
define gui.interface_text_size = 22

default persistent.unlocked_achievements = []
default persistent.chapter2_unlocked = False
default persistent.reading_font_size = 27

default current_scene_id = "CH01-001"
default current_scene_title = "清晨"
default current_scene_time = "Day 1，07:15"
default current_scene_location = "沪海市 · 公寓"
default chapter_route = None
default phone_mode = False
default phone_speaker = "讯息"
default phone_text = ""
default quick_menu = True

init python:
    # Loaded as UTF-8 source by ch02_screens, so retain this runtime data file.
    build.classify("game/ch02_model.py", "all")
    build.classify("docs/**", None)
    build.classify("tools/**", None)
    build.classify("prototype/**", None)
    build.classify(".git/**", None)
    build.classify("*.md", None)
    build.classify("*.py", None)
    build.classify("game/fonts/OFL.txt", "all")
    build.documentation("game/fonts/OFL.txt")
