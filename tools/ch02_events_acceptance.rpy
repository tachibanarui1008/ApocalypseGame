# Test-only source copied to an isolated project, never to the shipped game.
default c2e_test_repaired = False
default c2e_test_watch = False

screen c2e_test_wait():
    modal True
    textbutton "开始验证" action Return() align (0.5, 0.5)

screen c2e_test_done():
    modal True
    textbutton "验证完成" action MainMenu(confirm=False) align (0.5, 0.5)

label c2e_test_driver:
    scene black
    call screen c2e_test_wait
    call ch02_rescue_decision
    $ c2_story = c2e_test_finish_contact(c2_story)
    if c2_story["parents_status"] == "deceased":
        call ch02_gate_event(c2e_test_repaired, c2e_test_watch)
    call ch02_storm_epilogue
    if _return == "menu":
        return
    call screen c2e_test_done
    return

init 100 python:
    import os
    from pathlib import Path
    C2E_TEST_OUT = Path(os.environ['C2E_TEST_OUTPUT'])
    def c2e_test_checkpoint():
        (C2E_TEST_OUT / 'checkpoint.json').write_text(json.dumps(c2_story), encoding='utf-8')
    def c2e_test_restored():
        return c2_story == json.loads((C2E_TEST_OUT / 'checkpoint.json').read_text(encoding='utf-8'))
    _test.timeout = 30.0
    _test.maximum_framerate = True

    def c2e_test_finish_contact(s):
        if s['rescue_plan'] == 'pickup':
            s = c2e_day(s, 9 if s['route'] == 'B' else 4)
            s = c2e_parents(s, 'aboard')
            s = c2e_parents(s, 'safe')
            return c2e_day(s, 12)
        s = c2e_day(s, 12)
        s = c2e_parents(s, 'en_route')
        return c2e_parents(s, 'deceased')

testsuite global:
    teardown:
        exit

testsuite ch02_events_acceptance:
    testcase branches:
        parameter (route, outcome, choice, repaired, watch) = [(r, 'deceased', c, p, w) for r in ('B', 'C') for c in ('stay', 'close') for p in (False, True) for w in (False, True)] + [(r, 'safe', 'stay', False, False) for r in ('B', 'C')]
        pause until screen "main_menu"
        run Start('c2e_test_driver')
        pause until screen "c2e_test_wait"
        $ preferences.text_cps = 0
        $ c2_story = c2e_new(route)
        $ c2e_test_repaired = repaired
        $ c2e_test_watch = watch
        click "开始验证"
        advance until screen "choice"
        assert eval c2_story['rescue_plan'] is None
        $ c2e_test_checkpoint()
        run FileSave(2, confirm=False)
        pause 0.2
        $ c2_story = c2e_choose_rescue(c2_story, 'self_arrival')
        run FileLoad(2, confirm=False)
        pause until screen "choice"
        assert eval c2e_test_restored()
        if eval outcome == 'safe':
            click "我们去接，别让他们自己折腾了。"
        else:
            click "这两天先收拾家里，等他们晚点过来。"
        if eval outcome == 'deceased':
            advance until screen "choice"
            assert eval c2_story['gate_opened']
            $ c2e_test_checkpoint()
            run FileSave(1, confirm=False)
            pause 0.2
            $ c2_story = c2e_new('B')
            run FileLoad(1, confirm=False)
            pause until screen "choice"
            assert eval c2e_test_restored()
            if eval choice == 'stay':
                click "留在她身边，让父亲合门"
            else:
                click "先合院门，让母亲陪她回屋"
        advance until screen "c2e_chapter_end"
        assert eval c2_story['day'] == (13 if outcome == 'safe' else 12)
        assert eval c2_story['chapter_outcome'] == ('good' if outcome == 'safe' else 'bad')
        assert eval c2_story['parents_status'] == outcome
        assert eval c2_story['household_size'] == (6 if outcome == 'safe' else 4)
        assert eval c2 is None
        if eval outcome == 'deceased':
            assert eval c2_story['gate_opened']
            assert eval c2_story['intrusion'] == (not (repaired and (choice == 'stay' or watch)))
        else:
            assert eval not c2_story['gate_opened']
        $ c2e_test_checkpoint()
        run FileSave(3, confirm=False)
        pause 0.2
        $ c2_story = c2e_new('B')
        run FileLoad(3, confirm=False)
        pause until screen "c2e_chapter_end"
        assert eval c2e_test_restored()
        if eval outcome == 'safe':
            click "进入第三章" until not screen "c2e_chapter_end"
            pause until screen "c2e_test_done"
            click "验证完成"
        else:
            click "返回主菜单" until not screen "c2e_chapter_end"
        pause until screen "main_menu"
