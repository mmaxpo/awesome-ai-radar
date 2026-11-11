"""Add the repo from a "Suggest a repo" issue to repos.yml.

Reads the issue body (ISSUE_BODY) and the approving comment (COMMENT, e.g. "/approve agents"
to override the category). Writes `repo`, `added` and `message` to $GITHUB_OUTPUT.
"""
import os
import re
import sys
import uuid

sys.path.insert(0, os.path.dirname(__file__))
from add_repo import add  # noqa: E402


def field(body, heading):
    """Issue forms render each field as '### Heading' followed by the answer."""
    m = re.search(rf"^###\s*{re.escape(heading)}\s*$(.*?)(?=^###\s|\Z)", body, re.M | re.S)
    if not m:
        return ""
    value = m.group(1).strip()
    return "" if value == "_No response_" else value


def output(**kv):
    path = os.environ.get("GITHUB_OUTPUT")
    lines = []
    for k, v in kv.items():
        d = f"EOF_{uuid.uuid4().hex}"
        lines.append(f"{k}<<{d}\n{v}\n{d}\n")
    if path:
        with open(path, "a") as f:
            f.writelines(lines)
    print("".join(lines))


body = os.environ.get("ISSUE_BODY", "")
comment = os.environ.get("COMMENT", "").strip().split()
repo = field(body, "Repository link")
why = field(body, "Why is it worth following?")
category = field(body, "Category")
if len(comment) > 1:  # "/approve agents" overrides the category
    category = comment[1]
if category.lower().startswith("other") or category.lower() == "not sure":
    category = ""
category = category.split(" ")[0]  # dropdown values look like "agents — Agent frameworks"

try:
    name, added = add(repo, why, "study", category)
except ValueError as e:
    output(repo="", added="false", message=f"⚠️ {e}")
    sys.exit(0)

if added:
    output(repo=name, added="true",
           message=f"✅ Added **[{name}](https://github.com/{name})** to the radar — thanks for the suggestion! "
                   "It will appear in the README in a minute or two.")
else:
    output(repo=name, added="false", message=f"ℹ️ **{name}** is already on the radar — thanks anyway!")
