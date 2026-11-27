# JuliusBrussee/caveman

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/JuliusBrussee/caveman)

> why use many token when few token do trick. Skill + local proxy for coding agents: shorter answers, smaller tool output, every original recoverable.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Skill + proxy that makes coding agents talk in far fewer tokens |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 123.2k |
| 🍴 **Forks** | 7.2k |
| 🐞 **Open issues + PRs** | [117](https://github.com/JuliusBrussee/caveman/issues) |
| 💻 **Languages** | Go 50% · JavaScript 26% · TypeScript 14% · Python 10% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `anthropic` `caveman` `claude` `claude-code` `llm` `meme` `prompt-engineering` `skill` `tokens` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-04-04 |
| 📦 **Latest release** | [v4.2.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.2.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.7 MB |
| 🌐 **Website** | https://docs.caveman.so/caveman |

## 📦 Recent releases

### [v4.2.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.2.0) — Caveman 4.2.0
<sub>2026-11-22 · 5d ago</sub>

> Caveman 4.2.0 adds a QuickJS Code-Mode MCP gateway (`caveman codemode` / `caveman wrap --codemode`) with multi-agent overlays, multi-harness tool-envelope unwrapping in the compression engine, cache-safe proxy optimizations (local turn-effort gating, duplicate-read collapsing, canonical tool ordering, and `defer_loading`), `@caveman-ai/middleware/codemode`, opt-in Code-Mode support in `@caveman-ai/pi` 0.4.0, and a native Codex CLI provider for `caveman-compress`.
> **New**
> **QuickJS Code-Mode MCP gateway** (#1559)
> - **`caveman-mcp codemode` and `caveman codemode`** collapse large upstream stdio and HTTP MCP catalogs into a static, prefix-cache-safe set of Code-Mode tools (`codemode_search_tools`, `codemode_execute`, `codemode_mutate`) backed by an embedded pure-Go QuickJS sandbox (`modernc.org/quickjs`) plus built-in repo and PR helpers (`batch_read`, `symbol_outline`, `pr_read`, `ci_logs`).
> - **`caveman wrap --codemode`** installs temporary per-session Code-Mode overlays for Claude Code, Codex, OpenCode, Gemini CLI, Qwen Code, Kilo, OpenClaw, Pi, and Hermes (including `config.yaml` sync-back of in-session Hermes edits; Cursor MCP configs are discovered by `caveman codemode`).
> - **Workspace MCP discovery is explicit:** workspace-local MCP definitions are loaded only when `--trust-workspace-mcp` or `CAVEMAN_TRUST_WORKSPACE_MCP=1` is set.
> …

### [bin-v4.2.0](https://github.com/JuliusBrussee/caveman/releases/tag/bin-v4.2.0)
<sub>2026-11-22 · 5d ago</sub>

> Signed Caveman runtime companions for macOS, Linux, and Windows. The binaries are licensed under the Apache License 2.0 (LICENSE, NOTICE); see LICENSING.md and the attached third-party notices. The ghcr.io caveman-proxy image is still built without cgo, so its code compressor handles Go source only; the caveman-proxy and caveman-engine binaries here also compress TypeScript, JavaScript, Python, Rust, Java and C/C++.

### [middleware-ts-v1.2.0](https://github.com/JuliusBrussee/caveman/releases/tag/middleware-ts-v1.2.0) — @caveman-ai/middleware 1.2.0
<sub>2026-11-22 · 5d ago</sub>

> - Add the `@caveman-ai/middleware/codemode` subpath (`createCodeModeToolset`):
>   a provider-agnostic, zero-dependency in-process Code-Mode toolset that
>   collapses large framework or MCP tool catalogs into three static,
>   prefix-cache-safe meta-tools (`codemode_search_tools`, `codemode_execute`,
>   and `codemode_mutate`) with BM25 discovery, structured execution pipelines,
>   and read/write separation (#1559).
> …

### [v4.1.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.1.0) — Caveman 4.1.0
<sub>2026-11-08 · 19d ago</sub>

> Caveman 4.1.0 is a maintenance release: bug fixes across compress, OpenCode, Hermes, Pi, the proxy and the hooks, a recovery store that no longer fills up and stops compressing, and a few small switches people asked for. caveman-compress now refuses a file with a key or token in it, and installs from skill hubs again.
> **Action needed**
> - **`forward_headers` under a `providers.<name>` block now stops the proxy from starting.** Before, it was silently ignored: no headers were forwarded and the only symptom was an upstream 401. Configure that upstream as a compat mount instead: `compat.<name>` with `base_url` and `forward_headers`, plus `wire_dialect: anthropic` if it speaks the Anthropic protocol (see `docs/technical/configuration.md`) (#1458).
> - **caveman-compress refuses a file whose text holds a credential**, such as a private key block or a cloud, Git host or model API token. Compression sends the file to your model provider, so move the secret into an env var or secret manager first. The error names the line, never the secret. Placeholders like `sk-...` or `$OPENAI_API_KEY` still compress (#1471).
> **Changed**
> - **Old recovery handles can now expire.** The recovery store used to keep every compressed original forever, so it filled up and compression stopped (#1370). When a write would exceed the store's cap, it now frees room: typed objects of sessions idle 14 days (archived) or 30 days (any) are expired, oldest first, until the store is at 80%. Retrieving an expired handle answers `cave_expired_recovery`, and each expiry is logged in `proxy.log`. Blob recoveries never expire (#1481).
> …

### [middleware-python-v1.0.1](https://github.com/JuliusBrussee/caveman/releases/tag/middleware-python-v1.0.1) — caveman-middleware 1.0.1
<sub>2026-11-08 · 19d ago</sub>

> - Security: the `litellm` extra excludes litellm 1.107.0, which upstream
>   reported compromised
>   ([security incident, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)),
>   and 1.106.0 to 1.106.2, which import the optional `mcp` package on ordinary
>   tool calls. The extra also requires a patched `filelock` (4.2.1 or later).
> - `anthropic` 2.x is inside the supported range (`>=1.0,<3`). Before this, the
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [docs(workflow): document clean worktree and green-CI PR workflow in A…](https://github.com/JuliusBrussee/caveman/commit/e74a11ccdb38b98d15c9f9545787c907dd15f0ab) | JuliusBrussee |
| 2026-11-24 | [chore(hygiene): remove private path references and external competito…](https://github.com/JuliusBrussee/caveman/commit/47c61be2d10a354f0c5cbe2b90959d24c06b16c6) | JuliusBrussee |
| 2026-11-24 | [docs(agents): add public Caveman ecosystem repository pointers](https://github.com/JuliusBrussee/caveman/commit/27ead7169f563b21de8eb53c71b1cef0d495f963) | JuliusBrussee |
| 2026-11-23 | [chore: sync SKILL.md copies [skip ci]](https://github.com/JuliusBrussee/caveman/commit/b89752f6bca5a26bfde8b019813554241800ca99) | github-actions[bot] |
| 2026-11-23 | [fix: address PR review findings across codemode, HTML tables, Pi comp…](https://github.com/JuliusBrussee/caveman/commit/af5c6b085169c5840ff583beedece1debca7c19b) | JuliusBrussee |
| 2026-11-23 | [fix(pi): match api.anthropic.com and api.openai.com by parsed hostname](https://github.com/JuliusBrussee/caveman/commit/9547565d9d32f561bce935725cd463e75a75b450) | JuliusBrussee |
| 2026-11-23 | [docs: update technical docs and sync root codex manifest to 4.2.0](https://github.com/JuliusBrussee/caveman/commit/8428036b4d98232edc7df56fc38176ac88d14cd5) | JuliusBrussee |
| 2026-11-23 | [fix(codemode): support OpenCode V2 mcp.servers masking and Hermes flo…](https://github.com/JuliusBrussee/caveman/commit/8db3be74cb4c80e46a0e5d66920aef7269bac619) | JuliusBrussee |
| 2026-11-23 | [fix(codemode): classify compound write verbs as mutating](https://github.com/JuliusBrussee/caveman/commit/08587894364428c7a977dbd94800201dafe05ee3) | JuliusBrussee |
| 2026-11-23 | [chore(profiles): verify and pin latest coding agent CLI versions](https://github.com/JuliusBrussee/caveman/commit/0e15c7a8709290cf06d7c116b529c0361bd5273d) | JuliusBrussee |

[See all commits ↗](https://github.com/JuliusBrussee/caveman/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuliusBrussee/caveman.git
```
