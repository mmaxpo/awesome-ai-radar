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
| 🐞 **Open issues + PRs** | [606](https://github.com/charmbracelet/crush/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agentic-ai` `ai` `llms` `ravishing` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2025-05-21 |
| 📦 **Latest release** | [v0.104.0](https://github.com/charmbracelet/crush/releases/tag/v0.104.0) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 40.7 MB |

## 📦 Recent releases

### [v0.104.0](https://github.com/charmbracelet/crush/releases/tag/v0.104.0)
<sub>2026-11-27 · today</sub>

> **Better onboarding + maintenance**
> Hey all, hope all americans are having a great Thanksgiving! 🦃
> **Onboarding**
> We plan to work on the onboarding to help new Crush users. On this release we're shipping a first pass:
> * Before, we skipped the onboarding if any API were found on your ENV. Now we'll always show for new installations.
> * ENVs keep working as expected. If one was found for the chosen provider, Crush will just use it and won't ask you to paste an API key.
> …

### [v0.103.0](https://github.com/charmbracelet/crush/releases/tag/v0.103.0)
<sub>2026-11-26 · today</sub>

> **Client/server, OSC 7511, Turtle 🐢**
> Lots of new stuff in this one, plus a ton of fixes. Read on!
> **Second life 🛟**
> <img width="1000" alt="Rex demo" src="https://github.com/user-attachments/assets/6c0aed7f-7a2e-40be-884b-2ecab27f482d" />
> Terminals that support the Program Resume Protocol (OSC 7577), such as [Rex](https://www.superlogical.com/rex), can now bring Crush back after they restart, whether from an update, a crash, or a reboot. You'll land in the same session, in the same project folder. If you started Crush with a custom data folder or server, those come back too.
> **Client/Server Mode, Now in Your Config**
> …

### [nightly](https://github.com/charmbracelet/crush/releases/tag/nightly) _(pre-release)_
<sub>2026-11-27 · today</sub>

> ---
> <details>
> <summary>Verifying the artifacts</summary>
> First, download the [`checksums.txt` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt) and the [`checksums.txt.sigstore.json` file](https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt.sigstore.json) files, for example, with `wget`:
> ```bash
> wget 'https://github.com/charmbracelet/crush/releases/download/nightly/checksums.txt'
> …

### [v0.102.0](https://github.com/charmbracelet/crush/releases/tag/v0.102.0)
<sub>2026-11-19 · 7d ago</sub>

> **Channels, custom prompts and server hardening**
> There's so much good stuff in this release and we're really proud of _all_ of it. Read on for more.
> **BYO Prompts**
> At last, you can replace the system prompts with…whatever you want. And not just the main agent but prompts for subagents, planning, compaction, session titles and `crush init`:
> ```bash
> option prompt coder ~/.config/crush/prompts/coder.md.tpl
> …

### [v0.101.0](https://github.com/charmbracelet/crush/releases/tag/v0.101.0)
<sub>2026-11-12 · 14d ago</sub>

> **Skill toggles, tool timers and a faster Hyper ⚡**
> This release was brought to you by our team and our favorite contributors! Long awaited features ahead, read along!
> **Toggle skills**
> <img width="600" alt="Screenshot 2026-11-12 at 19 58 39" src="https://github.com/user-attachments/assets/99d45606-bdb9-4f99-8501-72fa7fc4c648" />
> Skills can now be switched on and off right from the command palette. Broken skills are easy to spot, too! (they're marked with a red × and the reason they failed)
> **🕐 How long is this taking?**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [feat: add option to disable subagents (#4453)](https://github.com/charmbracelet/crush/commit/bbd86b427c56a4122ccb5cb1917e4328334de3cf) | andrinoff |
| 2026-11-27 | [v0.104.0](https://github.com/charmbracelet/crush/commit/cb76d94d29d3800571f8ec3b54cc545630b1e23d) | andreynering |
| 2026-11-27 | [chore: update fantasy and catwalk](https://github.com/charmbracelet/crush/commit/1ad0adb2c08f64ce858ec8d4a40d0f8eb6bb6a2e) | andreynering |
| 2026-11-27 | [chore: auto-update files](https://github.com/charmbracelet/crush/commit/bfc989df81423894925216afffd90114580d0380) | charmcli |
| 2026-11-27 | [feat: onboarding ux pass (#4444)](https://github.com/charmbracelet/crush/commit/1bc9788a8db244f2fb97ae91a49c4039de9da9df) | andreynering |
| 2026-11-27 | [chore(legal): @J4ck1e2000 has signed the CLA](https://github.com/charmbracelet/crush/commit/5e7af480dc5ab75055b3b076f5bff33f8d9df5d5) | charmcli |
| 2026-11-27 | [fix(pinentry): keep the gpg passphrase hint out of terminal scrollback](https://github.com/charmbracelet/crush/commit/1396e64601fc8f8e47d18a716718c4cf7cbbcef6) | taciturnaxolotl |
| 2026-11-26 | [v0.103.0](https://github.com/charmbracelet/crush/commit/759183839754ea54ac3b421206817cc0714cb0c8) | andrinoff |
| 2026-11-26 | [feat(mcp): cap large tool output and fix doc link (#4436)](https://github.com/charmbracelet/crush/commit/cff500642bbafdb8b290108bf60f3592ec993861) | andrinoff |
| 2026-11-26 | [chore: add a `.taskrc.yml`](https://github.com/charmbracelet/crush/commit/f84f6c619da6e346e72e095ed00cd79a50bb2d65) | andreynering |

[See all commits ↗](https://github.com/charmbracelet/crush/commits)

## ⬇️ Get it

```bash
git clone https://github.com/charmbracelet/crush.git
```
