define n = Character(None)
define char_protagonist = Character("陈知远")
define char_partner = Character("林晚宁")
define char_father = Character("陈建川")
define char_mother = Character("周慧敏")

init python:
    ENDINGS = {
        "A": ("昨日重现", "你曾以为，自己还有足够的时间。", "ACH-001", "BAD END · 01"),
        "B": ("长路归乡", "这一程虽不容易，但幸好，家还在。", "ACH-003", "CHAPTER 01 · 完成"),
        "C": ("长路归乡", "离开熟悉的城市后，家乡的灯光依然为你亮着。", "ACH-003", "CHAPTER 01 · 完成"),
        "D": ("围城", "你以为自己只是暂时没有离开。", "ACH-002", "BAD END · 02"),
    }
    ACHIEVEMENTS = [
        ("ACH-001", "昨日重现", "在归途中遭遇致命危机"),
        ("ACH-002", "围城", "困守沪海市公寓，最终遇难"),
        ("ACH-003", "长路归乡", "成功抵达庐州市城郊安全屋"),
    ]

label start:
    $ c2 = None
    $ chapter_route = None
    $ quick_menu = True
    $ phone_mode = False
    jump ch01_001

label route_end(route):
    $ ending = ENDINGS[route]
    if ending[2] not in persistent.unlocked_achievements:
        $ persistent.unlocked_achievements.append(ending[2])
    if route in ("B", "C"):
        $ persistent.chapter2_unlocked = True
    $ renpy.save_persistent()
    $ quick_menu = False
    call screen chapter_end(route)
    if route == "B" and _return == "continue":
        jump ch02_b_start
    $ quick_menu = True
    return
