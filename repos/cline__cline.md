# cline/cline

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/cline/cline)

> Autonomous coding agent as an SDK, IDE extension, or CLI assistant.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Autonomous coding agent inside VS Code |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 71.9k |
| 🍴 **Forks** | 8.0k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/cline/cline/issues) |
| 💻 **Languages** | TypeScript 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (yesterday) |
| 📅 **Created** | 2024-07-06 |
| 📦 **Latest release** | [v4.1.28](https://github.com/cline/cline/releases/tag/v4.1.28) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 623.7 MB |
| 🌐 **Website** | https://cline.bot |

## 📦 Recent releases

### [v4.1.28](https://github.com/cline/cline/releases/tag/v4.1.28)
<sub>2026-11-26 · yesterday</sub>

> **Changed**
> - Refreshed the model catalog. The OpenAI provider no longer lists ids the upstream catalog marks deprecated, including `gpt-4o`, `gpt-4.1`, `gpt-5`, `gpt-5-mini`, `gpt-5.1`, `gpt-5.3-codex`, `o3` and `o3-pro`. `gpt-5.3-codex-spark` is no longer listed for ChatGPT subscriptions. Adds the Concentrate and Prima Labs providers.
> - The third-party license notices in the extension package now cover software that was missing from the list.
> - Internal telemetry cleanup.
> **Full Changelog**: https://github.com/cline/cline/compare/v4.1.27...v4.1.28

### [desktop-v0.0.51](https://github.com/cline/cline/releases/tag/desktop-v0.0.51) — Desktop v0.0.51
<sub>2026-11-26 · yesterday</sub>

> - Refreshed the model catalog. The OpenAI provider no longer lists ids the upstream catalog marks deprecated, including `gpt-4o`, `gpt-4.1`, `gpt-5`, `gpt-5-mini`, `gpt-5.1`, `gpt-5.3-codex`, `o3` and `o3-pro`. `gpt-5.3-codex-spark` is no longer listed for ChatGPT subscriptions. Adds the Concentrate and Prima Labs providers
> - The third-party notices in Settings → About now cover software that was missing from the list
> - Internal telemetry cleanup
> **Full Changelog**: https://github.com/cline/cline/compare/desktop-v0.0.50...desktop-v0.0.51

### [cli-v3.0.76](https://github.com/cline/cline/releases/tag/cli-v3.0.76) — CLI v3.0.76
<sub>2026-11-26 · yesterday</sub>

> - The npm package now ships one `THIRD_PARTY_NOTICES.txt` at its root that covers every platform binary
> - Refreshed the bundled model catalog. The OpenAI picker no longer lists ids the upstream catalog marks deprecated, including `gpt-4o`, `gpt-4.1`, `gpt-5`, `gpt-5-mini`, `gpt-5.1`, `gpt-5.3-codex`, `o3` and `o3-pro`. `gpt-5.3-codex-spark` is no longer listed for ChatGPT subscriptions
> - Internal telemetry cleanup
> **Full Changelog**: https://github.com/cline/cline/compare/cli-v3.0.75...cli-v3.0.76

### [sdk/sdk/v0.2.2](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.2) — SDK v0.2.2
<sub>2026-11-26 · yesterday</sub>

> - Internal telemetry cleanup. Some telemetry helper exports were removed from `@cline/llms`, `@cline/shared` and `@cline/core`, and `@cline/llms` has fewer dependencies
> - `writeGlobalSettings`, `setTelemetryOptOutGlobally` and `setAutoUpdateEnabledGlobally` no longer take an options argument
> - Refreshed the bundled model catalog. It adds the `concentrate` and `primalabs` providers and changes the default model for 28 providers. OpenAI ids the upstream catalog now marks deprecated are no longer listed: `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`, `gpt-4.1-mini`, `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro`, `gpt-5.1`, `gpt-5.3-codex`, `gpt-5.3-codex-spark`, `gpt-5.4-nano`, `gpt-image-2`, `o3` and `o3-pro`. `MiniMax-M3` is no longer listed on the MiniMax coding plans
> **Full Changelog**: https://github.com/cline/cline/compare/sdk/sdk/v0.2.1...sdk/sdk/v0.2.2

### [v4.1.27](https://github.com/cline/cline/releases/tag/v4.1.27)
<sub>2026-11-21 · 6d ago</sub>

> **Added**
> - LM Studio settings have an API key field, for servers with "Require Authentication" turned on.
> - The MCP tab shows a "read-only" badge on tools whose server declares them read-only.
> - The Account view has a Privacy settings link to the Cline web app's data-use preferences.
> - The extension package now includes its third-party license notices.
> **Changed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [chore(vscode): release v4.1.28](https://github.com/cline/cline/commit/cbc7d1419a74464c622117a740fdfe87a5e0a7b2) | saoudrizwan |
| 2026-11-26 | [chore(desktop): release v0.0.51](https://github.com/cline/cline/commit/aa6e19157ffa709c37787f30c52ba37efcfd1120) | saoudrizwan |
| 2026-11-26 | [test(core): stop pinning a model id the catalog refresh dropped](https://github.com/cline/cline/commit/2a0f0485807a95c181bf8077da5689101f8b3cb1) | saoudrizwan |
| 2026-11-26 | [chore(cli): release v3.0.76](https://github.com/cline/cline/commit/05e50a5440252082998aff4bb5f19794df5ca19a) | saoudrizwan |
| 2026-11-26 | [chore(sdk): release v0.2.2](https://github.com/cline/cline/commit/ece04575c529d769f3e9e8e3fefe4dd471562c1d) | saoudrizwan |
| 2026-11-26 | [fix and update telemetry (#15871)](https://github.com/cline/cline/commit/0accde2b7e49694ffcee12e45a7947f7d4b63947) | saoudrizwan |
| 2026-11-26 | [Fix Third Party Notices [ENG-2594] (#15846)](https://github.com/cline/cline/commit/660460b0344c362c88c7b1fcb1bc03d067c60603) | BarreiroT |
| 2026-11-25 | [Fix bundled licenses (#15870)](https://github.com/cline/cline/commit/fa51b2bc70b687cd1c91ee42bd18394c2a94115a) | BarreiroT |
| 2026-11-25 | [Remove Langfuse (#15869)](https://github.com/cline/cline/commit/46441dc705656b3fc56d22ae398fc2d4565a3e23) | BarreiroT |
| 2026-11-23 | [Move the third party notices to the root on the CLI install (#15836)](https://github.com/cline/cline/commit/34c104e6fc49781cda4adcd73ffdccd8f029fef9) | BarreiroT |

[See all commits ↗](https://github.com/cline/cline/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cline/cline.git
```
