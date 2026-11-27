# garrytan/gstack

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/garrytan/gstack)

> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Garry Tan's Claude Code setup: 23 opinionated role tools |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 142.8k |
| 🍴 **Forks** | 21.1k |
| 🐞 **Open issues + PRs** | [45](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.104.1.0](https://github.com/garrytan/gstack/releases/tag/v1.104.1.0) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 282.6 MB |

## 📦 Recent releases

### [v1.104.1.0](https://github.com/garrytan/gstack/releases/tag/v1.104.1.0) — gstack v1.104.1.0
<sub>2026-11-27 · today</sub>

> **gstack v1.104.1.0**
> **What's new**
> - Upgrading now removes the old `ship` and `cso` skill folders that 1.104.0.0 left behind. ([#4844](https://github.com/garrytan/gstack/pull/4844))
> - `./setup` on Windows now works when your home folder has an apostrophe in its name, such as `C:\Users\O'Brien`. ([#4845](https://github.com/garrytan/gstack/pull/4845))
> - `/gstack-ship` now handles very large results PRs. ([#4847](https://github.com/garrytan/gstack/pull/4847))
> - make-pdf removes `javascript:` links spelled with tabs, line breaks or entity letters. ([#4848](https://github.com/garrytan/gstack/pull/4848))
> …

### [v1.104.0.0](https://github.com/garrytan/gstack/releases/tag/v1.104.0.0) — gstack v1.104.0.0
<sub>2026-11-26 · yesterday</sub>

> **gstack v1.104.0.0**
> **What's new**
> - gstack now picks the newest Opus, Fable, Sol and Astra everywhere it chooses a model. ([#4811](https://github.com/garrytan/gstack/pull/4811))
> - New guide section: you don't need to cut back on MCP servers for accuracy, up to about 300 tools, as long as Claude Code's tool search stays on. ([#4814](https://github.com/garrytan/gstack/pull/4814))
> - /gstack-ship honours a ruled edit after the final review, and a stop on a second-model blocker records. ([#4829](https://github.com/garrytan/gstack/pull/4829))
> - make-pdf's new layout handles three more cases. ([#4828](https://github.com/garrytan/gstack/pull/4828))
> …

### [v1.103.3.0](https://github.com/garrytan/gstack/releases/tag/v1.103.3.0) — gstack v1.103.3.0
<sub>2026-11-25 · 2d ago</sub>

> **gstack v1.103.3.0**
> **What's new**
> - A first version's ruled-out line now counts only against the one reply it cites. ([#4800](https://github.com/garrytan/gstack/pull/4800))
> - A first version's plan can say the owner ruled something out, and that line now counts only when he actually said it. ([#4789](https://github.com/garrytan/gstack/pull/4789))
> - /ship's instructions now match how it reviews code. ([#4779](https://github.com/garrytan/gstack/pull/4779))
> **Fixes**
> …

### [v1.103.1.0](https://github.com/garrytan/gstack/releases/tag/v1.103.1.0) — gstack v1.103.1.0
<sub>2026-11-24 · 3d ago</sub>

> **gstack v1.103.1.0**
> **What's new**
> - `/ship` now tells you what to change when GitHub refuses a push for email privacy. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - `gstack-approvals rule` and `round-grant` now say which `--owner-ref` check failed. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - The merge queue's bisect now accepts a red judge case whose name holds a space. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - /cso reports every security finding the code supports instead of dropping most of them. ([#4739](https://github.com/garrytan/gstack/pull/4739))
> …

### [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — gstack v1.103.0.0
<sub>2026-11-23 · 4d ago</sub>

> **gstack v1.103.0.0**
> This release closes gaps in two of gstack's safety checks and its merge tool, fixes the /ship failures that were stopping pull requests from finishing, and renames `/verify` to `/build-check` so Claude Code's own `/verify` works again. Upgrade with `/gstack-upgrade`.
> **Action needed: `/verify` is now `/build-check`**
> - `/verify` is now `/build-check`, so typing `/verify` opens Claude Code's built-in `/verify` again. Use `/build-check` for gstack's build-and-check loop and `/build-check quick` for the check-only pass. (#4714)
> - If you turned the skill off with `disabled_skills: verify`, change that entry to `build-check`. Until you do, gstack reads `verify` as `build-check`, so the skill stays off after you upgrade. (#4719)
> - gstack no longer runs the check pass before every commit on its own, so the `verify_before_commit` setting is retired. Setting it prints a note and changes nothing, and a config file that still has it keeps working. (#4714)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [v1.104.1.0 release (#4854)](https://github.com/garrytan/gstack/commit/306ff23b9d2bd7951b7f6c408c7376f3237520c9) | garrytan |
| 2026-11-26 | [Review diffs over the 2 MB ceiling in slices instead of stopping (GST…](https://github.com/garrytan/gstack/commit/e3f916bf0d0bdb145e2505b62f3329230f6329e1) | garrytan |
| 2026-11-26 | [/codex cleanup stops asking for /careful approval, and plan-mode Code…](https://github.com/garrytan/gstack/commit/be64b102975afe46f35dd27d3fe7c6908d7c9d5e) | garrytan |
| 2026-11-26 | [Let /gstack-ship handle very large results PRs (GST-4003) (#4847)](https://github.com/garrytan/gstack/commit/77da8a0160e8a651ec328e305a37c8fea140bfbb) | garrytan |
| 2026-11-26 | [Upgrading from inside the gstack checkout no longer reinstalls Codex …](https://github.com/garrytan/gstack/commit/0febbce1e4382b140a930f6a17c53234de2b05e7) | garrytan |
| 2026-11-26 | [The release gate's live /autoplan guard test runs on Haiku 5.5 (GST-3…](https://github.com/garrytan/gstack/commit/aa503e29f4e620a2ab689172c7fb261c7b280874) | garrytan |
| 2026-11-26 | [Make the plan-review test judge reject failed sessions and steady two…](https://github.com/garrytan/gstack/commit/89825888c57ec5ed472f8fea4a715882b401a9e5) | garrytan |
| 2026-11-26 | [make-pdf blocks javascript: links written with tabs or entity letters…](https://github.com/garrytan/gstack/commit/f5b42d682c109db29d127ac9c1a90a264d37d058) | garrytan |
| 2026-11-26 | [Setup works on Windows when the home folder name has an apostrophe (#…](https://github.com/garrytan/gstack/commit/4ec576aaa57ea76be375d4259e6dca7966abfa86) | garrytan |
| 2026-11-26 | [Upgrading removes the leftover ship and cso skill folders (GST-3999) …](https://github.com/garrytan/gstack/commit/fd81a04ba7a85d20c8d2134893f45765df5ee578) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
