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
| ⭐ **Stars** | 81.0k |
| 🍴 **Forks** | 6.4k |
| 🐞 **Open issues + PRs** | [337](https://github.com/headroomlabs-ai/headroom/issues) |
| 💻 **Languages** | Python 81% · Rust 12% · JavaScript 3% · TypeScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `ai` `anthropic` `compression` `context-engineering` `context-window` `fastapi` `langchain` `llm` `mcp` `openai` `proxy` `python` `rag` `token-optimization` `claude-code` `cursor` `prompt-engineering` `tokens` `typescript` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-01-07 |
| 📦 **Latest release** | [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 106.6 MB |
| 🌐 **Website** | https://docs.headroomlabs.ai/docs |

## 📦 Recent releases

### [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — Release v0.45.0
<sub>2026-11-22 · 5d ago</sub>

> **[0.45.0](https://github.com/headroomlabs-ai/headroom/compare/v0.44.0...v0.45.0) (2026-11-22)**
> **Features**
> * **opencode:** add repeatable --extra-model flag for custom wrap-time models ([#2364](https://github.com/headroomlabs-ai/headroom/issues/2364)) ([66e0086](https://github.com/headroomlabs-ai/headroom/commit/66e0086952d4b311c9fe9b489fbd12d1d270fcde))
> * **savings:** book modelled output savings per request, as a token and dollar range ([#4878](https://github.com/headroomlabs-ai/headroom/issues/4878)) ([00436a8](https://github.com/headroomlabs-ai/headroom/commit/00436a8b11b69f19e280ba0ce3f54f50094e4a5e))
> * **shaper:** let an extension replace a level's steering text; default to L3 ([#4877](https://github.com/headroomlabs-ai/headroom/issues/4877)) ([a3afd43](https://github.com/headroomlabs-ai/headroom/commit/a3afd43e0cbd3ed4b2186419bcc8ac447d110e39))
> * **telemetry:** split beacon sessions by harness, model and day ([#4881](https://github.com/headroomlabs-ai/headroom/issues/4881)) ([ac932eb](https://github.com/headroomlabs-ai/headroom/commit/ac932eb7c43156e94088d21e6c1edf3dc14b233b))
> …

### [v0.44.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.44.0) — Release v0.44.0
<sub>2026-11-10 · 17d ago</sub>

> **[0.44.0](https://github.com/headroomlabs-ai/headroom/compare/v0.43.1...v0.44.0) (2026-11-09)**
> **⚠ BREAKING CHANGES**
> * **packaging:** keep PyTorch extras out of all ([#4067](https://github.com/headroomlabs-ai/headroom/issues/4067))
> **Features**
> * **pipeline:** say whose request an OutcomeSnapshot is ([#4698](https://github.com/headroomlabs-ai/headroom/issues/4698)) ([a2bcbd1](https://github.com/headroomlabs-ai/headroom/commit/a2bcbd101b1391debfd218ec8c63cb72d2bc240a))
> * **providers:** add Hermes agent wrap support ([#934](https://github.com/headroomlabs-ai/headroom/issues/934)) ([7877241](https://github.com/headroomlabs-ai/headroom/commit/7877241d84c93b3ec487e07324245838ddae85cc))
> …

### [v0.43.1](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.1) — Release v0.43.1
<sub>2026-11-05 · 21d ago</sub>

> **[0.43.1](https://github.com/headroomlabs-ai/headroom/compare/v0.43.0...v0.43.1) (2026-11-05)**
> **Bug Fixes**
> * **ccr:** keep the in-memory order queue from evicting re-stored entries ([#4545](https://github.com/headroomlabs-ai/headroom/issues/4545)) ([c6f5bf9](https://github.com/headroomlabs-ai/headroom/commit/c6f5bf9549e9b357e9c2369d4e04bc437f5e180d))
> * **memory:** read the relation key the memory_save schema advertises ([#4647](https://github.com/headroomlabs-ai/headroom/issues/4647)) ([7592e68](https://github.com/headroomlabs-ai/headroom/commit/7592e681459f14a2041eb5f524a658cb6ad1dd92))
> * **memory:** replace the HNSW vector when a memory is re-indexed ([#4649](https://github.com/headroomlabs-ai/headroom/issues/4649)) ([ee638f9](https://github.com/headroomlabs-ai/headroom/commit/ee638f9532b3788bacd13ed8d26dd0faf0740baf))
> * **openclaw:** accept 12-character hashes in headroom_retrieve ([#4640](https://github.com/headroomlabs-ai/headroom/issues/4640)) ([8d3e9e5](https://github.com/headroomlabs-ai/headroom/commit/8d3e9e5ca7cd645eb73084b848edbea5fc796e1a))
> …

### [v0.43.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.0) — Release v0.43.0
<sub>2026-11-05 · 21d ago</sub>

> **[0.43.0](https://github.com/headroomlabs-ai/headroom/compare/v0.42.0...v0.43.0) (2026-11-05)**
> **⚠ BREAKING CHANGES**
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603))
> **Features**
> * **ccr:** answer headroom_retrieve on streaming chat completions ([#4631](https://github.com/headroomlabs-ai/headroom/issues/4631)) ([31dcaf4](https://github.com/headroomlabs-ai/headroom/commit/31dcaf41f7fafaebec0838a05ff328da456faef0))
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603)) ([ee2252a](https://github.com/headroomlabs-ai/headroom/commit/ee2252a3155c87e948c8893b79af5824eb30e64c))
> …

### [v0.42.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.42.0) — Release v0.42.0
<sub>2026-10-26 · 1mo ago</sub>

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
| 2026-11-26 | [fix(bedrock): answer model discovery from Bedrock and map undated mod…](https://github.com/headroomlabs-ai/headroom/commit/6a50f22cb38df8a57ff628db6540a54932bb786e) | chopratejas |
| 2026-11-26 | [fix(memory): preserve YAML string metadata in agent files (#5046)](https://github.com/headroomlabs-ai/headroom/commit/c9d7eae7e6254ff9864f1c1bd505ae1e37adca31) | stefanielizeth73-art |
| 2026-11-26 | [fix(sdk): preserve compact server-sent event data fields (#5009)](https://github.com/headroomlabs-ai/headroom/commit/5d3f8560e9fa97ecd81814b0d014fd22b239ed08) | DivyamTalwar |
| 2026-11-26 | [fix(asgi): update content length after request compression (#5007)](https://github.com/headroomlabs-ai/headroom/commit/b9cf195acbcb30473699a206c8fed959531acedd) | DivyamTalwar |
| 2026-11-26 | [fix(learn): read list tool results as their text (#4969)](https://github.com/headroomlabs-ai/headroom/commit/747e499bd4758bcb7f892cf7dccf51ae79d425a4) | chuenchen309 |
| 2026-11-26 | [fix(learn): pair parallel Gemini calls to the same tool with their ow…](https://github.com/headroomlabs-ai/headroom/commit/0fbe8e87a085497e6d108169edf3cb6df7ba7036) | nurlanmnn |
| 2026-11-26 | [fix(security): pin HuggingFace model revisions in from_pretrained / h…](https://github.com/headroomlabs-ai/headroom/commit/4571390681b1763a390166d607a7fb7a1a735d24) | Parideboy |
| 2026-11-25 | [fix(rust): emit a function-body row shared by two statements once (#4…](https://github.com/headroomlabs-ai/headroom/commit/98ba445ddd7e1cfd021f443eb96e3b8550a17443) | divya0795 |
| 2026-11-25 | [fix(proxy): forward Gemini batch polls to /v1beta/batches/<id> instea…](https://github.com/headroomlabs-ai/headroom/commit/de9915f2487829e933d1c6d4fb5a7beae1a6d8a5) | coder-abu |
| 2026-11-25 | [fix(ccr): count per-result continuation rounds in batch results (#5043)](https://github.com/headroomlabs-ai/headroom/commit/d2014cb948d27bd9d411b147a6d203363f70b912) | 123XieC |

[See all commits ↗](https://github.com/headroomlabs-ai/headroom/commits)

## ⬇️ Get it

```bash
git clone https://github.com/headroomlabs-ai/headroom.git
```
