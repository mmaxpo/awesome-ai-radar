# cosmicstack-labs/mercury-agent

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/cosmicstack-labs/mercury-agent)

> Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access. Runs 24/7 from CLI, Telegram or More.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Always-on AI agent you message via WhatsApp, Telegram or Slack |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.1k |
| 🍴 **Forks** | 414 |
| 🐞 **Open issues + PRs** | [31](https://github.com/cosmicstack-labs/mercury-agent/issues) |
| 💻 **Languages** | TypeScript 68% · Kotlin 11% · Swift 10% · Rust 4% · MDX 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `ai-assistant` `llm` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-04-20 |
| 📦 **Latest release** | [v1.5.4](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.4) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 67.5 MB |
| 🌐 **Website** | https://mercuryagent.sh/ |

## 📦 Recent releases

### [v1.5.4](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.4) — Mercury v1.5.4
<sub>2026-11-17 · 4d ago</sub>

> **☿ Mercury Agent v1.5.4**
> Set up voice from your phone, and fewer approval prompts.
> **Voice from any device**
> - **Set voice keys from your phone**, with or without Optimus: OpenAI, Gemini, ElevenLabs, Deepgram and more. Mercury checks each key before saving it. A key is never shown back to a device, only its last four characters.
> - **One place for keys.** A key saved from the phone, Mercury Desktop or Optimus is the same key everywhere.
> **Fewer prompts**
> …

### [v1.5.3](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.3) — Mercury v1.5.3
<sub>2026-11-17 · 4d ago</sub>

> **☿ Mercury Agent v1.5.3**
> Ready for Mercury on your phone, Google Workspace in one command, and bots that can't be steered by what they read.
> **Mercury on your phone**
> The native iPhone and Android apps connect to this release. They aren't in the app stores yet.
> - **Real-time voice calls.** The phone gets a short-lived token from your Mercury and runs Mercury's own voice engine, so a call answers in about two seconds. Your API keys never leave your computer.
> - **Calls hear you, not the room.** Background talk and noise don't count as you speaking.
> …

### [optimus-v0.5.2](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/optimus-v0.5.2) — Optimus 0.5.2
<sub>2026-11-14 · 7d ago</sub>

> Plugin-only update. Install or update with `/plugins update optimus`, or **Plugins → Optimus → Update** in Mercury Desktop. Works with Mercury 1.3.9 and newer; screenshot sizing per model needs Mercury 1.5.2.
> - **Screenshots sized for the model in use.** Optimus resizes each capture to what the model reads best: Claude and OpenAI 1024×640, Gemini 768×480, open vision models 896×560. Click coordinates stay exact.
> - **No screenshot for models that can't see images.** Optimus says which window is in front instead of sending a picture the model can't read.

### [v1.5.2](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.2) — Mercury v1.5.2
<sub>2026-11-12 · 8d ago</sub>

> **☿ Mercury Agent v1.5.2**
> Watch your bots work live, approve things one at a time, and get complex jobs done properly. Chats run at the same time, memory keeps one copy of each thing, and text Mercury reads can't steer it.
> **Getting real work done**
> - **Complex chat work follows Mercury Code's rules.** Once the chat makes a plan:
>   - it acts instead of announcing;
>   - it checks what it made before calling it done;
> …

### [v1.5.1](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.1) — Mercury v1.5.1
<sub>2026-11-03 · 17d ago</sub>

> **☿ Mercury Agent v1.5.1**
> Reading aloud and voice typing now use the voice you chose, Gemini included, and the Optimus update button tells you what it did.
> **Speech**
> - **Your voice choice counts everywhere.** Reading a reply aloud, voice typing and voice notes from Telegram or WhatsApp use the voice service chosen in Settings → Voice when it has a key. A fresh install with only a Gemini key no longer asks for an OpenAI key.
> - **Gemini speaks and listens.** Gemini reads replies aloud (about 4 seconds for a sentence) and transcribes what you say, with the same key Optimus uses. A Gemini model that's busy or retired falls through to the next one.
> - **The "needs a speech service" notice** points to Voice settings and names every option (Gemini, OpenAI, Deepgram, ElevenLabs) instead of an "Add OpenAI key" button.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [chore(site): rebuild with the blog fixes from #314](https://github.com/cosmicstack-labs/mercury-agent/commit/cb6692180715d816e458d33c4a598fc7452b936f) | hotheadhacker |
| 2026-11-21 | [Merge PR #314 from tashiriskhan: blog fixes](https://github.com/cosmicstack-labs/mercury-agent/commit/7cbb88dfeb820fa322af6f095cba7adf968b9c3d) | hotheadhacker |
| 2026-11-21 | [feat(skills): Any to PDF as a built-in skill, dependencies installed …](https://github.com/cosmicstack-labs/mercury-agent/commit/5b00d8173f059efad0667c6529b2ab088eba1d3c) | hotheadhacker |
| 2026-11-21 | [feat(bots): auto mode — bots decide permission asks at once (ADR-047)](https://github.com/cosmicstack-labs/mercury-agent/commit/b55b76e823e4a213f2b9afcc219fd9fdbf9757e4) | hotheadhacker |
| 2026-11-21 | [perf(bots): fewer steps per run, and work kept at the token cap](https://github.com/cosmicstack-labs/mercury-agent/commit/1a5f2da5423359528d9f321e5a83703049681cee) | hotheadhacker |
| 2026-11-21 | [perf(bots): make prompt caching work in bot runs](https://github.com/cosmicstack-labs/mercury-agent/commit/afbbf4f7e6f73b08d59faeed7603dfa66e971a5c) | hotheadhacker |
| 2026-11-21 | [fix(reach): a call to a named device rings only that device](https://github.com/cosmicstack-labs/mercury-agent/commit/85b2c0cc4dccbb847754afaa0b24798a6667f540) | hotheadhacker |
| 2026-11-21 | [Restore six-agents slug to keep live URL](https://github.com/cosmicstack-labs/mercury-agent/commit/a5d01ade7f6390b52f7006efea8a44e4125abda7) | tashiriskhan |
| 2026-11-21 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/daa5ff3d0d9ef922700cee907650566e17d3c388) | mercuryagent |
| 2026-11-20 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/382579ba0a36524e2bd6da0438d2e21d4e73525c) | mercuryagent |

[See all commits ↗](https://github.com/cosmicstack-labs/mercury-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cosmicstack-labs/mercury-agent.git
```
