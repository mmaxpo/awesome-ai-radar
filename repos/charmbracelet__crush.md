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
| 🐞 **Open issues + PRs** | [596](https://github.com/charmbracelet/crush/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agentic-ai` `ai` `llms` `ravishing` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-05-21 |
| 📦 **Latest release** | [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 39.8 MB |

## 📦 Recent releases

### [nightly](https://github.com/charmbracelet/crush/releases/tag/nightly) _(pre-release)_
<sub>2026-11-26 · today</sub>

> ---
> <details>
> <summary>Verifying the artifacts</summary>
> First, download the [`checksums.txt` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt) and the [`checksums.txt.sigstore.json` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt.sigstore.json) files, for example, with `wget`:
> ```bash
> wget 'https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt'
> …

### [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0)
<sub>2026-11-19 · 6d ago</sub>

> **Channels, custom prompts and server hardening**
> There's so much good stuff in this release and we're really proud of _all_ of it. Read on for more.
> **BYO Prompts**
> At last, you can replace the system prompts with…whatever you want. And not just the main agent but prompts for subagents, planning, compaction, session titles and `crush init`:
> ```bash
> option prompt coder ~/.config/crush/prompts/coder.md.tpl
> …

### [v0.101.0](https://github.com/charmbracelet/crush/releases/tag/v0.101.0)
<sub>2026-11-12 · 13d ago</sub>

> **Skill toggles, tool timers and a faster Hyper ⚡**
> This release was brought to you by our team and our favorite contributors! Long awaited features ahead, read along!
> **Toggle skills**
> <img width="600" alt="Screenshot 2026-11-12 at 19 58 39" src="https://github.com/user-attachments/assets/99d45606-bdb9-4f99-8501-72fa7fc4c648" />
> Skills can now be switched on and off right from the command palette. Broken skills are easy to spot, too! (they're marked with a red × and the reason they failed)
> **🕐 How long is this taking?**
> …

### [v0.100.0](https://github.com/charmbracelet/crush/releases/tag/v0.100.0)
<sub>2026-11-05 · 20d ago</sub>

> **Subagents, Sysadmin Mode, and PGP/SSH Prompts**
> This is a big one! Crush can now run a team of subagents, permissions are much more flexible, and you can now do GPG and SSH auth right inside Crush! Read on for more.
> **👩🏼‍🐰‍👩🏽 Subagents**
> At last, subagents. Crush can now spawn a little team of friendly subagents  in the background, as well as check on them, send them mid-run follow-ups, stop them, or move them to a different model.
> <p><img width="600" alt="image" src="https://github.com/user-attachments/assets/a8f4f437-dd9a-46bb-ab31-65a14b84c07a" /></p>
> You can watch them work right in the transcript, sidebar and header. Every subagent gets its own name, too, so you always know who's doing what. And, if you refer to them by name, Crush will know which of ’em you’re talking about!
> …

### [v0.99.0](https://github.com/charmbracelet/crush/releases/tag/v0.99.0)
<sub>2026-10-29 · 27d ago</sub>

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
| 2026-11-26 | [feat(mcp): cap large tool output and fix doc link (#4436)](https://github.com/charmbracelet/crush/commit/cff500642bbafdb8b290108bf60f3592ec993861) | andrinoff |
| 2026-11-26 | [chore: add a `.taskrc.yml`](https://github.com/charmbracelet/crush/commit/f84f6c619da6e346e72e095ed00cd79a50bb2d65) | andreynering |
| 2026-11-26 | [docs: add the client / server mode specs (#4322)](https://github.com/charmbracelet/crush/commit/70a46fbd8f77fac9b2a5f910f88a685766481d2a) | andrinoff |
| 2026-11-26 | [feat: program resume protocol (OSC 7577) (#4434)](https://github.com/charmbracelet/crush/commit/f79634b5f58b9f6e7682841ff6a7ca30a8846745) | andrinoff |
| 2026-11-26 | [fix(server): stop crush server from leaking the env (#4391)](https://github.com/charmbracelet/crush/commit/e596bad90522445cbf473fae3d4baa0bfc9a9fb3) | andrinoff |
| 2026-11-25 | [chore(legal): @lordrifango has signed the CLA](https://github.com/charmbracelet/crush/commit/152e565f9f63c73d1d61157db1eb31afea46ba8e) | charmcli |
| 2026-11-25 | [feat: integrate `charm.land/turtle` core utilities (#4423)](https://github.com/charmbracelet/crush/commit/fb464363ff54e2dae6286b6ede8096fb51946d74) | andreynering |
| 2026-11-25 | [docs: move the channels out of the README (#4421)](https://github.com/charmbracelet/crush/commit/535dad0ba50cd57e46a17907a76cb861081e1244) | andrinoff |
| 2026-11-25 | [fix(server): stop a new window from getting other sessions' prompts (…](https://github.com/charmbracelet/crush/commit/6e54ac296b159b282433193d2dd21db51b0f2365) | andrinoff |
| 2026-11-25 | [fix(server): title sessions started with a ! command in client/server…](https://github.com/charmbracelet/crush/commit/18bc386b4578a2002980d1e854fb7a512655b4f2) | andrinoff |

[See all commits ↗](https://github.com/charmbracelet/crush/commits)

## ⬇️ Get it

```bash
git clone https://github.com/charmbracelet/crush.git
```
