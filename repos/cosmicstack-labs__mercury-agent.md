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
| 🍴 **Forks** | 420 |
| 🐞 **Open issues + PRs** | [37](https://github.com/cosmicstack-labs/mercury-agent/issues) |
| 💻 **Languages** | TypeScript 68% · Kotlin 11% · Swift 10% · Rust 4% · MDX 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `ai-assistant` `llm` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-04-20 |
| 📦 **Latest release** | [captcha-v0.1.0](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/captcha-v0.1.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 68.1 MB |
| 🌐 **Website** | https://mercuryagent.sh/ |

## 📦 Recent releases

### [captcha-v0.1.0](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/captcha-v0.1.0) — CAPTCHA Solver 0.1.0
<sub>2026-11-22 · 3d ago</sub>

> New plugin. Install with `/plugins install captcha`, or **Plugins → CAPTCHA Solver → Install** in Mercury Desktop. Needs Mercury 1.5.5 or newer.
> - **Cheapest first.** Your own vision models read simple image CAPTCHAs for free; two must agree before an answer is used.
> - **A solving service with your key** handles reCAPTCHA v2/v3 (Enterprise too), Cloudflare Turnstile, GeeTest and FunCaptcha: 2Captcha by default, or CapSolver, Anti-Captcha or CapMonster. Solved tokens come with a script that puts them into the page. A daily limit caps paid solves.
> - **You, as the last resort.** If nothing else can, the CAPTCHA goes to your chats, Mercury Desktop and your phones, and the plugin waits for your answer (up to 4 minutes).
> - Also `captcha__detect` (finds CAPTCHAs on a page) and `captcha__balance`.

### [v1.5.5](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.5) — Mercury v1.5.5
<sub>2026-11-22 · 3d ago</sub>

> **☿ Mercury Agent v1.5.5**
> Devices sign in with a device token, Mercury asks you for what only you can do, and bots use fewer tokens.
> **Devices sign in with a device token**
> - **Password sign-in from other devices is now off by default.** To connect a phone, Mercury Desktop or a browser on another computer, make a token on the computer Mercury runs on: `/server token <name>` (or `mercury devices add <name>`), and paste it in. Devices already signed in keep working. Turn password sign-in back on with `/server password on`.
> - **`/server` is easier:** add allowed addresses by typing them, copying a token closes the token screen, and in Mercury Desktop `/server` opens its own Remote access window.
> **Mercury asks you for what only you can do**
> …

### [v1.5.4](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.4) — Mercury v1.5.4
<sub>2026-11-17 · 8d ago</sub>

> **☿ Mercury Agent v1.5.4**
> Set up voice from your phone, and fewer approval prompts.
> **Voice from any device**
> - **Set voice keys from your phone**, with or without Optimus: OpenAI, Gemini, ElevenLabs, Deepgram and more. Mercury checks each key before saving it. A key is never shown back to a device, only its last four characters.
> - **One place for keys.** A key saved from the phone, Mercury Desktop or Optimus is the same key everywhere.
> **Fewer prompts**
> …

### [v1.5.3](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/v1.5.3) — Mercury v1.5.3
<sub>2026-11-17 · 8d ago</sub>

> **☿ Mercury Agent v1.5.3**
> Ready for Mercury on your phone, Google Workspace in one command, and bots that can't be steered by what they read.
> **Mercury on your phone**
> The native iPhone and Android apps connect to this release. They aren't in the app stores yet.
> - **Real-time voice calls.** The phone gets a short-lived token from your Mercury and runs Mercury's own voice engine, so a call answers in about two seconds. Your API keys never leave your computer.
> - **Calls hear you, not the room.** Background talk and noise don't count as you speaking.
> …

### [optimus-v0.5.2](https://github.com/cosmicstack-labs/mercury-agent/releases/tag/optimus-v0.5.2) — Optimus 0.5.2
<sub>2026-11-14 · 11d ago</sub>

> Plugin-only update. Install or update with `/plugins update optimus`, or **Plugins → Optimus → Update** in Mercury Desktop. Works with Mercury 1.3.9 and newer; screenshot sizing per model needs Mercury 1.5.2.
> - **Screenshots sized for the model in use.** Optimus resizes each capture to what the model reads best: Claude and OpenAI 1024×640, Gemini 768×480, open vision models 896×560. Click coordinates stay exact.
> - **No screenshot for models that can't see images.** Optimus says which window is in front instead of sending a picture the model can't read.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/d2d02f30c9522ae6cf825fd34d355a07115ab55b) | mercuryagent |
| 2026-11-24 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/a369c65cd66d8c766eba6e4bb092824c7d68cbe7) | mercuryagent |
| 2026-11-24 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/625afc0a2e5feb7011daf8eb3b9125a460d7f04c) | mercuryagent |
| 2026-11-23 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/91caface60512b81b43cda87eda5797d6f11da4e) | mercuryagent |
| 2026-11-23 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/0e55a5e4d624292fb92540a8d1d3ab3dcffea150) | mercuryagent |
| 2026-11-22 | [chore(badges): refresh download totals [skip ci]](https://github.com/cosmicstack-labs/mercury-agent/commit/a0d87e4485538bab887567dc4bd31928117546b9) | mercuryagent |
| 2026-11-22 | [plugins: CAPTCHA Solver 0.1.0 in the catalog](https://github.com/cosmicstack-labs/mercury-agent/commit/8378eb0309b7fd807489b47b83cc3b597f4eb73b) | hotheadhacker |
| 2026-11-22 | [release: v1.5.5 on mercuryagent.sh (downloads, updates, docs)](https://github.com/cosmicstack-labs/mercury-agent/commit/1610f5738bad37b33055198f6b79dcf9b5eafbdd) | mercuryagent |
| 2026-11-22 | [Mercury 1.5.5: device-token sign-in, owner tasks, cheaper bots](https://github.com/cosmicstack-labs/mercury-agent/commit/5772e7dc181b68ba070b352ad6defacb0df36641) | hotheadhacker |
| 2026-11-22 | [fix(server): add allowed addresses by typing them; /server is its own…](https://github.com/cosmicstack-labs/mercury-agent/commit/b8fdb27de4e967a170441edceb38cd953e43b679) | hotheadhacker |

[See all commits ↗](https://github.com/cosmicstack-labs/mercury-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cosmicstack-labs/mercury-agent.git
```
