"""Append one repo to repos.yml.

Used by the "Run workflow" form (reads REPO, WHY, STATUS, CATEGORY, PROJECT from the
environment) and by the suggestion flow (scripts/approve_suggestion.py imports add()).
"""
import os
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_RE = re.compile(r"(?:github\.com/)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?:\.git)?/?$")


def parse_repo(raw):
    raw = (raw or "").strip().split("?")[0].split("#")[0].strip()
    raw = re.sub(r"/(tree|blob)/.*$", "", raw)  # links to a branch or file
    m = REPO_RE.search(raw)
    return m.group(1) if m else None


def q(s):
    s = " ".join(str(s or "").split())[:200]  # one line, reasonable length
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def add(raw, why="", status="study", category="", project=""):
    """Return (repo_name, added: bool). Raises ValueError if the link can't be understood."""
    name = parse_repo(raw)
    if not name:
        raise ValueError(f"Couldn't understand repo: {raw!r}")
    path = ROOT / "repos.yml"
    text = path.read_text()
    if re.search(rf"^- repo:\s*{re.escape(name)}\s*$", text, re.M | re.I):
        return name, False
    category = re.sub(r"[^a-z0-9_-]", "", (category or "").strip().lower())
    status = status if status in ("study", "using", "later", "done") else "study"
    entry = f"\n- repo: {name}\n  why: {q(why)}\n"
    if category:
        entry += f"  category: {category}\n"
    entry += f"  status: {status}\n  added: {date.today()}\n"
    if project:
        entry += f"  project: {q(project)}\n"
    path.write_text(text.rstrip("\n") + "\n" + entry)
    return name, True


if __name__ == "__main__":
    try:
        name, added = add(os.environ.get("REPO", ""), os.environ.get("WHY", ""),
                          os.environ.get("STATUS", "study"), os.environ.get("CATEGORY", ""),
                          os.environ.get("PROJECT", ""))
    except ValueError as e:
        sys.exit(str(e))
    print(f"Added {name}" if added else f"{name} is already in the list.")
