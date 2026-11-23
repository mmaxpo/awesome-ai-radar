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
| 🐞 **Open issues + PRs** | [578](https://github.com/charmbracelet/crush/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agentic-ai` `ai` `llms` `ravishing` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2025-05-21 |
| 📦 **Latest release** | [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 37.1 MB |

## 📦 Recent releases

### [nightly](https://github.com/charmbracelet/crush/releases/tag/nightly) _(pre-release)_
<sub>2026-11-23 · today</sub>

> ---
> <details>
> <summary>Verifying the artifacts</summary>
> First, download the [`checksums.txt` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt) and the [`checksums.txt.sigstore.json` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt.sigstore.json) files, for example, with `wget`:
> ```bash
> wget 'https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt'
> …

### [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0)
<sub>2026-11-19 · 3d ago</sub>

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
<sub>2026-11-05 · 17d ago</sub>

> **Subagents, Sysadmin Mode, and PGP/SSH Prompts**
> This is a big one! Crush can now run a team of subagents, permissions are much more flexible, and you can now do GPG and SSH auth right inside Crush! Read on for more.
> **👩🏼‍🐰‍👩🏽 Subagents**
> At last, subagents. Crush can now spawn a little team of friendly subagents  in the background, as well as check on them, send them mid-run follow-ups, stop them, or move them to a different model.
> <p><img width="600" alt="image" src="https://github.com/user-attachments/assets/a8f4f437-dd9a-46bb-ab31-65a14b84c07a" /></p>
> You can watch them work right in the transcript, sidebar and header. Every subagent gets its own name, too, so you always know who's doing what. And, if you refer to them by name, Crush will know which of ’em you’re talking about!
> …

### [v0.99.0](https://github.com/charmbracelet/crush/releases/tag/v0.99.0)
<sub>2026-10-29 · 24d ago</sub>

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
| 2026-11-23 | [feat(ui): show bash and job output live while commands run (#4276)](https://github.com/charmbracelet/crush/commit/ee51fe87bb306a945bf9057edf94f5574b192fd2) | KunoDLK |
| 2026-11-23 | [fix(run): print the whole answer in crush run (#4270)](https://github.com/charmbracelet/crush/commit/a787a05d887dcfea72a04fff3b9e3a4bd08c5000) | AnyCPU |
| 2026-11-22 | [chore(legal): @manelsen has signed the CLA](https://github.com/charmbracelet/crush/commit/46ce1595be55a77feb5c0bb46e7f2cbed7022b79) | charmcli |
| 2026-11-22 | [fix(config): make crushrc exports reach Crush and stop expanding valu…](https://github.com/charmbracelet/crush/commit/7fa693e9373197be757fad530ca9b24634789e99) | taciturnaxolotl |
| 2026-11-21 | [chore(legal): @AynSiddiqui has signed the CLA](https://github.com/charmbracelet/crush/commit/d63960b5147b94593ff50efefd1afa3fc4aface8) | charmcli |
| 2026-11-21 | [feat: allow to change the model and reasoning during a run (#4325)](https://github.com/charmbracelet/crush/commit/3d00da85c17004fecc68a5f6d0c5a854aee336ba) | andrinoff |
| 2026-11-21 | [chore(nix): update nixpkgs so the dev shell's linter can read Go 1.27…](https://github.com/charmbracelet/crush/commit/6ce1491d406974f3610cf755b27ab1096451feb4) | taciturnaxolotl |
| 2026-11-21 | [chore(legal): @2118505078xyh1 has signed the CLA](https://github.com/charmbracelet/crush/commit/db7c905f8df5e3893e33ba44322f9dae2dca668d) | charmcli |
| 2026-11-20 | [Fix/bash process cleanup (#4339)](https://github.com/charmbracelet/crush/commit/07f4baf0ef02269b8efbf3c5f4d3720d104dd592) | janearc |
| 2026-11-20 | [server: only log source in debug mode, with a short path](https://github.com/charmbracelet/crush/commit/db8e2efc4ecbf48a2b43facbdb3ba0055190401d) | meowgorithm |

[See all commits ↗](https://github.com/charmbracelet/crush/commits)

## ⬇️ Get it

```bash
git clone https://github.com/charmbracelet/crush.git
```
