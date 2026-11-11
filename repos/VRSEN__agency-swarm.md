# VRSEN/agency-swarm

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/VRSEN/agency-swarm)

> Reliable Multi-Agent Orchestration Framework

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why I saved it** | Build an 'agency' of agents with roles, on OpenAI |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.6k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [9](https://github.com/VRSEN/agency-swarm/issues) |
| 💻 **Languages** | Python 97% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-02 (9d ago) |
| 📅 **Created** | 2023-11-16 |
| 📦 **Latest release** | [v1.11.0](https://github.com/VRSEN/agency-swarm/releases/tag/v1.11.0) — 2026-08-03 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 42.0 MB |
| 🌐 **Website** | https://agency-swarm.ai/ |

## 📦 Recent releases

### [v2.0.0-beta.1](https://github.com/VRSEN/agency-swarm/releases/tag/v2.0.0-beta.1) _(pre-release)_
<sub>2026-10-30 · 12d ago</sub>

> This release moves Agency Swarm onto the newest versions of its core libraries: the OpenAI Python SDK 3, MCP 2 and FastMCP 4. Long conversations now cost less, because OpenAI compacts them and later turns send only what comes after the compaction. The default model is now GPT-6 Luna.
> 2.0.0b1 is a pre-release, so `pip install --upgrade agency-swarm` still installs 1.11. To try it:
> ```bash
> pip install --pre "agency-swarm==2.0.0b1"
> ```
> Several changes need action when you upgrade. The [migration guide](https://agency-swarm.ai/migration/v2) lists each one with the code to change.
> …

### [v1.11.0](https://github.com/VRSEN/agency-swarm/releases/tag/v1.11.0)
<sub>2026-08-03 · 3mo ago</sub>

> This release adds realtime voice calls, per-user OAuth for MCP servers, and first-class system reminders. It also changes the default model, corrects usage-cost accounting, and fixes a token-isolation bug found by driving the OAuth flow end to end.
> **Voice agents**
> Run an existing agency as a realtime voice service. Use `run_realtime(agency=...)` for a dedicated server, add `/{agency}/realtime` to an existing app with `run_fastapi(enable_realtime=True)`, or call `Agency.to_realtime()` to build your own. Ships with OpenAI and xAI support, a packaged browser client, and a Twilio phone bridge ([#735](https://github.com/VRSEN/agency-swarm/pull/735)).
> **Limit worth knowing:** a call keeps one voice from start to finish. The realtime API refuses to change voices once the model has spoken, so the voice is chosen when the call starts and stays fixed even across handoffs. Set `voice=` on your entry agent, or pass it to `run_realtime()`.
> **OAuth for MCP servers**
> Connect OAuth-protected MCP servers with `MCPServerOAuth`. Sign-in is deferred until the agent calls `authenticate_mcp_server`, and tokens are stored in per-user buckets. FastAPI streams `oauth_redirect` and `oauth_status` events so a web client can drive the browser flow ([#734](https://github.com/VRSEN/agency-swarm/pull/734)).
> …

### [v1.10.5](https://github.com/VRSEN/agency-swarm/releases/tag/v1.10.5)
<sub>2026-07-17 · 3mo ago</sub>

> **What's Changed**
> * fix: keep runtime handoffs available across mid-run agent switches by @nicko-ai in https://github.com/VRSEN/agency-swarm/pull/727
> **Full Changelog**: https://github.com/VRSEN/agency-swarm/compare/v1.10.4...v1.10.5

### [v1.10.4](https://github.com/VRSEN/agency-swarm/releases/tag/v1.10.4)
<sub>2026-07-17 · 3mo ago</sub>

> **What's Changed**
> * fix(deps): constrain LiteLLM below 1.92 by @nicko-ai in https://github.com/VRSEN/agency-swarm/pull/726
> **Full Changelog**: https://github.com/VRSEN/agency-swarm/compare/v1.10.3...v1.10.4

### [v1.10.3](https://github.com/VRSEN/agency-swarm/releases/tag/v1.10.3)
<sub>2026-07-14 · 4mo ago</sub>

> Agency Swarm 1.10.3 prevents fresh installations from selecting an OpenAI release that is incompatible with the currently pinned Agents SDK. It also fixes invalid replay histories containing consecutive reasoning items.
> **What's Changed**
> **Reliability and compatibility**
> - Prevent fresh installs with `openai-agents==0.14.8` from resolving incompatible OpenAI 2.45+ versions in https://github.com/VRSEN/agency-swarm/pull/720.
> - Remove consecutive orphaned reasoning items transitively so invalid histories are not sent to the Responses API in https://github.com/VRSEN/agency-swarm/pull/707.
> - Expand supported datamodel-code-generator versions through 0.66.x in https://github.com/VRSEN/agency-swarm/pull/709.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-02 | [fix: stop uploading traces to OpenAI when OPENAI_BASE_URL points elsewhere (#857)](https://github.com/VRSEN/agency-swarm/commit/1bec92f0fc6e8485e53847c6f4a943a847058bff) | nicko-ai |
| 2026-10-30 | [release: v2.0.0-beta.1 (#855)](https://github.com/VRSEN/agency-swarm/commit/b28ac98321b21c9e052f915a76f74fc449f8e74a) | VRSEN |
| 2026-10-21 | [chore(deps-dev): bump fastapi from 0.141.1 to 0.143.3 (#845)](https://github.com/VRSEN/agency-swarm/commit/5b02d5f5bb1e47fd50c404398b36a07050f98001) | dependabot[bot] |
| 2026-10-21 | [chore(deps-dev): bump langchain-core from 1.6.9 to 1.6.12 (#844)](https://github.com/VRSEN/agency-swarm/commit/a17d18b177c687cdaa850ed26615175d0d60e679) | dependabot[bot] |
| 2026-10-21 | [chore(deps-dev): bump ruff from 0.17.0 to 0.17.1 (#842)](https://github.com/VRSEN/agency-swarm/commit/f79f6d69e18779069ee69405e73b3f64487af724) | dependabot[bot] |
| 2026-10-21 | [test: make concurrent multi-agency test send the bare value to SharedStateTool (#846)](https://github.com/VRSEN/agency-swarm/commit/1ac9e7f87fc5b04738a9622a87400a2c181b60e3) | nicko-ai |
| 2026-10-21 | [fix: servers bind all interfaces again; browser demos stay on localhost (#835)](https://github.com/VRSEN/agency-swarm/commit/1d841edb10f5e64b335e1c6fd2bc5c46b5b52a1b) | nicko-ai |
| 2026-10-15 | [chore(deps): bump pydantic from 2.13.5 to 2.14.1 (#837)](https://github.com/VRSEN/agency-swarm/commit/a86d657e12b693be64a8dcb8ead560a7b9a4ef01) | dependabot[bot] |
| 2026-10-15 | [chore(deps-dev): bump langchain-core from 1.6.3 to 1.6.9 (#838)](https://github.com/VRSEN/agency-swarm/commit/feb36786ee4534d9b40697f38878e8d726aa17b0) | dependabot[bot] |
| 2026-10-15 | [chore(deps-dev): bump mypy from 2.3.1 to 2.4.0 (#839)](https://github.com/VRSEN/agency-swarm/commit/438e2ff36fe3d653b0b0b01281333ab9d8562448) | dependabot[bot] |

[See all commits ↗](https://github.com/VRSEN/agency-swarm/commits)

## 👥 Top contributors

[nicko-ai](https://github.com/nicko-ai) (1662) · [VRSEN](https://github.com/VRSEN) (478) · [ArtemShatokhin](https://github.com/ArtemShatokhin) (441) · [dependabot[bot]](https://github.com/dependabot[bot]) (57) · [dumitruPuggle](https://github.com/dumitruPuggle) (28)

## ⬇️ Get it

```bash
git clone https://github.com/VRSEN/agency-swarm.git
```
