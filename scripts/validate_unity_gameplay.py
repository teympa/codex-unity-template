#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GAMEPLAY_DIR = ROOT / "Assets" / "Scripts" / "Gameplay"

FRAME_METHODS = ("Update", "FixedUpdate", "LateUpdate")
LINQ_CALLS = ("Where", "Select", "ToList", "ToArray")
FIND_PATTERNS = (
    "GameObject.Find",
    "FindObjectOfType",
    "FindAnyObjectByType",
)

SUSPICIOUS_NUMBER_RE = re.compile(
    r"(?<![\w.])(?:const\s+)?(?:int|float|double)\s+\w+\s*=\s*(-?\d+(?:\.\d+)?)\s*;"
)
INSTANCE_RE = re.compile(r"public\s+static\s+\w+(?:<[^>]+>)?\s+Instance\s*(?:[;{=])")
METHOD_RE = re.compile(
    r"(?P<indent>^[ \t]*)"
    r"(?:(?:public|private|protected|internal)\s+)?"
    r"(?:(?:new|virtual|override|sealed|async|static|unsafe|extern)\s+)*"
    r"(?:void|IEnumerator)\s+"
    r"(?P<name>Update|FixedUpdate|LateUpdate)\s*\([^)]*\)\s*"
    r"\{",
    re.MULTILINE,
)


def should_flag_number(value: float) -> bool:
    if value in (-1.0, 0.0, 1.0, 2.0):
        return False
    return True


def line_number_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def extract_method_body(text: str, start_index: int) -> str:
    brace_depth = 0
    body_start = text.find("{", start_index)
    if body_start == -1:
        return ""

    for index in range(body_start, len(text)):
        char = text[index]
        if char == "{":
            brace_depth += 1
        elif char == "}":
            brace_depth -= 1
            if brace_depth == 0:
                return text[body_start + 1 : index]
    return text[body_start + 1 :]


def inspect_file(path: Path) -> list[str]:
    findings: list[str] = []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        findings.append(f"{path}: file is not readable as UTF-8")
        return findings

    for match in SUSPICIOUS_NUMBER_RE.finditer(text):
        value_text = match.group(1)
        try:
            value = float(value_text)
        except ValueError:
            continue

        if should_flag_number(value):
            line = line_number_for(text, match.start())
            findings.append(
                f"{path}:{line}: suspicious hardcoded value `{value_text}` in gameplay code"
            )

    for pattern in FIND_PATTERNS:
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            line = line_number_for(text, index)
            findings.append(f"{path}:{line}: avoid `{pattern}` in gameplay code")
            start = index + len(pattern)

    for match in INSTANCE_RE.finditer(text):
        line = line_number_for(text, match.start())
        findings.append(
            f"{path}:{line}: public static Instance suggests adding another singleton"
        )

    for method_match in METHOD_RE.finditer(text):
        method_name = method_match.group("name")
        body = extract_method_body(text, method_match.start())
        line = line_number_for(text, method_match.start())

        if "GetComponent<" in body or "GetComponent(" in body:
            findings.append(
                f"{path}:{line}: `{method_name}` contains per-frame `GetComponent` usage"
            )

        for linq_call in LINQ_CALLS:
            if f".{linq_call}(" in body:
                findings.append(
                    f"{path}:{line}: `{method_name}` contains LINQ call `.{linq_call}()`"
                )

        if re.search(r'"[^"\n]*"\s*\+\s*[\w("]', body) or re.search(
            r"[\w)\"]\s*\+\s*\"[^\"\n]*\"", body
        ):
            findings.append(
                f"{path}:{line}: `{method_name}` may concatenate strings every frame"
            )

    return findings


def main() -> int:
    if not GAMEPLAY_DIR.exists():
        print(f"skip: {GAMEPLAY_DIR} does not exist")
        return 0

    files = sorted(GAMEPLAY_DIR.rglob("*.cs"))
    findings: list[str] = []

    for file_path in files:
        findings.extend(inspect_file(file_path))

    if findings:
        print("Unity gameplay validation failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Unity gameplay validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
