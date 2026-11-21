# Aider-AI/aider

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Aider-AI/aider)

> aider is AI pair programming in your terminal

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Classic AI pair programmer in the terminal, git-aware |
| **Added** | 2026-11-15 |

💤 **Quiet** — no activity for 6mo

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 50.2k |
| 🍴 **Forks** | 5.2k |
| 🐞 **Open issues + PRs** | [2.0k](https://github.com/Aider-AI/aider/issues) |
| 💻 **Languages** | Python 80% · CSS 4% · Shell 4% · Tree-sitter Query 4% · JavaScript 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `chatgpt` `cli` `command-line` `gpt-4` `openai` `gpt-3` `gpt-35-turbo` `claude-3` `gpt-4o` `anthropic` `gemini` `llama` `sonnet` |
| 🕒 **Last activity** | 2026-05-22 (6mo ago) |
| 📅 **Created** | 2023-05-09 |
| 📦 **Latest release** | [v0.86.0](https://github.com/Aider-AI/aider/releases/tag/v0.86.0) — 2025-08-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 137.1 MB |
| 🌐 **Website** | https://aider.chat/ |

## 📦 Recent releases

### [v0.86.0](https://github.com/Aider-AI/aider/releases/tag/v0.86.0) — Aider v0.86.0
<sub>2025-08-09 · 1y ago</sub>

> - Added support for all GPT-5 models.
> - Added support for Grok-4 via `xai/grok-4` and `openrouter/x-ai/grok-4` model names.
> - Added support for `gemini/gemini-2.5-flash-lite-preview-06-17` model, by Tamir Zahavi-Brunner.
> - `/clear` now prints “All chat history cleared.” so you know it worked, by Zexin Yuan.
> - `/undo` output now shows only the first line of each commit message, making it easier to read.
> - Added support for `openrouter/moonshotai/kimi-k2` model, by Jack Harrington.
> …

### [v0.85.0](https://github.com/Aider-AI/aider/releases/tag/v0.85.0) — Aider v0.85.0
<sub>2025-06-27 · 1y ago</sub>

> **New Models**
> - Added support for new Gemini models including `gemini-2.5-pro`, `gemini-2.5-flash`, and `gemini-2.5-pro-preview-06-05` with thinking tokens support.
> - Updated model aliases: `flash` now points to `gemini-2.5-flash` and `gemini` now points to `gemini-2.5-pro`.
> - Support for Responses API models like o1-pro, o3-pro.
> - Added support for OpenAI o3-pro model across multiple providers.
> - Enhanced thinking tokens support: can now be disabled by setting to 0, and improved help text with examples.
> …

### [v0.84.0](https://github.com/Aider-AI/aider/releases/tag/v0.84.0) — Aider v0.84.0
<sub>2025-05-30 · 1y ago</sub>

> **Model support & provider updates**
> - Added support for new Claude models including the Sonnet 4 and Opus 4 series (e.g., `claude-sonnet-4-20250514`,
> `claude-opus-4-20250514`) across various providers. The default `sonnet` and `opus` aliases were updated to these newer
> versions.
> - Added support for the `vertex_ai/gemini-2.5-flash-preview-05-20` model.
> - Updated default OpenRouter models during onboarding to `deepseek/deepseek-r1:free` for the free tier and
> …

### [v0.83.0](https://github.com/Aider-AI/aider/releases/tag/v0.83.0) — Aider v0.83.0
<sub>2025-05-09 · 1y ago</sub>

> - Added support for `gemini-2.5-pro-preview-05-06` models.
> - Added support for `qwen3-235b` models.
> - Added repo-map support for OCaml and OCaml interface files, by Andrey Popp.
> - Added a spinner animation while waiting for the LLM to start streaming its response.
> - Updated the spinner animation to a Knight Rider style.
> - Introduced `--attribute-co-authored-by` option to add co-author trailer to commit messages, by Andrew Grigorev.
> …

### [v0.82.0](https://github.com/Aider-AI/aider/releases/tag/v0.82.0) — Aider v0.82.0
<sub>2025-04-14 · 1y ago</sub>

> - Support for GPT 4.1, mini and nano.
> - Improved support for using architect mode with Gemini 2.5 Pro.
> - Add support for `xai/grok-3-beta`, `xai/grok-3-mini-beta`, `openrouter/x-ai/grok-3-beta`,
> `openrouter/x-ai/grok-3-mini-beta`, and `openrouter/openrouter/optimus-alpha` models.
> - Added support for `grok-3-fast-beta` and `grok-3-mini-fast-beta` models.
> - Added new `patch` edit format for OpenAI's GPT-4.1 model.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-05-22 | [Merge pull request #5173 from Cyberfilo/feat/anthropic_models-list-ad…](https://github.com/Aider-AI/aider/commit/5dc9490bb35f9729ef2c95d00a19ccd30c26339c) | paul-gauthier |
| 2026-05-22 | [Apply ANTHROPIC_MODELS expansion](https://github.com/Aider-AI/aider/commit/a7a54a9367fefb46fa576840e97f4479c46c7771) | Cyberfilo |
| 2026-05-22 | [Expand ANTHROPIC_MODELS list with recent Claude model names](https://github.com/Aider-AI/aider/commit/2ec3550e71c174efe84fe87d7fa669b66903fa41) | Cyberfilo |
| 2026-05-16 | [Merge pull request #5132 from Mramaran/add-bash-tree-sitter-tags](https://github.com/Aider-AI/aider/commit/6435cb8b1e885d7275327d4b61206b1b1618dfe1) | paul-gauthier |
| 2026-05-15 | [feat: add bash tree-sitter tags for repomap support](https://github.com/Aider-AI/aider/commit/ff191affc6e1413f33dad914d9930a5993aad853) | Mramaran |
| 2026-04-25 | [fix: update FAQ token percentages and switch history model to gpt-5.5](https://github.com/Aider-AI/aider/commit/3ec8ec5a7d695b08a6c24fe6c0c235c8f87df9af) | paul-gauthier |
| 2026-04-25 | [copy](https://github.com/Aider-AI/aider/commit/c723364ada98922cfc781d8d3968d53be6870882) | paul-gauthier |
| 2026-04-24 | [feat: add gpt-5.5 model settings across providers](https://github.com/Aider-AI/aider/commit/308b1546a035ef012ac91ffb83a2139d01325526) | paul-gauthier |
| 2026-04-24 | [test: update model alias expectations for sonnet and opus](https://github.com/Aider-AI/aider/commit/cd24a3a3c842c4566c198b2aa13b87c1ec78e3b2) | paul-gauthier |
| 2026-04-23 | [copy](https://github.com/Aider-AI/aider/commit/0189cf4f0009aa58fd24a3b8c834819c8230fa77) | paul-gauthier |

[See all commits ↗](https://github.com/Aider-AI/aider/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Aider-AI/aider.git
```
