#!/usr/bin/env python3
"""Checks SKILL.md frontmatter against the rules claude.ai applies on upload.

- name and description are present, and name matches the skill's folder
- the description has no angle brackets, which claude.ai reads as XML tags
- the description stays within 1024 characters
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    rel = skill.relative_to(ROOT)
    if not m:
        errors.append(f"{rel}: no frontmatter")
        continue
    fields = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
    name, desc = fields.get("name", ""), fields.get("description", "")
    if name != skill.parent.name:
        errors.append(f"{rel}: name '{name}' does not match folder '{skill.parent.name}'")
    if not desc:
        errors.append(f"{rel}: description missing")
    if "<" in desc or ">" in desc:
        errors.append(f"{rel}: description contains < or >, which claude.ai rejects as XML tags")
    if len(desc) > 1024:
        errors.append(f"{rel}: description is {len(desc)} characters, over 1024")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("OK: skill frontmatter passes.")
