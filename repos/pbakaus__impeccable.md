# pbakaus/impeccable

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pbakaus/impeccable)

> The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Front-end design quality skill: shape, critique, polish, animate |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 110.1k |
| 🍴 **Forks** | 6.6k |
| 🐞 **Open issues + PRs** | [62](https://github.com/pbakaus/impeccable/issues) |
| 💻 **Languages** | Rust 77% · JavaScript 20% · TypeScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai` `anti-slop` `design` `slop` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2025-11-16 |
| 📦 **Latest release** | [cli-v4.9.1](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.9.1) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 886.0 MB |
| 🌐 **Website** | https://impeccable.style |

## 📦 Recent releases

### [cli-v4.9.1](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.9.1) — CLI 4.9.1
<sub>2026-11-14 · today</sub>

> - **New verbs.** `world` seeds DESIGN.md from a catalog world, `walkthrough` turns a recording into a walkthrough card, and `foundations` checks launch readiness from local files.
> - **Loop.** `loop connect` now teaches your agents to ask through Needs you.

### [skill-v4.9.1](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.9.1) — Skill 4.9.1
<sub>2026-11-14 · today</sub>

> - **Start from a world.** `impeccable world <id>` writes that world's design system as your DESIGN.md, beside PRODUCT.md, and never overwrites one you have. Later direction rounds name the world you chose instead of dealing new ones. Needs a signed-in account.
> - **Live on a first page.** In an empty folder, Live says there is no page yet and offers to craft one, instead of leaving files behind. A plain HTML page gets its one-line config written for it. The first pick works on a bare element, and a first session tells you what to click.
> - **Live edits stay on their line.** Live can wrap an element that shares its line with other markup, and accepting a variant never removes the rest of that line.
> - **Walkthroughs from any recording.** `impeccable walkthrough` turns a screen recording into an MP4, a poster and chapters, ready for a Needs you walkthrough card.
> - **Agents that use Loop.** `impeccable loop connect` now teaches your coding agents to ask through Needs you, and tells them that Loop wakes them when you answer.
> - **Foundations from your files.** `impeccable foundations` checks 16 of its 18 launch items from local files. It leaves an item unchecked when it couldn't see enough to be sure, for example a stylesheet a build hasn't produced yet.

### [engine-v0.1.24](https://github.com/pbakaus/impeccable/releases/tag/engine-v0.1.24) — impeccable engine engine-v0.1.24
<sub>2026-11-13 · today</sub>

> Prebuilt impeccable engine binaries (engine-v0.1.24). The launcher, the npm shim and impeccable install download these on first run. Docs: https://impeccable.style

### [cli-v4.9.0](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.9.0) — CLI 4.9.0
<sub>2026-11-13 · yesterday</sub>

> - **What a signed-in CLI saves.** Design health, foundations, DESIGN.md, critique reports and setup status, each with its own off and forget command.
> - **Behind a proxy.** Downloads honor `NO_PROXY`, and a GitHub outage during a download is named as one.

### [skill-v4.9.0](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.9.0) — Skill 4.9.0
<sub>2026-11-13 · yesterday</sub>

> - **What a signed-in CLI saves.** If you sign in with `impeccable login`, a full `detect` of a git repo saves its design health counts and the foundations it found, never your code or file names. Your DESIGN.md and each critique report your agent saves upload in full, and the first upload of each tells you so and names its off command. Setup status reports once a day which coding agents have Impeccable. Each one has its own off switch (`impeccable health off`, `impeccable health design off`, `impeccable critiques off`, `impeccable setup off`), and `forget` deletes what was saved. Nothing is saved on CI.
> - **Codex's design hook sees shell writes.** Codex writes most files through the shell, so the end-of-turn pass used to scan nothing in about half of sessions. It now checks every UI file changed since the session began.
> - **A fair shot for every direction.** Before dealing directions for a new look, the skill asks only about the product and proposes no look of its own. A product your brief names, like Linear or Stripe, now sets the quality bar instead of fixing the style, so the dealt directions still get a fair look.
> - **Audit keeps its report.** `audit` saves its findings next to critique's, and one `reports` setting turns saving on or off for both.
> - **Smaller fixes.** A boot note points to `/impeccable doctor` when the design hook isn't installed. Live mode keeps page fonts in captures and keeps an accepted variant styled on static pages. The engine honors `NO_PROXY`. Subagents can reach your MCP tools. `audit` checks right-to-left layouts. Codex's plugin hooks run on Windows, thanks to @MaxFabian25 for the report and @zhangkom for the fix.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [Merge pull request #1461 from pbakaus/feat/cli-first-signin-scan](https://github.com/pbakaus/impeccable/commit/1995764b4936f2bfbf4eb719cb37b384a45ceacb) | pbakaus |
| 2026-11-14 | [Sync generated provider output](https://github.com/pbakaus/impeccable/commit/fb46cc6e356253a5d9945c4e3667c20c3d699cc8) | github-actions[bot] |
| 2026-11-14 | [Merge remote-tracking branch 'origin/main' into feat/cli-first-signin…](https://github.com/pbakaus/impeccable/commit/9d37e58e35d19d45724d4ee2a0d9ceaa929227ba) | pbakaus |
| 2026-11-14 | [Merge pull request #1460 from pbakaus/fix/typeset-token-cap](https://github.com/pbakaus/impeccable/commit/c346a9bcd7b6089cb726295fe612d14b590eaf57) | pbakaus |
| 2026-11-14 | [Fix: check sync under the health.json lock before writing a first-sca…](https://github.com/pbakaus/impeccable/commit/a2e2686d5a66c62af3dea80cd5700e10917ac591) | pbakaus |
| 2026-11-14 | [Fix: sign-in scan review findings](https://github.com/pbakaus/impeccable/commit/544b2abbd7c8900bfa469ae8d8f1daebf0fad27c) | pbakaus |
| 2026-11-14 | [Feat: the first CLI sign-in in a repository adds it to the account](https://github.com/pbakaus/impeccable/commit/8db7a0c2a7ea5647afff06d465055cec1d1c262e) | pbakaus |
| 2026-11-14 | [Fix: raise the typeset cap for the optical alignment section](https://github.com/pbakaus/impeccable/commit/539bf1d1fee92fb106e0a48378cfb4357b5522a9) | pbakaus |
| 2026-11-14 | [Merge pull request #1459 from pbakaus/feat/loop-taste-block](https://github.com/pbakaus/impeccable/commit/61e73eebd34a845df0bfef463eb0d31ed4eab581) | pbakaus |
| 2026-11-14 | [Merge pull request #1377 from thoughtleader/docs/typeset-optical-alig…](https://github.com/pbakaus/impeccable/commit/9272526cbd11eff91f0842d383be099f30fc3ff9) | pbakaus |

[See all commits ↗](https://github.com/pbakaus/impeccable/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pbakaus/impeccable.git
```
