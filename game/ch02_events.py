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
                gate_opened=False, gate_status="secured", intrusion=False,
                indoor_defence=False, grief=False, support=None, seen_events=[])


def c2e_day(state, day):
    if isinstance(day, bool) or not isinstance(day, int) or day < state["day"] or day > 13:
        raise ValueError("事件日历只能向前推进到Day13；回退由存档快照负责")
    n = deepcopy(state)
    n["day"] = day
    n["logistics"] = "halted" if day >= 12 else "detour" if day >= 8 else "normal"
    return n


def c2e_parents(state, outcome):
    transitions = {
        "waiting": {"delayed", "aboard", "en_route"},
        "delayed": {"aboard", "en_route"},
        "aboard": {"safe"},
        "en_route": {"unknown", "deceased"},
        "unknown": {"deceased"},
        "safe": set(), "deceased": set(),
    }
    current = state["parents_status"]
    if outcome == current:
        return deepcopy(state)
    if outcome not in transitions[current]:
        raise ValueError("接应状态不允许此转移")
    if outcome in ("en_route", "unknown", "deceased") and state["day"] < 12:
        raise ValueError("转移途中与章末失联/遇害属于Day12事件")
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
    if state["day"] != 12:
        raise ValueError("第二章章末交接必须发生于Day12")
    if state["parents_status"] not in ("safe", "unknown", "deceased"):
        raise ValueError("接应必须先形成明确的章末状态")
    if state["parents_status"] == "deceased" and "CH02-S05-resolved" not in state["seen_events"]:
        raise ValueError("途中遇害分支必须经过实际开门和处置")
    n = c2e_day(state, 13)
    if "CH02-S06" not in n["seen_events"]:
        n["seen_events"].append("CH02-S06")
    return n
