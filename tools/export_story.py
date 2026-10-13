#!/usr/bin/env python3
"""Export the current chapter-one working manuscript for the text-only prototype.

The manuscript remains the source of truth. Part boundaries exclude route briefs
and production notes; route completion and choice actions are exported as data.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


REPO = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO / "docs/chapters/ch01/SCRIPT.md"
DEFAULT_OUTPUT = REPO / "game/data/ch01.json"
PART = re.compile(r"^# 第([一二三四五六])部分：.+$", re.MULTILINE)
SCENE = re.compile(r"^#{2,3}\s+(CH01-(?:\d{3}|[ABCD]\d{2}))｜(.+)$", re.MULTILINE)
METADATA = re.compile(r"^\*\*(时间|地点|背景)：(.+?)\*\*\s*$")
DIALOGUE = re.compile(r"^\*\*(.+?)：\*\*\s*(.*)$", re.DOTALL)
MARKER = re.compile(r"^【([^】]+)】$")
CHOICE = re.compile(r"^\*\*([ABCD])｜(.+?)\*\*\s*\n\s*\n\*(.+?)\*", re.MULTILINE)
PHONE_MARKERS = {
    "工作群", "聊天消息", "聊天界面", "工作聊天", "家庭群", "购物软件",
    "手机导航", "车机导航", "车机提示", "手机提示", "发送视频",
}
SYSTEM_MARKERS = {"返回主菜单", "等待玩家选择", "B路线结束", "C路线结束"}
SPEAKERS = {"陈知远", "林晚宁", "陈建川", "周慧敏", "主角", "伴侣", "父亲", "母亲"}


def plain(text: str) -> str:
    """Remove presentation delimiters while retaining text, quotes and punctuation."""
    return re.sub(r"\*\*([^*]+)\*\*", r"\1", text).strip().strip("*")


def blocks_for(body: str, scene_id: str) -> list[dict]:
    if scene_id == "CH01-004":
        return []  # All four options are rendered once from choices metadata.
    body = "\n".join(line for line in body.splitlines() if not METADATA.fullmatch(line.strip()))
    blocks: list[dict] = []
    phone_mode = False
    phone_speaker = None
    news_next = False
    pending_speaker = None
    for paragraph in re.split(r"\n\s*\n", body.strip()):
        paragraph = paragraph.strip()
        if not paragraph or paragraph == "---" or METADATA.fullmatch(paragraph):
            continue
        if paragraph.startswith("#") or paragraph == "**成就解锁**":
            continue  # Ending titles/achievements are driven by route metadata.
        marker = MARKER.fullmatch(paragraph)
        if marker:
            label = marker[1]
            if label in SYSTEM_MARKERS or label.startswith(("成就解锁：", "第二章解锁：")):
                continue
            if label in SPEAKERS:
                pending_speaker = label
                if label == "周慧敏":
                    phone_mode = True  # B01's standalone incoming message label.
                continue
            if label.startswith("未读消息："):
                role = label.split("：", 1)[1]
                display_name = {"母亲": "周慧敏", "父亲": "陈建川", "伴侣": "林晚宁"}.get(role, role)
                phone_speaker = f"{display_name}（{role}）· 未读消息" if display_name != role else f"{role} · 未读消息"
                phone_mode = True
            elif label in PHONE_MARKERS:
                phone_mode = True
                phone_speaker = None
            elif label in {"聊天结束", "通话结束", "视频结束"}:
                phone_mode = False
                phone_speaker = None
            elif label in {"手机新闻", "新闻"}:
                news_next = True
                phone_mode = False
            elif label.startswith(("背景：", "场景：", "画面", "转场", "镜头转场")):
                phone_mode = False
            blocks.append({"type": "direction", "text": label})
            continue
        if pending_speaker:
            blocks.append({"type": "phone" if phone_mode else "dialogue",
                           "speaker": pending_speaker, "text": plain(paragraph)})
            pending_speaker = None
            continue
        dialogue = DIALOGUE.fullmatch(paragraph)
        if dialogue:
            blocks.append({"type": "phone" if phone_mode else "dialogue",
                           "speaker": dialogue[1], "text": plain(dialogue[2])})
            continue
        if paragraph.startswith(">"):
            text = "\n".join(re.sub(r"^> ?", "", line) for line in paragraph.splitlines())
            blocks.append({"type": "news", "text": plain(text)})
            news_next = False
            continue
        if news_next:
            blocks.append({"type": "news", "text": plain(paragraph)})
            news_next = False
            continue
        if phone_mode and (paragraph.startswith("**") or paragraph.startswith("“")
                           or paragraph.startswith(("搜索：", "订单已", "预计", "目的地：", "推荐路线"))):
            block = {"type": "phone", "text": plain(paragraph)}
            if phone_speaker:
                block["speaker"] = phone_speaker
            blocks.append(block)
            continue
        blocks.append({"type": "narration", "text": plain(paragraph)})
        if paragraph not in {"过了一会儿。", "几分钟后。", "回复："}:
            phone_mode = False  # Conservative: ordinary narration ends device mode.
            phone_speaker = None
    if pending_speaker:
        raise ValueError(f"Unconsumed standalone speaker in {scene_id}: {pending_speaker}")
    return blocks


def export(source: Path) -> dict:
    raw = source.read_bytes()
    script = raw.decode("utf-8")
    part_matches = list(PART.finditer(script))
    if [m[1] for m in part_matches[:6]] != list("一二三四五六"):
        raise ValueError("Expected five narrative parts followed by production part six")
    scenes = []
    for index, route in enumerate(["COMMON", "A", "B", "C", "D"]):
        part = script[part_matches[index].start():part_matches[index + 1].start()]
        matches = list(SCENE.finditer(part))
        for position, match in enumerate(matches):
            end = matches[position + 1].start() if position + 1 < len(matches) else len(part)
            body = part[match.end():end]
            meta = {}
            for line in body.splitlines():
                item = METADATA.fullmatch(line.strip())
                if item:
                    meta[item[1]] = item[2]
            scenes.append({
                "id": match[1], "title": match[2], "time": meta.get("时间", ""),
                "location": meta.get("地点", ""),
                "bg": re.findall(r"BG-\d{2}", meta.get("背景", "")), "route": route,
                "blocks": blocks_for(body, match[1]),
                "next": matches[position + 1][1] if position + 1 < len(matches) else None,
            })
    choices = [{"id": m[1], "label": m[2], "description": m[3], "target": f"CH01-{m[1]}01"}
               for m in CHOICE.finditer(script[script.index("## CH01-004"):script.index("# 第二部分")])]
    achievements = [{"id": m[1], "title": m[2].strip(), "description": m[3].strip()}
                    for m in re.finditer(r"^\| (ACH-\d{3}) \| ([^|]+) \| [^|]+ \| ([^|]+) \|$", script, re.MULTILINE)]
    routes = {
        "A": {"end": "CH01-A06", "title": "昨日重现", "achievement": "ACH-001", "kind": "bad"},
        "B": {"end": "CH01-B07", "title": "长路归乡", "achievement": "ACH-003", "kind": "home"},
        "C": {"end": "CH01-C06", "title": "长路归乡", "achievement": "ACH-003", "kind": "home"},
        "D": {"end": "CH01-D07", "title": "围城", "achievement": "ACH-002", "kind": "bad"},
    }
    data = {"schemaVersion": 1, "chapter": {"id": "ch01", "title": "晦暗阴云"},
            "start": "CH01-001", "scenes": scenes, "choiceScene": "CH01-004",
            "choices": choices, "routes": routes, "achievements": achievements,
            "sourceHash": hashlib.sha256(raw).hexdigest(),
            "sourcePath": source.relative_to(REPO).as_posix() if source.is_relative_to(REPO) else str(source),
            "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    validate(data)
    return data


def validate(data: dict) -> None:
    scenes = data["scenes"]
    ids = {scene["id"] for scene in scenes}
    expected = {f"CH01-{i:03d}" for i in range(1, 5)}
    expected |= {f"CH01-{route}{i:02d}" for route, count in {"A": 6, "B": 7, "C": 6, "D": 7}.items()
                 for i in range(1, count + 1)}
    assert len(scenes) == 30 and ids == expected, "Missing or duplicate narrative scenes"
    assert [c["id"] for c in data["choices"]] == list("ABCD"), "Missing choices"
    assert {a["id"] for a in data["achievements"]} == {"ACH-001", "ACH-002", "ACH-003"}
    assert len(data["achievements"]) == 3
    assert all(c["target"] in ids for c in data["choices"])
    for scene in scenes:
        assert scene["next"] is None or scene["next"] in ids
        if scene["next"]:
            target = next(s for s in scenes if s["id"] == scene["next"])
            assert target["route"] == scene["route"], "Automatic cross-route transition"
        assert all(b["type"] in {"narration", "dialogue", "phone", "news", "direction"}
                   and b["text"] for b in scene["blocks"])
    for route, spec in data["routes"].items():
        end = next(s for s in scenes if s["id"] == spec["end"])
        assert end["route"] == route and end["next"] is None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = export(args.source.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(data['scenes'])} scenes, 4 choices and 3 achievements to {args.output}")


if __name__ == "__main__":
    main()
