# headroomlabs-ai/headroom

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/headroomlabs-ai/headroom)

> Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | TCOS |
| **Why it's worth a look** | Compress tool outputs, logs and RAG chunks before they hit the LLM |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 80.4k |
| 🍴 **Forks** | 6.3k |
| 🐞 **Open issues + PRs** | [327](https://github.com/headroomlabs-ai/headroom/issues) |
| 💻 **Languages** | Python 81% · Rust 12% · JavaScript 3% · TypeScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `ai` `anthropic` `compression` `context-engineering` `context-window` `fastapi` `langchain` `llm` `mcp` `openai` `proxy` `python` `rag` `token-optimization` `claude-code` `cursor` `prompt-engineering` `tokens` `typescript` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-01-07 |
| 📦 **Latest release** | [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 105.0 MB |
| 🌐 **Website** | https://docs.headroomlabs.ai/docs |

## 📦 Recent releases

### [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — Release v0.45.0
<sub>2026-11-22 · today</sub>

> **[0.45.0](https://github.com/headroomlabs-ai/headroom/compare/v0.44.0...v0.45.0) (2026-11-22)**
> **Features**
> * **opencode:** add repeatable --extra-model flag for custom wrap-time models ([#2364](https://github.com/headroomlabs-ai/headroom/issues/2364)) ([66e0086](https://github.com/headroomlabs-ai/headroom/commit/66e0086952d4b311c9fe9b489fbd12d1d270fcde))
> * **savings:** book modelled output savings per request, as a token and dollar range ([#4878](https://github.com/headroomlabs-ai/headroom/issues/4878)) ([00436a8](https://github.com/headroomlabs-ai/headroom/commit/00436a8b11b69f19e280ba0ce3f54f50094e4a5e))
> * **shaper:** let an extension replace a level's steering text; default to L3 ([#4877](https://github.com/headroomlabs-ai/headroom/issues/4877)) ([a3afd43](https://github.com/headroomlabs-ai/headroom/commit/a3afd43e0cbd3ed4b2186419bcc8ac447d110e39))
> * **telemetry:** split beacon sessions by harness, model and day ([#4881](https://github.com/headroomlabs-ai/headroom/issues/4881)) ([ac932eb](https://github.com/headroomlabs-ai/headroom/commit/ac932eb7c43156e94088d21e6c1edf3dc14b233b))
> …

### [v0.44.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.44.0) — Release v0.44.0
<sub>2026-11-10 · 12d ago</sub>

> **[0.44.0](https://github.com/headroomlabs-ai/headroom/compare/v0.43.1...v0.44.0) (2026-11-09)**
> **⚠ BREAKING CHANGES**
> * **packaging:** keep PyTorch extras out of all ([#4067](https://github.com/headroomlabs-ai/headroom/issues/4067))
> **Features**
> * **pipeline:** say whose request an OutcomeSnapshot is ([#4698](https://github.com/headroomlabs-ai/headroom/issues/4698)) ([a2bcbd1](https://github.com/headroomlabs-ai/headroom/commit/a2bcbd101b1391debfd218ec8c63cb72d2bc240a))
> * **providers:** add Hermes agent wrap support ([#934](https://github.com/headroomlabs-ai/headroom/issues/934)) ([7877241](https://github.com/headroomlabs-ai/headroom/commit/7877241d84c93b3ec487e07324245838ddae85cc))
> …

### [v0.43.1](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.1) — Release v0.43.1
<sub>2026-11-05 · 16d ago</sub>

> **[0.43.1](https://github.com/headroomlabs-ai/headroom/compare/v0.43.0...v0.43.1) (2026-11-05)**
> **Bug Fixes**
> * **ccr:** keep the in-memory order queue from evicting re-stored entries ([#4545](https://github.com/headroomlabs-ai/headroom/issues/4545)) ([c6f5bf9](https://github.com/headroomlabs-ai/headroom/commit/c6f5bf9549e9b357e9c2369d4e04bc437f5e180d))
> * **memory:** read the relation key the memory_save schema advertises ([#4647](https://github.com/headroomlabs-ai/headroom/issues/4647)) ([7592e68](https://github.com/headroomlabs-ai/headroom/commit/7592e681459f14a2041eb5f524a658cb6ad1dd92))
> * **memory:** replace the HNSW vector when a memory is re-indexed ([#4649](https://github.com/headroomlabs-ai/headroom/issues/4649)) ([ee638f9](https://github.com/headroomlabs-ai/headroom/commit/ee638f9532b3788bacd13ed8d26dd0faf0740baf))
> * **openclaw:** accept 12-character hashes in headroom_retrieve ([#4640](https://github.com/headroomlabs-ai/headroom/issues/4640)) ([8d3e9e5](https://github.com/headroomlabs-ai/headroom/commit/8d3e9e5ca7cd645eb73084b848edbea5fc796e1a))
> …

### [v0.43.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.0) — Release v0.43.0
<sub>2026-11-05 · 16d ago</sub>

> **[0.43.0](https://github.com/headroomlabs-ai/headroom/compare/v0.42.0...v0.43.0) (2026-11-05)**
> **⚠ BREAKING CHANGES**
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603))
> **Features**
> * **ccr:** answer headroom_retrieve on streaming chat completions ([#4631](https://github.com/headroomlabs-ai/headroom/issues/4631)) ([31dcaf4](https://github.com/headroomlabs-ai/headroom/commit/31dcaf41f7fafaebec0838a05ff328da456faef0))
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603)) ([ee2252a](https://github.com/headroomlabs-ai/headroom/commit/ee2252a3155c87e948c8893b79af5824eb30e64c))
> …

### [v0.42.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.42.0) — Release v0.42.0
<sub>2026-10-26 · 26d ago</sub>

> **[0.42.0](https://github.com/headroomlabs-ai/headroom/compare/v0.41.0...v0.42.0) (2026-10-26)**
> **Features**
> * **pipeline:** put per-request saved tokens on OutcomeSnapshot ([#4231](https://github.com/headroomlabs-ai/headroom/issues/4231)) ([8cedf7b](https://github.com/headroomlabs-ai/headroom/commit/8cedf7be4decfb3a0da42e4e955b6a3301a66dc9))
> * **proxy:** let turn hooks rewrite OpenAI Responses requests on HTTP and WebSocket ([#4232](https://github.com/headroomlabs-ai/headroom/issues/4232)) ([fbf7bc3](https://github.com/headroomlabs-ai/headroom/commit/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05))
> * **proxy:** report the same tool savings on gateway /v1/compress as the proxy path ([#4467](https://github.com/headroomlabs-ai/headroom/issues/4467)) ([a904210](https://github.com/headroomlabs-ai/headroom/commit/a90421083a781990b877d34fdaba0bc1b6cf6c4d))
> * **savings:** add the per-request counterfactual savings record ([#4236](https://github.com/headroomlabs-ai/headroom/issues/4236)) ([2912b7b](https://github.com/headroomlabs-ai/headroom/commit/2912b7b620d7abd39828db73e4f326b9a041d309))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [chore: release 0.45.0 (#4724)](https://github.com/headroomlabs-ai/headroom/commit/ce0460cfa8598dc939243dbc7aec4b2d35f4e44a) | headroom-release[bot] |
| 2026-11-22 | [ci(security): verify the gitleaks download against its release checks…](https://github.com/headroomlabs-ai/headroom/commit/6608cf702ee040f8d71ebc778abba85bd327af6b) | chopratejas |
| 2026-11-22 | [fix(ci): keep alert rule and location out of the public CodeQL triage…](https://github.com/headroomlabs-ai/headroom/commit/047aadde868d38e27b5d6bc2d99dd21362fa0d53) | chopratejas |
| 2026-11-22 | [fix(proxy): keep settings.json mode and symlink in the cc-switch reco…](https://github.com/headroomlabs-ai/headroom/commit/3bae009c3fd9c2a730b98830e642ecb312878002) | chopratejas |
| 2026-11-22 | [fix(plugins): keep the hook launcher's Python fallback off the projec…](https://github.com/headroomlabs-ai/headroom/commit/c5d8f133606ffadbf4be8731dc1fed77e471f64f) | chopratejas |
| 2026-11-22 | [fix(memory): keep Neo4j relationship types to a single identifier (#4…](https://github.com/headroomlabs-ai/headroom/commit/b0a8c000caade71df451b4c1976fe402e12a2a6a) | chopratejas |
| 2026-11-22 | [feat(shaper): let an extension replace a level's steering text; defau…](https://github.com/headroomlabs-ai/headroom/commit/a3afd43e0cbd3ed4b2186419bcc8ac447d110e39) | chopratejas |
| 2026-11-20 | [fix(cache): preserve complete CCR hashes across restarts (#4820)](https://github.com/headroomlabs-ai/headroom/commit/e27f0d96cc3032d5f2c510ac97545553b867a697) | stefanielizeth73-art |
| 2026-11-20 | [fix(lossless): never grep-fold Ruby Logger timestamps (#4907)](https://github.com/headroomlabs-ai/headroom/commit/4a945007817022c9f797d811f475dc1172522b97) | Ayushraj06-bit |
| 2026-11-20 | [test(memory): skip HNSW tests when the hnswlib probe fails (#4911)](https://github.com/headroomlabs-ai/headroom/commit/f4c2974e11b64a78f886caca6cdcde28d406f835) | Parideboy |

[See all commits ↗](https://github.com/headroomlabs-ai/headroom/commits)

## ⬇️ Get it

```bash
git clone https://github.com/headroomlabs-ai/headroom.git
```
