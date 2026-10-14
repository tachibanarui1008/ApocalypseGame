# Copied only into an extracted build by test_windows.py; never shipped.
init 100 python:
    import os
    import pathlib
    import copy
    WTEST_OUT = pathlib.Path(os.environ['WYC_TEST_OUTPUT'])
    WTEST_OUT.mkdir(parents=True, exist_ok=True)
    _test.timeout = 30.0
    _test.transition_timeout = 0.1
    _test.maximum_framerate = True
    _original_c1_scene = c1_scene
    WTEST_SCENES = []

    def c1_scene(identifier):
        if identifier not in WTEST_SCENES:
            WTEST_SCENES.append(identifier)
        _original_c1_scene(identifier)

    def wtest_picture(name):
        renpy.screenshot(str(WTEST_OUT / (name + '.png')))

    def wtest_checkpoint():
        (WTEST_OUT / 'checkpoint.json').write_text(json.dumps(c2), encoding='utf-8')

    def wtest_restored():
        return c2 == json.loads((WTEST_OUT / 'checkpoint.json').read_text(encoding='utf-8'))

    def wtest_report(route, mode):
        data = dict(route=route, mode=mode, scenes=list(WTEST_SCENES),
                    c2=c2, achievements=list(persistent.unlocked_achievements))
        (WTEST_OUT / (route + '-' + mode + '.json')).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

testsuite global:
    teardown:
        exit

testsuite windows_acceptance:
    testcase playthrough:
        parameter (route, choice_text, mode) = [('A', '查阅官方消息', 'walk'), ('B', '联系庐州市的父母', 'walk'), ('C', '先与伴侣商量', 'walk'), ('D', '暂时不予理会', 'walk'), ('T', '', 'walk'), ('T', '', 'suv'), ('T', '', 'ev')]
        $ WTEST_SCENES.clear()
        pause until screen "main_menu"
        $ persistent.unlocked_achievements = []
        $ preferences.text_cps = 0
        if eval route != 'T':
            run Start()
            pause 0.3
            $ wtest_picture(route + '-chapter1')
            advance until screen "choice" timeout 180
            click expression choice_text
            advance until screen "chapter_end" timeout 180
            assert eval chapter_route == route
            assert eval ENDINGS[route][2] in persistent.unlocked_achievements
            $ wtest_picture(route + '-ending')
            if eval route == 'B':
                click "进入第二章" until not screen "chapter_end"
            else:
                $ wtest_report(route, mode)
                click "返回主菜单" until screen "main_menu"
        else:
            run Start('ch02_b_start')
        if eval route in ('B', 'T'):
            advance until screen "c2_board"
            click "食品"
            pause until screen "c2_inventory"
            click "知道了 / 返回安排"
            run Function(c2_map_click, 'market')
            run Function(c2_home, 'mother', '清点')
            run Function(c2_edit, 'transport', mode)
            pause 0.3
            $ wtest_picture(route + '-' + mode + '-map')
            $ wtest_checkpoint()
            run FileSave(1, confirm=False)
            pause 0.5
            run Function(c2_edit, 'quantity', 2)
            run FileLoad(1, confirm=False)
            pause 0.5
            pause until screen "c2_board"
            assert eval wtest_restored()
            click "确认执行" until not screen "c2_board"
            pause until screen "c2_travel"
            click "跳过动画" until not screen "c2_travel"
            advance until screen "c2_purchase"
            click "付款并装载" until not screen "c2_purchase"
            pause until screen "c2_travel"
            click "跳过动画" until not screen "c2_travel"
            pause until screen "c2_result"
            assert eval c2['resources']['food'] == 92
            $ wtest_checkpoint()
            run FileSave(2, confirm=False)
            pause 0.5
            run FileLoad(2, confirm=False)
            pause 0.5
            pause until screen "c2_result"
            assert eval wtest_restored()
            click "进入下午" until screen "c2_board"
            pause until screen "c2_board"
            click "主角洗漱"
            click "确认执行" until not screen "c2_board"
            advance until screen "c2_result"
            click "进入晚间盘点" until not screen "c2_result"
            advance until screen "c2_settlement"
            assert eval c2['resources']['food'] == 88
            assert eval c2['resources']['water'] == 240
            assert eval c2['resources']['ev'] == 100
            assert eval c2['mains_water_used'] == 14
            if eval mode == 'suv':
                assert eval c2['resources']['fuel'] < 40
            $ wtest_checkpoint()
            run FileSave(3, confirm=False)
            pause 0.5
            run FileLoad(3, confirm=False)
            pause 0.5
            pause until screen "c2_settlement"
            assert eval wtest_restored()
            pause 0.3
            $ wtest_picture(route + '-' + mode + '-settlement')
            click "进入Day 7" until screen "c2_day7"
            pause until screen "c2_day7"
            assert eval c2['day'] == 7
            $ wtest_report(route, mode)
            click "返回主菜单" until screen "main_menu"

    testcase pressure:
        pause until screen "main_menu"
        run Start('ch02_b_start')
        advance until screen "c2_board"
        run Function(c2_skip)
        run Function(c2_select, 'rest')
        run Function(c2_home, 'partner', '阅读放松')
        click "确认执行" until not screen "c2_board"
        advance until screen "c2_result"
        assert eval c2['people']['hero']['stress'] == 15
        assert eval c2['people']['partner']['stress'] == 11
        click "进入下午" until screen "c2_board"
        run Function(c2_select, 'relax')
        $ wtest_picture('pressure-board')
        click "确认执行" until not screen "c2_board"
        advance until screen "c2_result"
        assert eval c2['people']['hero']['stress'] == 6
        click "进入晚间盘点" until not screen "c2_result"
        advance until screen "c2_settlement"
        run Function(c2_bedtime, 'mother')
        $ wtest_checkpoint()
        run FileSave(4, confirm=False)
        pause 0.5
        run Function(c2_bedtime, 'mother')
        run FileLoad(4, confirm=False)
        pause until screen "c2_settlement"
        assert eval wtest_restored()
        $ wtest_picture('pressure-settlement')
        click "进入Day 7" until screen "c2_day7"
        assert eval c2['people']['hero']['stress'] == 0
        assert eval c2['people']['mother']['stress'] == 10
        assert eval c2['slept_day'] == 6
        click "返回主菜单" until screen "main_menu"

    testcase gallery:
        pause until screen "main_menu"
        $ wtest_picture('main-menu')
        click "美术资源"
        pause until screen "resource_gallery"
        assert eval len(C1_ASSETS) == 42
        pause 0.3
        $ wtest_picture('gallery')
        click "← 返回"
