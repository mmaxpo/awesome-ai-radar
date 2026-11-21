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
| ⭐ **Stars** | 71.8k |
| 🍴 **Forks** | 7.9k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/cline/cline/issues) |
| 💻 **Languages** | TypeScript 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2024-07-06 |
| 📦 **Latest release** | [v4.1.27](https://github.com/cline/cline/releases/tag/v4.1.27) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 623.6 MB |
| 🌐 **Website** | https://cline.bot |

## 📦 Recent releases

### [v4.1.27](https://github.com/cline/cline/releases/tag/v4.1.27)
<sub>2026-11-21 · today</sub>

> **Added**
> - LM Studio settings have an API key field, for servers with "Require Authentication" turned on.
> - The MCP tab shows a "read-only" badge on tools whose server declares them read-only.
> - The Account view has a Privacy settings link to the Cline web app's data-use preferences.
> - The extension package now includes its third-party license notices.
> **Changed**
> …

### [desktop-v0.0.50](https://github.com/cline/cline/releases/tag/desktop-v0.0.50) — Desktop v0.0.50
<sub>2026-11-21 · today</sub>

> - The thinking picker offers **Max** reasoning effort, for models whose top level is max
> - A manual `/compact` can be stopped. Before, it could sit on "Thinking…" with no Stop button when the summarizer stalled
> - With no saved model, the Cline provider now starts on the first free model instead of Claude Sonnet 5.5. Saved selections are untouched
> - The Account view has a Privacy settings link to the Cline web app's data-use preferences
> - Settings → About has a **Third-party notices** entry with the licenses for the open source software included in Cline
> - On macOS, Check for Updates from the menu runs once instead of twice
> …

### [cli-v3.0.75](https://github.com/cline/cline/releases/tag/cli-v3.0.75) — CLI v3.0.75
<sub>2026-11-21 · today</sub>

> - One-shot runs (a prompt argument or piped stdin) now start in yolo mode instead of act mode, since nobody is at the keyboard to approve tools. Act mode is kept when auto-approve is off (`--auto-approve false` or the saved setting), when a mode flag is passed, when plan mode is saved, or when the prompt is a `/team` prompt. Yolo mode has no team tools, so pass `--act` when you need them
> - `--timeout` and Ctrl+C now stop the first turn of a one-shot run. Before, neither could interrupt it
> - The CLI no longer reads `.env` or `bunfig.toml` from the directory it is launched in
> - With no saved model, the Cline provider now starts on the first free model instead of Claude Sonnet 5.5. Saved selections are untouched
> - `/account` shows a Privacy settings link to the Cline web app's data-use preferences
> - `read_files` results are no longer cut to 8k characters on the way to the model. A read now arrives in full, up to the tool's own limit of 2000 lines or about 48k characters
> …

### [sdk/sdk/v0.2.1](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.1) — SDK v0.2.1
<sub>2026-11-21 · today</sub>

> - `read_files` results are no longer re-cut to the 8k tool-result cap on the way to the provider. They use the 50k file-content cap, so a read the tool reported in full arrives in full. Command, search, MCP and custom tool results keep the 8k cap, and an explicit tool-result cap still applies
> - Models that need interleaved reasoning get a placeholder `reasoning_content` on assistant messages that have none. This fixes Reflection Beam's `400 Missing required parameter: 'messages[n].reasoning_content'` after compaction or a model switch. The fact is carried as `ModelInfo.metadata.interleavedReasoningField`
> - The summarizer now states a preference to go without reasoning instead of disabling it outright. The gateway disables it only for models whose catalog entry advertises an off option. Before, uncatalogued models got `reasoning_effort: "none"`, which some endpoints reject, and compaction fell back to basic
> - A custom model with saved overrides now has `reasoning` seeded into its capability list unless it sets `supportsReasoning: false`, so an explicit reasoning disable reaches the provider. Before, gpt-5.6 and gpt-6 chat-completions endpoints rejected every tool call
> - The native OpenAI adapter fits the reasoning level to the model's advertised effort ladder, so `max` and Extra High are no longer sent verbatim to GPT-5.x and o-series models that reject them
> - LiteLLM: the legacy `max_tokens` is no longer used as the input budget when `max_output_tokens` is set. Null limits are treated as missing
> …

### [v4.1.26](https://github.com/cline/cline/releases/tag/v4.1.26)
<sub>2026-10-26 · 26d ago</sub>

> **Added**
> - Cloud tasks: Settings > API Configuration has a Local | Cloud toggle when cloud sessions are on. Cloud picks the Cline model new cloud tasks run on, saved separately from your local models. Clicking the model label in a cloud session's composer opens it there.
> - Starting or resuming a cloud sandbox shows a progress card with the repo, branch and steps (start sandbox, clone repository, start agent). It collapses once the agent starts.
> **Changed**
> - Cloud sessions hide the Plan/Act toggle and the auto-approve bar instead of showing them disabled.
> - With no model chosen, the Cline provider uses Claude Sonnet 5.5 again, which is back at the top of Cline's recommended list.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [chore(vscode): release v4.1.27](https://github.com/cline/cline/commit/8075d2e35cf5cad67c24f180c80a05d311b74a3e) | saoudrizwan |
| 2026-11-21 | [docs(desktop): drop flag-gated cloud items from the 0.0.50 notes](https://github.com/cline/cline/commit/e68fba63b3d7687cb518de378c9505efa007da67) | saoudrizwan |
| 2026-11-21 | [chore(desktop): release v0.0.50](https://github.com/cline/cline/commit/4e3add853d898e601d93f5b2a7e851a8f18f5c13) | saoudrizwan |
| 2026-11-21 | [chore(cli): release v3.0.75](https://github.com/cline/cline/commit/06f0ec711ea417430d552b98e7911fdac6f495a1) | saoudrizwan |
| 2026-11-21 | [chore(sdk): release v0.2.1](https://github.com/cline/cline/commit/0905e828929c2e89ee710eb3c899487e86064e82) | saoudrizwan |
| 2026-11-21 | [test(llms): accept tiered Qwen families in the prompt-cache route test](https://github.com/cline/cline/commit/0d7f2b18f94d913b3f2da1eebf7888803dab18a4) | saoudrizwan |
| 2026-11-21 | [Add third party licenses to the desktop app (#15816)](https://github.com/cline/cline/commit/9f750b8a3dfbb441b629547d5d84aca130ea3828) | BarreiroT |
| 2026-11-21 | [Add the third party notices to the CLI (#15811)](https://github.com/cline/cline/commit/4a5c5919308d32c29a116b345b88886a748d0929) | BarreiroT |
| 2026-11-21 | [Attach the third party notices on our VSIX (#15809)](https://github.com/cline/cline/commit/456a695f35af7c3f852cf7fcd74c03d09bfb2602) | BarreiroT |
| 2026-11-20 | [test(llms): remove image-model assertion on the generated catalog (#1…](https://github.com/cline/cline/commit/e8227d6f2e2725fdaad67e1a2ab9323e69b12516) | saoudrizwan |

[See all commits ↗](https://github.com/cline/cline/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cline/cline.git
```
