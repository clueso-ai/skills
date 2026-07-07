#!/usr/bin/env python3
"""Validate skills in this repository against spec/SKILL_SPEC.md.

Stdlib only. Exits non-zero with a list of violations.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FORBIDDEN_DIRS = {".venv", "venv", "node_modules", "__pycache__"}
FORBIDDEN_FILES = re.compile(r"(^\.env(\..*)?$|\.pyc$|\.mp4$|\.mov$|\.zip$|\.tar(\.gz)?$)")
MAX_FILE_BYTES = 1 * 1024 * 1024
MAX_SKILL_BYTES = 5 * 1024 * 1024
MAX_DESCRIPTION_LEN = 1024
REQUIRED_FIELDS = ("name", "description", "license")
REQUIRED_METADATA = ("requires", "external-apis", "external-tools")


def parse_frontmatter(text: str):
    """Minimal YAML frontmatter parser for the subset the spec allows."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fields, metadata = {}, {}
    lines = m.group(1).split("\n")
    i, current_key, in_metadata = 0, None, False
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("  ") and in_metadata:
            km = re.match(r"^\s+([\w-]+):\s*(.*)$", line)
            if km:
                metadata[km.group(1)] = km.group(2).strip().strip("'\"")
            i += 1
            continue
        km = re.match(r"^([\w-]+):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            in_metadata = key == "metadata"
            if val in (">-", ">", "|", "|-"):
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    block.append(lines[i].strip())
                    i += 1
                fields[key] = " ".join(b for b in block if b)
                continue
            if not in_metadata:
                fields[key] = val.strip("'\"")
        i += 1
    if metadata:
        fields["metadata"] = metadata
    return fields


def main() -> int:
    errors = []
    if not SKILLS_DIR.is_dir():
        print("FAIL: skills/ directory missing")
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        errors.append("skills/ contains no skill folders")

    for skill in skill_dirs:
        rel = skill.relative_to(REPO)
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel}: missing SKILL.md")
            continue

        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: SKILL.md has no frontmatter block")
            continue

        for field in REQUIRED_FIELDS:
            if not fm.get(field):
                errors.append(f"{rel}: frontmatter missing required field '{field}'")
        name = fm.get("name", "")
        if name and not NAME_RE.match(name):
            errors.append(f"{rel}: name '{name}' is not lowercase-hyphenated")
        if name and name != skill.name:
            errors.append(f"{rel}: name '{name}' != folder name '{skill.name}'")
        desc = fm.get("description", "")
        if desc and len(desc) > MAX_DESCRIPTION_LEN:
            errors.append(f"{rel}: description exceeds {MAX_DESCRIPTION_LEN} chars ({len(desc)})")
        meta = fm.get("metadata", {})
        for field in REQUIRED_METADATA:
            if not meta.get(field):
                errors.append(f"{rel}: metadata missing required key '{field}'")

        total = 0
        for f in skill.rglob("*"):
            if f.is_dir():
                if f.name in FORBIDDEN_DIRS:
                    errors.append(f"{f.relative_to(REPO)}: forbidden directory")
                continue
            size = f.stat().st_size
            total += size
            if FORBIDDEN_FILES.search(f.name):
                errors.append(f"{f.relative_to(REPO)}: forbidden file type")
            if size > MAX_FILE_BYTES:
                errors.append(f"{f.relative_to(REPO)}: file exceeds 1 MB ({size} bytes)")
        if total > MAX_SKILL_BYTES:
            errors.append(f"{rel}: skill exceeds 5 MB total ({total} bytes)")

    if errors:
        print(f"FAIL: {len(errors)} violation(s)")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(skill_dirs)} skill(s) validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
