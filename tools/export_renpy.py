#!/usr/bin/env python3
"""Generate native Ren'Py chapter labels from the current working manuscript.

Only story_generated.rpy is written. export_story.py supplies the validated,
source-backed narrative model without rewriting the manuscript or JSON export.
Character definitions, screens, start and route_end belong to handwritten UI.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy


REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "docs/chapters/ch01/SCRIPT.md"
OUTPUT = REPO / "game/story_generated.rpy"
CHARACTERS = {
    "陈知远": "char_protagonist", "主角": "char_protagonist",
    "林晚宁": "char_partner", "伴侣": "char_partner",
    "陈建川": "char_father", "父亲": "char_father",
    "周慧敏": "char_mother", "母亲": "char_mother",
}


def quoted(text: str) -> str:
    # With the SDK's default config.old_substitutions=True, say/menu perform
    # percent formatting before screen text sees the value: %% displays as %.
    # Ren'Py also consumes bracket interpolation and text-tag escapes.
    # Apply these to source text exactly once; the rendered wording is unchanged.
    escaped = text.replace("%", "%%").replace("[", "[[").replace("{", "{{")
    return json.dumps(escaped, ensure_ascii=False)


def label_for(scene_id: str) -> str:
    if not re.fullmatch(r"CH01-(?:\d{3}|[ABCD]\d{2})", scene_id):
        raise ValueError(f"Unexpected chapter scene identifier: {scene_id}")
    return scene_id.lower().replace("-", "_")


def load_story(source: Path) -> dict:
    module = runpy.run_path(str(REPO / "tools/export_story.py"))
    data = module["export"](source)
    module["validate"](data)
    assert data["sourceHash"] == hashlib.sha256(source.read_bytes()).hexdigest()
    return data


def say_lines(block: dict) -> list[str]:
    kind, text = block["type"], block["text"]
    if kind == "direction":
        return []  # Visual cues are kept separately from the authoritative manuscript.
    if kind in {"phone", "news"}:
        speaker = block.get("speaker") or ("新闻" if kind == "news" else "讯息")
        return ["    $ phone_mode = True",
                f"    $ phone_speaker = {quoted(speaker)}",
                f"    $ phone_text = {quoted(text)}",
                f"    n {quoted(text)}",
                "    $ phone_mode = False"]
    speaker = block.get("speaker", "")
    # The old phone-qualified role label still occurs in the working manuscript.
    role = re.sub(r"[（(]电话[）)]$", "", speaker)
    character = CHARACTERS.get(role)
    if kind == "dialogue" and character:
        return [f"    {character} {quoted(text)}"]
    if kind == "dialogue" and speaker:
        return [f"    n {quoted(speaker + '：' + text)}"]
    return [f"    n {quoted(text)}"]


def render(data: dict) -> str:
    scenes = data["scenes"]
    ends = {route["end"]: key for key, route in data["routes"].items()}
    lines = [
        "# GENERATED FILE — edit docs/chapters/ch01/SCRIPT.md, then regenerate.",
        "# Generator: python3 tools/export_renpy.py",
        f"# Source: {data['sourcePath']}",
        f"# SHA-256: {data['sourceHash']}",
        "# Visual cues: game/data/ch01_presentation.json; chapter dialogue is unchanged.",
        "# Requires n, char_protagonist, char_partner, char_father, char_mother, route_end.",
        "",
        "define story_choice_descriptions = {" + ", ".join(
            quoted(choice["label"]) + ": " + quoted(choice["description"])
            for choice in data["choices"]
        ) + "}",
        "",
    ]
    for scene in scenes:
        lines.extend([
            f"label {label_for(scene['id'])}:",
            f"    $ current_scene_id = {quoted(scene['id'])}",
            f"    $ current_scene_title = {quoted(scene['title'])}",
            f"    $ current_scene_time = {quoted(scene['time'])}",
            f"    $ current_scene_location = {quoted(scene['location'])}",
            "    $ phone_mode = False",
            f"    $ c1_scene({quoted(scene['id'])})",
        ])
        line_index = 0
        for block in scene["blocks"]:
            if block["type"] != "direction":
                speaker = re.sub(r"[（(]电话[）)]$", "", block.get("speaker", ""))
                lines.append(f"    $ c1_before({quoted(scene['id'])}, {line_index}, {quoted(speaker)})")
                line_index += 1
            lines.extend(say_lines(block))
        if scene["id"] == data["choiceScene"]:
            lines.append("    menu:")
            for choice in data["choices"]:
                lines.extend([f"        {quoted(choice['label'])}:",
                              f"            $ chapter_route = {quoted(choice['id'])}",
                              f"            jump {label_for(choice['target'])}"])
        elif scene["id"] in ends:
            route = ends[scene["id"]]
            lines.extend([f"    $ chapter_route = {quoted(route)}",
                          f"    call route_end({quoted(route)})", "    return"])
        elif scene["next"]:
            lines.append(f"    jump {label_for(scene['next'])}")
        else:
            raise ValueError(f"Non-ending scene has no successor: {scene['id']}")
        lines.append("")
    result = "\n".join(lines)
    validate_output(result, data)
    return result


def validate_output(result: str, data: dict) -> None:
    labels = re.findall(r"^label (\w+):$", result, re.MULTILINE)
    expected = {label_for(scene["id"]) for scene in data["scenes"]}
    assert len(labels) == 30 and set(labels) == expected
    assert all(target in expected for target in re.findall(r"^\s+jump (\w+)$", result, re.MULTILINE))
    assert sorted(re.findall(r'^\s+call route_end\("([ABCD])"\)$', result, re.MULTILINE)) == list("ABCD")
    for choice in data["choices"]:
        assert quoted(choice["description"]) in result, "Choice description omitted"
        assert f"$ chapter_route = {quoted(choice['id'])}\n            jump {label_for(choice['target'])}" in result
    text_blocks = [b for scene in data["scenes"] for b in scene["blocks"] if b["type"] != "direction"]
    rendered_says = re.findall(r"^\s+(?:n|char_protagonist|char_partner|char_father|char_mother) (.+)$", result, re.MULTILINE)
    assert len(rendered_says) == len(text_blocks), "Narrative content dropped or duplicated"
    for encoded in rendered_says:
        assert isinstance(json.loads(encoded), str), "Invalid string escaping"
    assert "scene " not in result and "play music" not in result and "play sound" not in result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = load_story(args.source.resolve())
    output = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    says = sum(block["type"] != "direction" for scene in data["scenes"] for block in scene["blocks"])
    print(f"Exported 30 native Ren'Py scene labels and {says} text blocks to {args.output}")


if __name__ == "__main__":
    main()
