# janhq/jan

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/janhq/jan)

> Jan is an open source alternative to ChatGPT that runs 100% offline on your computer.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Offline ChatGPT alternative that runs 100% on your computer |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 46.1k |
| 🍴 **Forks** | 3.3k |
| 🐞 **Open issues + PRs** | [594](https://github.com/janhq/jan/issues) |
| 💻 **Languages** | Rust 57% · TypeScript 40% · Python 1% · JavaScript 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `llamacpp` `localai` `self-hosted` `gpt` `tauri` `chatgpt` `llm` `open-source` |
| 🕒 **Last activity** | 2026-11-23 (2d ago) |
| 📅 **Created** | 2023-08-17 |
| 📦 **Latest release** | [v0.8.8](https://github.com/janhq/jan/releases/tag/v0.8.8) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1546.1 MB |
| 🌐 **Website** | https://jan.ai/ |

## 📦 Recent releases

### [v0.8.8](https://github.com/janhq/jan/releases/tag/v0.8.8) — 0.8.8
<sub>2026-10-28 · 28d ago</sub>

> **Jan v0.8.8: security fixes, llama.cpp 0.7.0, and Trusted Hosts for the local API**
> A security update to v0.8.7. We recommend updating. Your data and settings carry over; a few behaviours change, listed under **What you might notice**.
> **Security**
> - **Links in chat open in your browser.** Links in model replies, tool results, model cards and release notes now always open in your system browser, never inside Jan's window. Links that aren't web or email links are shown as plain text.
> - **The local API server checks where browser requests come from.** A web page can only call it if its origin is trusted: the same machine, Jan itself, or a host you list in **Trusted Hosts**. Requests without a browser origin (SDKs, scripts, curl, Claude Code) work as before.
> - **Server-side tool execution stays opt-in for every endpoint.** Requests to the local API run MCP tools only when **Settings > Local API Server** allows server-side tool execution.
> …

### [v0.8.7](https://github.com/janhq/jan/releases/tag/v0.8.7) — 0.8.7
<sub>2026-10-20 · 1mo ago</sub>

> **Jan v0.8.7: shell switch, image size limit, and fixes**
> A minor update to v0.8.6. Your data and settings carry over; one MCP clean-up runs on first launch (below).
> **New**
> - **Turn the shell tool off in chat.** The chat input's tool menu has a **Shell** switch. Off, the model is not given the shell tool; web search, fetch and your MCP tools keep working. On by default, and shown when the shell can run sandboxed and the model supports tools ([#9222](https://github.com/janhq/jan/issues/9222)).
> - **A separate size limit for images.** **Settings > Attachments > Max Image Size (MB)**: default 10, range 1 to 100 ([#9312](https://github.com/janhq/jan/pull/9312)).
> - **Built-in subagents for the Jan agent**: explore (read-only by default), research, review and debug, each with its own model ([#9261](https://github.com/janhq/jan/pull/9261)).
> …

### [v0.8.6](https://github.com/janhq/jan/releases/tag/v0.8.6) — 0.8.6
<sub>2026-10-09 · 1mo ago</sub>

> **Jan v0.8.6: hotfix for v0.8.5**
> Fixes only. If you're on 0.8.5, updating is recommended, especially on Linux (AppImage) and on older NVIDIA GPUs.
> **Fixes**
> - **Linux AppImage crashed on every model load on some distributions** ([#9173](https://github.com/janhq/jan/issues/9173), fixed in [#9178](https://github.com/janhq/jan/pull/9178)). The AppImage bundled the build machine's Vulkan loader. It now uses your system's loader, and the build fails if a GPU loader is ever bundled again.
> - **NVIDIA Turing GPUs (GTX 16xx, RTX 20xx) failed with "the provided PTX was compiled with an unsupported toolchain"** ([#9185](https://github.com/janhq/jan/issues/9185), fixed in [#9187](https://github.com/janhq/jan/pull/9187)). On drivers older than R595, the Windows and Linux CUDA engine could not run on these cards. It now ships native Turing code, as 0.8.4 did, so no driver update is needed.
> - **Qwen3.8 with MTP (speculative decoding) slowed down sharply after updating to 0.8.5** ([#9183](https://github.com/janhq/jan/issues/9183), fixed in [#9186](https://github.com/janhq/jan/pull/9186)). With Parallel Sequences on auto, the engine reserved memory for 4 slots. On cards with 12 GB or similar, that pushed the model into shared system memory. A model with MTP now uses one slot when Parallel Sequences is auto; a value you set yourself is respected.
> …

### [v0.8.5](https://github.com/janhq/jan/releases/tag/v0.8.5) — 0.8.5
<sub>2026-10-08 · 1mo ago</sub>

> **This release is fixes only**
> No new features are announced in v0.8.5. Work in progress stays in the nightly channel: [Cowork](https://jan.ai/docs/desktop/cowork) and the current agent work ship there until they are announced, and a stable build does not show them.
> One thing a first launch will notice: the first-run setup is now a guided wizard - welcome, engine setup, a first model, and the consent page - instead of opening straight into the chat with no engine or model set up. It is onboarding rather than a new capability, so it is not a headline; it is written down here so a new install is not a surprise.
> ---
> **Migration**
> **The llama.cpp engine now ships with the app.**
> …

### [v0.8.4](https://github.com/janhq/jan/releases/tag/v0.8.4) — 0.8.4
<sub>2026-07-23 · 4mo ago</sub>

> **Migration**
> **Settings and credentials now live in a backend-managed store.**
> Provider settings and credentials previously persisted in the webview's `localStorage`. In 0.8.4, Jan reads and writes them from a backend-managed store instead (secrets go to the OS keyring). Your existing settings and API keys are copied over automatically on first launch - no manual action is needed, and from this version on all new changes are saved to the backend store.
> Your old `localStorage` data is **not deleted** - it's kept as a snapshot so you can downgrade to a pre-0.8.4 build and still have your previous settings. Any changes you make in 0.8.4+ live only in the backend store, so a downgrade sees the older snapshot, not your latest settings.
> ---
> **What's Changed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [feat(app): desktop notifications for finished, failed and approval-ne…](https://github.com/janhq/jan/commit/49a84bdeaebdfc0f36c00f252eb638f516a48432) | qnixsynapse |
| 2026-11-16 | [feat(llamacpp): upgrade the engine to 1.0.0 (b12359) (#9699)](https://github.com/janhq/jan/commit/da44e320f2132b6fa91879f3b723200fe281c1cb) | qnixsynapse |
| 2026-11-16 | [Merge pull request #9700 from janhq/ci/lock-github-actions](https://github.com/janhq/jan/commit/b6d88f6918bf5dd1c06dfd45699402510ab8738f) | Minh141120 |
| 2026-11-16 | [ci: lock actions used by local composite actions](https://github.com/janhq/jan/commit/e0ec02ca0658418dd31a5f166ff18e22b5c81ee9) | Minh141120 |
| 2026-11-16 | [ci: lock GitHub Actions dependencies](https://github.com/janhq/jan/commit/e419635ee190ae928c35a56814c9802c09393aeb) | Minh141120 |
| 2026-11-16 | [feat(app): close-to-tray setting for Windows and Linux (#9666) (#9670)](https://github.com/janhq/jan/commit/6a1214c2bc0f25564c85a5accce84229ed681648) | thinhlpg |
| 2026-11-16 | [fix(chat): send arguments for a tool call cut off before its input (#…](https://github.com/janhq/jan/commit/14f298709dbaf6f9107008fd74c5d5a3cc94111f) | b84330808 |
| 2026-11-16 | [fix(agent): truncate @directory listings at a UTF-8 boundary (#9690)](https://github.com/janhq/jan/commit/60cc8182fcdb074714f7b235917eb82933f898e0) | Celestial-0 |
| 2026-11-14 | [Merge pull request #9614 from youdotcom-oss/feat/websearch-youcom-key…](https://github.com/janhq/jan/commit/20a20960dece5d84c95d833f41f786c2d5c2f3f6) | qnixsynapse |
| 2026-11-12 | [Merge pull request #9644 from janhq/feat/llamacpp-load-mode](https://github.com/janhq/jan/commit/ea98bd3e0fe3dcf6374ec31f23045776d7471356) | qnixsynapse |

[See all commits ↗](https://github.com/janhq/jan/commits)

## ⬇️ Get it

```bash
git clone https://github.com/janhq/jan.git
```
