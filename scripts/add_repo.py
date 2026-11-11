"""Append one repo to repos.yml (used by the 'Run workflow' form)."""
import os
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
raw = os.environ.get("REPO", "").strip()
m = re.search(r"(?:github\.com/)?([\w.-]+/[\w.-]+?)(?:\.git)?/?$", raw.split("?")[0].split("#")[0])
if not m:
    sys.exit(f"Couldn't understand repo: {raw!r}")
name = m.group(1)

path = ROOT / "repos.yml"
text = path.read_text()
if re.search(rf"^- repo:\s*{re.escape(name)}\s*$", text, re.M | re.I):
    print(f"{name} is already in the list.")
    sys.exit(0)


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


entry = f"\n- repo: {name}\n  why: {q(os.environ.get('WHY', ''))}\n  status: {os.environ.get('STATUS', 'study')}\n  added: {date.today()}\n"
if os.environ.get("CATEGORY"):
    entry += f"  category: {os.environ['CATEGORY'].strip().lower()}\n"
if os.environ.get("PROJECT"):
    entry += f"  project: {q(os.environ['PROJECT'])}\n"
path.write_text(text.rstrip("\n") + "\n" + entry)
print(f"Added {name}")
