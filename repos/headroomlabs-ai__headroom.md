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
| ⭐ **Stars** | 80.8k |
| 🍴 **Forks** | 6.3k |
| 🐞 **Open issues + PRs** | [334](https://github.com/headroomlabs-ai/headroom/issues) |
| 💻 **Languages** | Python 81% · Rust 12% · JavaScript 3% · TypeScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `ai` `anthropic` `compression` `context-engineering` `context-window` `fastapi` `langchain` `llm` `mcp` `openai` `proxy` `python` `rag` `token-optimization` `claude-code` `cursor` `prompt-engineering` `tokens` `typescript` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-01-07 |
| 📦 **Latest release** | [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 106.5 MB |
| 🌐 **Website** | https://docs.headroomlabs.ai/docs |

## 📦 Recent releases

### [v0.45.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.45.0) — Release v0.45.0
<sub>2026-11-22 · 3d ago</sub>

> **[0.45.0](https://github.com/headroomlabs-ai/headroom/compare/v0.44.0...v0.45.0) (2026-11-22)**
> **Features**
> * **opencode:** add repeatable --extra-model flag for custom wrap-time models ([#2364](https://github.com/headroomlabs-ai/headroom/issues/2364)) ([66e0086](https://github.com/headroomlabs-ai/headroom/commit/66e0086952d4b311c9fe9b489fbd12d1d270fcde))
> * **savings:** book modelled output savings per request, as a token and dollar range ([#4878](https://github.com/headroomlabs-ai/headroom/issues/4878)) ([00436a8](https://github.com/headroomlabs-ai/headroom/commit/00436a8b11b69f19e280ba0ce3f54f50094e4a5e))
> * **shaper:** let an extension replace a level's steering text; default to L3 ([#4877](https://github.com/headroomlabs-ai/headroom/issues/4877)) ([a3afd43](https://github.com/headroomlabs-ai/headroom/commit/a3afd43e0cbd3ed4b2186419bcc8ac447d110e39))
> * **telemetry:** split beacon sessions by harness, model and day ([#4881](https://github.com/headroomlabs-ai/headroom/issues/4881)) ([ac932eb](https://github.com/headroomlabs-ai/headroom/commit/ac932eb7c43156e94088d21e6c1edf3dc14b233b))
> …

### [v0.44.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.44.0) — Release v0.44.0
<sub>2026-11-10 · 15d ago</sub>

> **[0.44.0](https://github.com/headroomlabs-ai/headroom/compare/v0.43.1...v0.44.0) (2026-11-09)**
> **⚠ BREAKING CHANGES**
> * **packaging:** keep PyTorch extras out of all ([#4067](https://github.com/headroomlabs-ai/headroom/issues/4067))
> **Features**
> * **pipeline:** say whose request an OutcomeSnapshot is ([#4698](https://github.com/headroomlabs-ai/headroom/issues/4698)) ([a2bcbd1](https://github.com/headroomlabs-ai/headroom/commit/a2bcbd101b1391debfd218ec8c63cb72d2bc240a))
> * **providers:** add Hermes agent wrap support ([#934](https://github.com/headroomlabs-ai/headroom/issues/934)) ([7877241](https://github.com/headroomlabs-ai/headroom/commit/7877241d84c93b3ec487e07324245838ddae85cc))
> …

### [v0.43.1](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.1) — Release v0.43.1
<sub>2026-11-05 · 19d ago</sub>

> **[0.43.1](https://github.com/headroomlabs-ai/headroom/compare/v0.43.0...v0.43.1) (2026-11-05)**
> **Bug Fixes**
> * **ccr:** keep the in-memory order queue from evicting re-stored entries ([#4545](https://github.com/headroomlabs-ai/headroom/issues/4545)) ([c6f5bf9](https://github.com/headroomlabs-ai/headroom/commit/c6f5bf9549e9b357e9c2369d4e04bc437f5e180d))
> * **memory:** read the relation key the memory_save schema advertises ([#4647](https://github.com/headroomlabs-ai/headroom/issues/4647)) ([7592e68](https://github.com/headroomlabs-ai/headroom/commit/7592e681459f14a2041eb5f524a658cb6ad1dd92))
> * **memory:** replace the HNSW vector when a memory is re-indexed ([#4649](https://github.com/headroomlabs-ai/headroom/issues/4649)) ([ee638f9](https://github.com/headroomlabs-ai/headroom/commit/ee638f9532b3788bacd13ed8d26dd0faf0740baf))
> * **openclaw:** accept 12-character hashes in headroom_retrieve ([#4640](https://github.com/headroomlabs-ai/headroom/issues/4640)) ([8d3e9e5](https://github.com/headroomlabs-ai/headroom/commit/8d3e9e5ca7cd645eb73084b848edbea5fc796e1a))
> …

### [v0.43.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.43.0) — Release v0.43.0
<sub>2026-11-05 · 19d ago</sub>

> **[0.43.0](https://github.com/headroomlabs-ai/headroom/compare/v0.42.0...v0.43.0) (2026-11-05)**
> **⚠ BREAKING CHANGES**
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603))
> **Features**
> * **ccr:** answer headroom_retrieve on streaming chat completions ([#4631](https://github.com/headroomlabs-ai/headroom/issues/4631)) ([31dcaf4](https://github.com/headroomlabs-ai/headroom/commit/31dcaf41f7fafaebec0838a05ff328da456faef0))
> * **mcp:** port MCP servers to SDK 2.x ([#4603](https://github.com/headroomlabs-ai/headroom/issues/4603)) ([ee2252a](https://github.com/headroomlabs-ai/headroom/commit/ee2252a3155c87e948c8893b79af5824eb30e64c))
> …

### [v0.42.0](https://github.com/headroomlabs-ai/headroom/releases/tag/v0.42.0) — Release v0.42.0
<sub>2026-10-26 · 29d ago</sub>

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
| 2026-11-25 | [feat(release): define versioned policy contracts (#3637)](https://github.com/headroomlabs-ai/headroom/commit/234c233cc439aedba53b242f02f695de5f90c877) | JerrettDavis |
| 2026-11-24 | [fix(savings): don't double-charge inferred cache writes in lifetime i…](https://github.com/headroomlabs-ai/headroom/commit/df4477f2753afc65528d2560429a62d33a730d26) | Totopo27 |
| 2026-11-24 | [fix(proxy): log peer close codes for Responses WebSockets (#4978)](https://github.com/headroomlabs-ai/headroom/commit/c489b5f8fe57b42b17f810ef5e9e65ede298947c) | emme1t |
| 2026-11-24 | [fix(code-compressor): don't blame the compressor or trip the breaker …](https://github.com/headroomlabs-ai/headroom/commit/d2d4e0e6f37ee06fb9609e4d663bc773e046dfa7) | KennethWKZ |
| 2026-11-24 | [fix(content-router): treat unparseable JSON as nothing to minify afte…](https://github.com/headroomlabs-ai/headroom/commit/8eedfc686baf0bcb37d278ba62324ac8ad93ab30) | KennethWKZ |
| 2026-11-24 | [fix(tool-search): treat Claude Code's ToolSearch as the resolver for …](https://github.com/headroomlabs-ai/headroom/commit/2c17627e03a67945b35d11eb2a5289276646d889) | KennethWKZ |
| 2026-11-24 | [fix(proxy): bucket invalid model keys into "other" in requests_by_mod…](https://github.com/headroomlabs-ai/headroom/commit/ae9d45875b418eec51b8d8e024265b03ad710ead) | PCTEJA |
| 2026-11-24 | [fix(proxy): skip a leading UTF-8 BOM when reconstructing closed SSE (…](https://github.com/headroomlabs-ai/headroom/commit/f21327105ae8843828b5733fb25f1179a0a3ca37) | Mystery01092000 |
| 2026-11-24 | [deps: Bump the cargo-minor-patch group across 1 directory with 10 upd…](https://github.com/headroomlabs-ai/headroom/commit/8c206ddf53c89424a84ad5e308d87c9d769e6aef) | dependabot[bot] |
| 2026-11-24 | [test(proxy): require no allow-origin header for rejected CORS origins…](https://github.com/headroomlabs-ai/headroom/commit/87b56ce1fb6de5fa1520ffb7d093b4de13498854) | chopratejas |

[See all commits ↗](https://github.com/headroomlabs-ai/headroom/commits)

## ⬇️ Get it

```bash
git clone https://github.com/headroomlabs-ai/headroom.git
```
