# letta-ai/letta

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/letta-ai/letta)

> Platform for stateful agents: AI with advanced memory that can learn and self-improve over time.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Stateful agents with long-term memory (ex-MemGPT) |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 25.4k |
| 🍴 **Forks** | 2.7k |
| 🐞 **Open issues + PRs** | [0](https://github.com/letta-ai/letta/issues) |
| 💻 **Languages** | — |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `llm` `llm-agent` `ai` `ai-agents` |
| 🕒 **Last activity** | 2026-10-18 (24d ago) |
| 📅 **Created** | 2023-10-11 |
| 📦 **Latest release** | [0.16.8](https://github.com/letta-ai/letta/releases/tag/0.16.8) — 2026-05-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 286.8 MB |
| 🌐 **Website** | https://docs.letta.com/ |

## 📦 Recent releases

### [0.16.8](https://github.com/letta-ai/letta/releases/tag/0.16.8) — v0.16.8
<sub>2026-05-14 · 6mo ago</sub>

> **What's Changed**
> * fix: workflows update by @cpacker in https://github.com/letta-ai/letta/pull/3292
> * fix(security): use JSON instead of pickle for sandbox->server tool result transport by @kianjones9 in https://github.com/letta-ai/letta/pull/3343
> **Full Changelog**: https://github.com/letta-ai/letta/compare/0.16.7...0.16.8

### [0.16.7](https://github.com/letta-ai/letta/releases/tag/0.16.7) — v0.16.7
<sub>2026-03-31 · 7mo ago</sub>

> **Letta Server 0.16.7 Release Notes**
> **173 commits since 0.16.6** | Released March 31, 2026
> **Highlights**
> **Self-hosted users: this is a big upgrade.** The default global context window is raised from 32k to 128k, the context window reset bug (LET-7991) is fixed, and compaction has been overhauled. If you've been running curl commands to patch your config after every ADE load, most of that pain should be gone.
> **Breaking Changes**
> - **Block limits are no longer enforced** -- block limit validation has been deprecated and removed from the git memory sync path (#9977, #9983). Blocks can now grow freely. If you were relying on limits to cap per-turn cost, you'll need to manage block size via other means.
> …

### [0.16.6](https://github.com/letta-ai/letta/releases/tag/0.16.6) — v0.16.6
<sub>2026-03-04 · 8mo ago</sub>

> **Highlights**
> - Expanded Conversations API support for **default conversation / agent-direct mode**.
> - New conversations now initialize with a **compiled system message at creation time**.
> - Fixed `model_settings.max_output_tokens` default behavior so it **does not silently override** existing `max_tokens` unless explicitly set.
> **Conversations API updates**
> - Added support for `conversation_id="default"` + `agent_id` across conversation endpoints (send/list/cancel/compact/stream retrieve).
> …

### [0.16.5](https://github.com/letta-ai/letta/releases/tag/0.16.5) — v0.16.5
<sub>2026-02-24 · 8mo ago</sub>

> **What's Changed**
> * chore: bump version 0.16.5 by @carenthomas in https://github.com/letta-ai/letta/pull/3202
> **Full Changelog**: https://github.com/letta-ai/letta/compare/0.16.4...0.16.5

### [0.16.4](https://github.com/letta-ai/letta/releases/tag/0.16.4) — v0.16.4
<sub>2026-01-29 · 9mo ago</sub>

> **What's Changed**
> * fix: update gh templates by @cpacker in https://github.com/letta-ai/letta/pull/3155
> * chore: release 0.16.3  by @sarahwooders in https://github.com/letta-ai/letta/pull/3158
> * chore: bump v0.16.4 by @carenthomas in https://github.com/letta-ai/letta/pull/3168
> **Full Changelog**: https://github.com/letta-ai/letta/compare/0.16.2...0.16.4

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-18 | [docs: remove desktop app mention from README (#3454)](https://github.com/letta-ai/letta/commit/8816d3a8516893bfdc0fa14bfb1235226012e295) | sarahwooders |
| 2026-10-18 | [docs: remove desktop app mention from README](https://github.com/letta-ai/letta/commit/60703a7784caeb69daee9963b5b47a8bf8a0f3d9) | letta-integration[bot] |
| 2026-09-10 | [docs: limit security reports to maintained projects (#3442)](https://github.com/letta-ai/letta/commit/5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a) | cpacker |
| 2026-09-10 | [fix: update privacy policy contact address (#3441)](https://github.com/letta-ai/letta/commit/e0d746e5e78702f8abe71f32791233dab360c1bf) | letta-integration[bot] |
| 2026-08-23 | [chore: restore issue spam guard (#3433)](https://github.com/letta-ai/letta/commit/4511fa0bc91f68fbab32b91f694617271ea9012b) | letta-integration[bot] |
| 2026-08-16 | [chore: archive the legacy server repository (#3430)](https://github.com/letta-ai/letta/commit/87fd37aab68c7bdd0d66fe63751553756f6af3e5) | letta-integration[bot] |
| 2026-08-14 | [chore: deter self-promotional issue spam (#3429)](https://github.com/letta-ai/letta/commit/56ba9c25552605eec89de8ed3dc6394b625c1993) | letta-integration[bot] |
| 2026-08-01 | [fix: require explicit AI tool disclosure in issues (#3421)](https://github.com/letta-ai/letta/commit/ff19ffeafeb54bd2a7dc5d4a552f10191732a235) | cpacker |
| 2026-07-30 | [Update AI_POLICY.md (#3418)](https://github.com/letta-ai/letta/commit/5beb66e9981da4802de05c90bf43fba18053d5d6) | cpacker |
| 2026-07-03 | [docs: update README to Letta Agent SDK, add AGENTS.md deprecation not…](https://github.com/letta-ai/letta/commit/b76da9092518cbaa2d09042e52fdcbde69243e18) | cpacker |

[See all commits ↗](https://github.com/letta-ai/letta/commits)

## ⬇️ Get it

```bash
git clone https://github.com/letta-ai/letta.git
```
