"""Chapter-two narrative snapshots; deliberately independent of tutorial inventory.

Event orchestration and six-person resource settlement are not implemented here.
Every transition copies its input for Ren'Py save/rollback compatibility.
"""
from copy import deepcopy


def c2e_new(route):
    if route not in ("B", "C"):
        raise ValueError("只有B/C进入第二章")
    arrival, tutorial = (5, 6) if route == "B" else (2, 3)
    return dict(route=route, arrival_day=arrival, tutorial_day=tutorial,
                day=tutorial, disaster_day=12, parents_status="waiting",
                household_size=4, logistics="normal", recon="none",
                rescue_plan=None, online_delivery_open=True, rooms_seen=[], unlocked_tasks=[],
                chapter_outcome=None, chapter_complete=False,
                gate_opened=False, gate_status="secured", intrusion=False,
                indoor_defence=False, grief=False, support=None, seen_events=[])


def c2e_day(state, day):
    if isinstance(day, bool) or not isinstance(day, int) or day < state["day"] or day > 13:
        raise ValueError("事件日历只能向前推进到Day13；回退由存档快照负责")
    if state["chapter_complete"] and day != state["day"]:
        raise ValueError("章节已结算，不能再推进坏结局或重播日程")
    n = deepcopy(state)
    n["day"] = day
    n["logistics"] = "halted" if day >= 12 else "detour" if day >= 8 else "normal"
    n["online_delivery_open"] = day < 8
    return n


def c2e_choose_rescue(state, plan):
    if plan not in ("pickup", "self_arrival"):
        raise ValueError("未知接应方式")
    if state["rescue_plan"] is not None:
        if state["rescue_plan"] == plan:
            return deepcopy(state)
        raise ValueError("接应方式已一次确认；改选需回到确认前的存档")
    if state["day"] > 7:
        raise ValueError("首次接应约定必须在封锁前完成")
    n = deepcopy(state)
    n["rescue_plan"] = plan
    return n


def c2e_inspect_room(state, room):
    tasks = {"basement": ["PREP-B1"], "radio": ["PREP-RADIO"],
             "server": ["PREP-MEDIA", "PREP-KNOWLEDGE"], "power": ["PREP-POWER"]}
    if room not in tasks:
        raise ValueError("未知房间观察点")
    n = deepcopy(state)
    if room not in n["rooms_seen"]:
        n["rooms_seen"].append(room)
        n["unlocked_tasks"].extend(tasks[room])
    return n


def c2e_parents(state, outcome):
    transitions = {
        "waiting": {"delayed", "aboard", "en_route"},
        "delayed": {"aboard", "en_route"},
        "aboard": {"safe"},
        "en_route": {"deceased"},
        "safe": set(), "deceased": set(),
    }
    plan = state["rescue_plan"]
    if plan is None:
        raise ValueError("必须先确认接应方式")
    allowed = {"pickup": {"delayed", "aboard", "safe"},
               "self_arrival": {"en_route", "deceased"}}[plan]
    if outcome != "waiting" and outcome not in allowed:
        raise ValueError("接应结果与首幕约定不符")
    current = state["parents_status"]
    if outcome == current:
        return deepcopy(state)
    if outcome not in transitions[current]:
        raise ValueError("接应状态不允许此转移")
    if outcome in ("en_route", "deceased") and state["day"] < 12:
        raise ValueError("自行前来途中与遇害确认属于Day12事件")
    if outcome == "aboard" and state["day"] > 10:
        raise ValueError("常规接应窗口已关闭")
    if outcome == "aboard" and state["day"] < (4 if state["route"] == "C" else 9):
        raise ValueError("本版接应尚未进入安排窗口")
    n = deepcopy(state)
    n["parents_status"] = outcome
    n["household_size"] = 6 if outcome == "safe" else 4
    n["grief"] = outcome == "deceased"
    return n


def c2e_gate_open(state):
    if state["day"] != 12 or state["parents_status"] != "deceased":
        raise ValueError("院门事故需要Day12途中遇害确认")
    n = deepcopy(state)
    if "CH02-S05-open" in n["seen_events"]:
        return n
    n["gate_opened"] = True
    n["gate_status"] = "open"
    n["seen_events"].append("CH02-S05-open")
    return n


def c2e_gate_resolve(state, choice, repaired=False, watch_ready=False):
    if choice not in ("stay", "close"):
        raise ValueError("未知院门选择")
    if "CH02-S05-open" not in state["seen_events"]:
        raise ValueError("院门尚未打开")
    if state["day"] != 12:
        raise ValueError("院门处置必须在事故当日完成")
    n = deepcopy(state)
    if "CH02-S05-resolved" in n["seen_events"]:
        return n
    # Staying with her includes an explicit instruction for father to close it.
    secured = repaired and (choice == "stay" or watch_ready)
    n["support"] = "hero_stays" if choice == "stay" else "mother_stays"
    n["gate_status"] = "secured" if secured else "damaged" if choice == "stay" else "open"
    n["intrusion"] = not secured
    n["indoor_defence"] = not secured
    n["seen_events"].append("CH02-S05-resolved")
    return n


def c2e_handoff(state):
    if state["chapter_complete"]:
        return deepcopy(state)
    if state["day"] != 12:
        raise ValueError("第二章章末交接必须发生于Day12")
    if state["parents_status"] not in ("safe", "deceased"):
        raise ValueError("接应必须先形成明确的章末状态")
    if state["parents_status"] == "deceased" and "CH02-S05-resolved" not in state["seen_events"]:
        raise ValueError("途中遇害分支必须经过实际开门和处置")
    good = state["parents_status"] == "safe"
    if state["rescue_plan"] != ("pickup" if good else "self_arrival"):
        raise ValueError("章末结果与接应定线不符")
    n = c2e_day(state, 13) if good else deepcopy(state)
    n["chapter_outcome"] = "good" if good else "bad"
    n["chapter_complete"] = True
    if "CH02-S06" not in n["seen_events"]:
        n["seen_events"].append("CH02-S06")
    return n
