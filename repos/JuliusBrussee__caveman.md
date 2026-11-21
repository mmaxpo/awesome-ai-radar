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
| ⭐ **Stars** | 121.9k |
| 🍴 **Forks** | 7.1k |
| 🐞 **Open issues + PRs** | [109](https://github.com/JuliusBrussee/caveman/issues) |
| 💻 **Languages** | Go 48% · JavaScript 26% · TypeScript 14% · Python 10% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `anthropic` `caveman` `claude` `claude-code` `llm` `meme` `prompt-engineering` `skill` `tokens` |
| 🕒 **Last activity** | 2026-11-20 (yesterday) |
| 📅 **Created** | 2026-04-04 |
| 📦 **Latest release** | [v4.1.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.1.0) — 2026-11-08 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 21.5 MB |
| 🌐 **Website** | https://docs.caveman.so/caveman |

## 📦 Recent releases

### [v4.1.0](https://github.com/JuliusBrussee/caveman/releases/tag/v4.1.0) — Caveman 4.1.0
<sub>2026-11-08 · 13d ago</sub>

> Caveman 4.1.0 is a maintenance release: bug fixes across compress, OpenCode, Hermes, Pi, the proxy and the hooks, a recovery store that no longer fills up and stops compressing, and a few small switches people asked for. caveman-compress now refuses a file with a key or token in it, and installs from skill hubs again.
> **Action needed**
> - **`forward_headers` under a `providers.<name>` block now stops the proxy from starting.** Before, it was silently ignored: no headers were forwarded and the only symptom was an upstream 401. Configure that upstream as a compat mount instead: `compat.<name>` with `base_url` and `forward_headers`, plus `wire_dialect: anthropic` if it speaks the Anthropic protocol (see `docs/technical/configuration.md`) (#1458).
> - **caveman-compress refuses a file whose text holds a credential**, such as a private key block or a cloud, Git host or model API token. Compression sends the file to your model provider, so move the secret into an env var or secret manager first. The error names the line, never the secret. Placeholders like `sk-...` or `$OPENAI_API_KEY` still compress (#1471).
> **Changed**
> - **Old recovery handles can now expire.** The recovery store used to keep every compressed original forever, so it filled up and compression stopped (#1370). When a write would exceed the store's cap, it now frees room: typed objects of sessions idle 14 days (archived) or 30 days (any) are expired, oldest first, until the store is at 80%. Retrieving an expired handle answers `cave_expired_recovery`, and each expiry is logged in `proxy.log`. Blob recoveries never expire (#1481).
> …

### [middleware-python-v1.0.1](https://github.com/JuliusBrussee/caveman/releases/tag/middleware-python-v1.0.1) — caveman-middleware 1.0.1
<sub>2026-11-08 · 13d ago</sub>

> - Security: the `litellm` extra excludes litellm 1.107.0, which upstream
>   reported compromised
>   ([security incident, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)),
>   and 1.106.0 to 1.106.2, which import the optional `mcp` package on ordinary
>   tool calls. The extra also requires a patched `filelock` (4.2.1 or later).
> - `anthropic` 2.x is inside the supported range (`>=1.0,<3`). Before this, the
> …

### [middleware-ts-v1.1.0](https://github.com/JuliusBrussee/caveman/releases/tag/middleware-ts-v1.1.0) — @caveman-ai/middleware 1.1.0
<sub>2026-11-08 · 13d ago</sub>

> - Security: the MCP adapter now requires `@modelcontextprotocol/sdk` 1.32.0 or
>   later. Earlier releases followed redirects to any origin and handed it custom
>   headers, and on 307/308 the request body including OAuth tokens
>   ([GHSA-6prh-2h8m-c8cw](https://osv.dev/vulnerability/GHSA-6prh-2h8m-c8cw)).
>   With 1.30.x or 1.31.x installed, MCP results pass through uncompressed and a
>   warning names the advisory and the version to upgrade to.
> …

### [bin-v4.1.0](https://github.com/JuliusBrussee/caveman/releases/tag/bin-v4.1.0)
<sub>2026-11-07 · 14d ago</sub>

> Signed Caveman runtime companions for macOS, Linux, and Windows. The binaries are licensed under the Apache License 2.0 (LICENSE, NOTICE); see LICENSING.md and the attached third-party notices. The ghcr.io caveman-proxy image is still built without cgo, so its code compressor handles Go source only; the caveman-proxy and caveman-engine binaries here also compress TypeScript, JavaScript, Python, Rust, Java and C/C++.

### [bin-v4.0.2](https://github.com/JuliusBrussee/caveman/releases/tag/bin-v4.0.2)
<sub>2026-10-23 · 29d ago</sub>

> Signed Caveman runtime companions for macOS, Linux, and Windows. The binaries are licensed under the Apache License 2.0 (LICENSE, NOTICE); see LICENSING.md and the attached third-party notices. The ghcr.io caveman-proxy image is still built without cgo, so its code compressor handles Go source only; the caveman-proxy and caveman-engine binaries here also compress TypeScript, JavaScript, Python, Rust, Java and C/C++.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [docs(readme): say what Caveman Code measured](https://github.com/JuliusBrussee/caveman/commit/a192894723a8f47e7f504c7b5041967ff1f18e55) | JuliusBrussee |
| 2026-11-17 | [chore: drop stale monorepo paths and private references from comments](https://github.com/JuliusBrussee/caveman/commit/3a0d376c1c1065f84bfae3b7518667defb394ff9) | JuliusBrussee |
| 2026-11-17 | [fix(engine): pixel atlas and golden generators write inside this repo](https://github.com/JuliusBrussee/caveman/commit/ace655cf7260206f2fc84a7edfb5e6600c83708a) | JuliusBrussee |
| 2026-11-17 | [chore(provider-catalog): mark the workspace package private](https://github.com/JuliusBrussee/caveman/commit/d775f2e8e6b35dcca295eeb4f6c3bed2258c0955) | JuliusBrussee |
| 2026-11-17 | [test(installer): run the stable PATH node test on a dynamically linke…](https://github.com/JuliusBrussee/caveman/commit/8846a12b5f98f8bf41cf44632432b3d21bb3af22) | JuliusBrussee |
| 2026-11-17 | [fix(cli): remove dev and deploy aws, which printed make targets this …](https://github.com/JuliusBrussee/caveman/commit/1cbe5b6290665298b15ef10a019687f502017ff1) | JuliusBrussee |
| 2026-11-17 | [docs: state benchmark numbers with their samples and drop private ref…](https://github.com/JuliusBrussee/caveman/commit/edd564851a75e1f3c31235e9edf0e4d6403221af) | JuliusBrussee |
| 2026-11-17 | [docs: collapse per-folder agent docs into one AGENTS.md each](https://github.com/JuliusBrussee/caveman/commit/8e00433f1a573c1b26a2135ec4cb9c67f50e2433) | JuliusBrussee |
| 2026-11-17 | [docs(technical): drop audits and design records, fold live rules in](https://github.com/JuliusBrussee/caveman/commit/299dac5212de6bebe13f5ea99b0babf359003549) | JuliusBrussee |
| 2026-11-17 | [docs: make AGENTS.md the agent guide and add docs/WHY.md](https://github.com/JuliusBrussee/caveman/commit/87f163debad0248dcf8b64abbf313a9eb6929a36) | JuliusBrussee |

[See all commits ↗](https://github.com/JuliusBrussee/caveman/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuliusBrussee/caveman.git
```
