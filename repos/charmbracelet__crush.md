# charmbracelet/crush

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/charmbracelet/crush)

> Glamourous agentic coding for all 💘

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Terminal coding agent for any LLM — swap models mid-session, LSP + MCP |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 29.2k |
| 🍴 **Forks** | 2.4k |
| 🐞 **Open issues + PRs** | [585](https://github.com/charmbracelet/crush/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agentic-ai` `ai` `llms` `ravishing` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-05-21 |
| 📦 **Latest release** | [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 39.4 MB |

## 📦 Recent releases

### [nightly](https://github.com/charmbracelet/crush/releases/tag/nightly) _(pre-release)_
<sub>2026-11-24 · today</sub>

> ---
> <details>
> <summary>Verifying the artifacts</summary>
> First, download the [`checksums.txt` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt) and the [`checksums.txt.sigstore.json` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt.sigstore.json) files, for example, with `wget`:
> ```bash
> wget 'https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt'
> …

### [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0)
<sub>2026-11-19 · 4d ago</sub>

> **Channels, custom prompts and server hardening**
> There's so much good stuff in this release and we're really proud of _all_ of it. Read on for more.
> **BYO Prompts**
> At last, you can replace the system prompts with…whatever you want. And not just the main agent but prompts for subagents, planning, compaction, session titles and `crush init`:
> ```bash
> option prompt coder ~/.config/crush/prompts/coder.md.tpl
> …

### [v0.101.0](https://github.com/charmbracelet/crush/releases/tag/v0.101.0)
<sub>2026-11-12 · 11d ago</sub>

> **Skill toggles, tool timers and a faster Hyper ⚡**
> This release was brought to you by our team and our favorite contributors! Long awaited features ahead, read along!
> **Toggle skills**
> <img width="600" alt="Screenshot 2026-11-12 at 19 58 39" src="https://github.com/user-attachments/assets/99d45606-bdb9-4f99-8501-72fa7fc4c648" />
> Skills can now be switched on and off right from the command palette. Broken skills are easy to spot, too! (they're marked with a red × and the reason they failed)
> **🕐 How long is this taking?**
> …

### [v0.100.0](https://github.com/charmbracelet/crush/releases/tag/v0.100.0)
<sub>2026-11-05 · 18d ago</sub>

> **Subagents, Sysadmin Mode, and PGP/SSH Prompts**
> This is a big one! Crush can now run a team of subagents, permissions are much more flexible, and you can now do GPG and SSH auth right inside Crush! Read on for more.
> **👩🏼‍🐰‍👩🏽 Subagents**
> At last, subagents. Crush can now spawn a little team of friendly subagents  in the background, as well as check on them, send them mid-run follow-ups, stop them, or move them to a different model.
> <p><img width="600" alt="image" src="https://github.com/user-attachments/assets/a8f4f437-dd9a-46bb-ab31-65a14b84c07a" /></p>
> You can watch them work right in the transcript, sidebar and header. Every subagent gets its own name, too, so you always know who's doing what. And, if you refer to them by name, Crush will know which of ’em you’re talking about!
> …

### [v0.99.0](https://github.com/charmbracelet/crush/releases/tag/v0.99.0)
<sub>2026-10-29 · 25d ago</sub>

> **Hooks, Catwalk v3!**
> A big one! Crush now runs on Catwalk v3, hooks can see every part of a run, and editors that host Crush get a whole new set of tools to feel right at home.
> **Hooks, everywhere 🪝**
> Hooks are no longer just about tools. They can now follow the whole run: sessions, turns, permissions and more!
> Hooks can now step in after a tool runs, too. Redact secrets from the output before the model sees them, add a note, or stop the turn. If the tool already did something it shouldn't have, your hook can tell the model "you committed without running the tests."
> ```bash
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore(legal): @Luxe7 has signed the CLA](https://github.com/charmbracelet/crush/commit/cd645ef7d0f061ac0c2e893eecad0b37db139dc4) | charmcli |
| 2026-11-24 | [fix(cmd): make --host connect to the server and read sessions there (…](https://github.com/charmbracelet/crush/commit/963ec056279666c5f6acedcdfdd43557dffbbfb1) | andrinoff |
| 2026-11-24 | [fix(cmd): show the workspace creation error once instead of twice (#4…](https://github.com/charmbracelet/crush/commit/aba74b50c09d5487444a899cabeda44e16d1d90f) | andrinoff |
| 2026-11-24 | [server: keep explicit servers and their workspaces alive (#4352)](https://github.com/charmbracelet/crush/commit/11cc53e9d0599bf4d475ef14a2202f3ff2b24ca7) | meowgorithm |
| 2026-11-24 | [chore(legal): @xgbtxy has signed the CLA](https://github.com/charmbracelet/crush/commit/3260032a9abc8467bac6b75e6bde213c5086f03a) | charmcli |
| 2026-11-23 | [ci(labeler): label on a schedule instead of pull_request_target](https://github.com/charmbracelet/crush/commit/603a22ae1eea6baa65d25b411195074bd72f6131) | taciturnaxolotl |
| 2026-11-23 | [feat(ui): show bash and job output live while commands run (#4276)](https://github.com/charmbracelet/crush/commit/ee51fe87bb306a945bf9057edf94f5574b192fd2) | KunoDLK |
| 2026-11-23 | [fix(run): print the whole answer in crush run (#4270)](https://github.com/charmbracelet/crush/commit/a787a05d887dcfea72a04fff3b9e3a4bd08c5000) | AnyCPU |
| 2026-11-22 | [chore(legal): @manelsen has signed the CLA](https://github.com/charmbracelet/crush/commit/46ce1595be55a77feb5c0bb46e7f2cbed7022b79) | charmcli |
| 2026-11-22 | [fix(config): make crushrc exports reach Crush and stop expanding valu…](https://github.com/charmbracelet/crush/commit/7fa693e9373197be757fad530ca9b24634789e99) | taciturnaxolotl |

[See all commits ↗](https://github.com/charmbracelet/crush/commits)

## ⬇️ Get it

```bash
git clone https://github.com/charmbracelet/crush.git
```
