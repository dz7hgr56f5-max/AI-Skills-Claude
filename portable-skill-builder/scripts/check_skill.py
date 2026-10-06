#!/usr/bin/env python3
"""Check a skill folder for portability. Standard library only.

Usage: python3 check_skill.py path/to/skill-folder
Exit code 0 = no FAIL, 1 = at least one FAIL.
"""
import re
import sys
from pathlib import Path

# Names of product-specific tools that smaller models usually lack.
TOOL_WORDS = [
    "WebSearch", "WebFetch", "AskUserQuestion", "TaskCreate", "TaskUpdate",
    "SendUserFile", "ToolSearch", "Artifact tool", "Bash tool", "mcp__",
]
MAX_BODY_LINES = 150
MAX_DESC_CHARS = 600


def parse(text):
    """Return (frontmatter dict, body) or (None, text) if no frontmatter."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_skill.py path/to/skill-folder")
        return 2
    folder = Path(sys.argv[1]).resolve()
    skill = folder / "SKILL.md"
    results = []

    def add(level, msg):
        results.append((level, msg))

    if not skill.is_file():
        print(f"FAIL: no SKILL.md in {folder}")
        return 1

    text = skill.read_text(encoding="utf-8")
    fm, body = parse(text)
    if fm is None:
        add("FAIL", "SKILL.md must start with --- frontmatter ---")
        fm = {}

    name = fm.get("name", "")
    desc = fm.get("description", "")

    if not name:
        add("FAIL", "frontmatter is missing name")
    else:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            add("FAIL", f"name '{name}' must be lowercase letters, numbers, hyphens")
        if len(name) > 40:
            add("WARN", f"name is {len(name)} characters; keep it under 40")
        if name != folder.name:
            add("FAIL", f"name '{name}' does not match folder '{folder.name}'")

    if not desc:
        add("FAIL", "frontmatter is missing description")
    else:
        if len(desc) > MAX_DESC_CHARS:
            add("WARN", f"description is {len(desc)} characters; keep it under {MAX_DESC_CHARS}")
        if "use when" not in desc.lower():
            add("WARN", "description should include 'Use when' plus trigger phrases")

    body_lines = len(body.strip().splitlines())
    if body_lines > MAX_BODY_LINES:
        add("WARN", f"body is {body_lines} lines; keep it under {MAX_BODY_LINES}")

    for heading in ("## Purpose", "## Instructions", "## Rules"):
        if heading not in body:
            add("WARN", f"missing section '{heading}'")

    for word in TOOL_WORDS:
        if word in body:
            add("WARN", f"mentions product-specific tool '{word}'; use plain words")

    # Files referenced as references/... or scripts/... must exist.
    for rel in sorted(set(re.findall(r"\b((?:references|scripts|assets)/[\w./-]+\w)", body))):
        if not (folder / rel).exists():
            add("FAIL", f"SKILL.md mentions {rel} but it does not exist")

    # Scripts should not need third-party packages.
    stdlib = set(getattr(sys, "stdlib_module_names", []))
    for py in (folder / "scripts").glob("*.py") if (folder / "scripts").is_dir() else []:
        for mod in re.findall(r"^\s*(?:import|from)\s+([A-Za-z_]\w*)", py.read_text(encoding="utf-8"), re.M):
            if stdlib and mod not in stdlib:
                add("WARN", f"{py.name} imports '{mod}', which is not in the standard library")

    fails = sum(1 for lvl, _ in results if lvl == "FAIL")
    warns = sum(1 for lvl, _ in results if lvl == "WARN")
    for lvl, msg in results:
        print(f"{lvl}: {msg}")
    print(f"Result: {fails} FAIL, {warns} WARN ({folder.name})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
