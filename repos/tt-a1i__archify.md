# tt-a1i/archify

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/tt-a1i/archify)

> Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why it's worth a look** | Turn any idea or codebase into an interactive diagram |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 98.5k |
| 🍴 **Forks** | 6.7k |
| 🐞 **Open issues + PRs** | [364](https://github.com/tt-a1i/archify/issues) |
| 💻 **Languages** | JavaScript 91% · CSS 4% · HTML 3% · Astro 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `architecture-diagram` `developer-tools` `system-design` `agent-skills` `codex` `opencode` `sequence-diagram` `deepseek-harness` `dsh-plugin` `coding-agents` `diagrams` `diagrams-as-code` `software-architecture` `ai-agents` `claude-code` `claude-skills` `flowchart` `llm` `mermaid` `visualization` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-04-15 |
| 📦 **Latest release** | [archify-dsh-v1.1.0](https://github.com/tt-a1i/archify/releases/tag/archify-dsh-v1.1.0) — 2026-11-08 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1762.6 MB |
| 🌐 **Website** | https://archify.si |

## 📦 Recent releases

### [archify-dsh-v1.1.0](https://github.com/tt-a1i/archify/releases/tag/archify-dsh-v1.1.0) — Archify DSH 1.1.0
<sub>2026-11-08 · 12d ago</sub>

> Published `@tt-a1i/archify-dsh@1.1.0` — a Skill-only DeepSeek Harness bundle containing Archify 3.2.0.
> - Published: 2026-11-08 (npm `latest`)
> - Bundled Skill: Archify 3.2.0, pinned to `edf158c4e7a1d18d20cc329840f864289634c090`
> - Accepted host: `@deepseek-ai/dsh@0.2.1-rc.2` (developer preview), Node `^22.19.0 || >=24.0.0`
> - Tarball SHA256: `e65d77e4d7ca34562d33f22480b0b4eae2b1e51ef13cd542c2618b228830b20d`
> - Three-platform release gate: https://github.com/tt-a1i/archify/actions/runs/42499004935
> …

### [v3.2.0](https://github.com/tt-a1i/archify/releases/tag/v3.2.0)
<sub>2026-10-19 · 1mo ago</sub>

> **Archify v3.2.0**
> Create a conclusion-first one-page answer from Markdown, with cited sources, interactive diagrams and browser exports.
> **Added**
> - **One-page answers (explainer) (#993).** Ask your agent to answer as a page and Archify builds a conclusion-first explainer from a Markdown draft. Each panel answers one question, using prose, tables, steps, checklists, charts, code and validated native diagrams.
>   - **Authoring and delivery:** `finalize explainer` validates, delivers atomically and checks the page. Charts come from a Mermaid fence or a CSV/JSON file next to the draft. Repository excerpts are read from the pinned commit. `patch explainer` replaces one panel by ID.
>   - **Reading:**
> …

### [v3.1.0](https://github.com/tt-a1i/archify/releases/tag/v3.1.0)
<sub>2026-10-13 · 1mo ago</sub>

> **Archify 3.1.0**
> https://github.com/user-attachments/assets/d6144aba-cb48-4692-a24d-b43bf7be62c2
> *30 seconds of Archify 3.1: five new diagram types, Live motion, light and dark.*
> Ten diagram types, with Live motion enabled by default: **ERD, Class/interface, Tree, Timeline and Waterfall** join Architecture, Workflow, Sequence, Dataflow and Lifecycle.
> - Type-specific motion stays separate from authored topology; switch to Still when needed.
> - Clearer cards, routing/label coordination, Sequence notes, Lifecycle layouts, and long-page reader navigation.
> …

### [archify-dsh-v1.0.0](https://github.com/tt-a1i/archify/releases/tag/archify-dsh-v1.0.0) — Archify DSH 1.0.0
<sub>2026-10-04 · 1mo ago</sub>

> **Archify DSH 1.0.0**
> `@tt-a1i/archify-dsh@1.0.0` brings the Archify 3.x authoring and delivery flow to the DeepSeek Harness community integration. It bundles Archify **3.0.1**, including the post-tag Skill installation fix from #704, from immutable source `7158026e852f3aa6578c741e673b46d7878c92c1`. Adapter and Archify version numbers are independent.
> The supported host is exactly **`@deepseek-ai/dsh@0.1.2-rc.1`**, with Node **`^22.19.0 || >=24.0.0`**. DSH remains a developer preview; the adapter's 1.0 contract does not promise compatibility with other host versions. This is a community integration, not an official DeepSeek product.
> **Install and upgrade**
> Update the DSH host separately to the supported version, then run this command in each profile that uses Archify:
> ```bash
> …

### [v3.0.1](https://github.com/tt-a1i/archify/releases/tag/v3.0.1)
<sub>2026-09-28 · 1mo ago</sub>

> Archify 3.0.1 makes stable update reminders part of normal diagram delivery. `finalize` and standalone `deliver` now include a bounded update result in their receipts and terminal output, and the Skill carries one reminder into its final response when a newer verified release is known. A reminder repeats until the user updates or explicitly asks to snooze it for seven days or ignore that exact release. Checks use the fixed official manifest and cached results; no update installs automatically.
> The diagram format, generated HTML/SVG content, validation quality gates, and existing path protections are unchanged. See the [changelog](https://github.com/tt-a1i/archify/blob/v3.0.1/CHANGELOG.md) for the full entry.
> **What's Changed**
> * Publish v3.0.0 stable update manifest by @tt-a1i in https://github.com/tt-a1i/archify/pull/598
> * Keep update notices in diagram delivery receipts by @tt-a1i in https://github.com/tt-a1i/archify/pull/599
> * Promote update reminders to stable by @tt-a1i in https://github.com/tt-a1i/archify/pull/610
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [Merge pull request #1423 from tt-a1i/feat/geo-seo-v3-main](https://github.com/tt-a1i/archify/commit/8509a3d63e763b4d454ea9aafa1f939545fcb1ea) | tt-a1i |
| 2026-11-21 | [docs(geo): clarify QbitAI command attribution and architecture placem…](https://github.com/tt-a1i/archify/commit/f524d8009a44bda29089f6187b19204e1e88f17a) | tt-a1i |
| 2026-11-21 | [Extract the real Skill ZIP reliably in the Windows install tests](https://github.com/tt-a1i/archify/commit/f06c31f74cbf48144e6de9618433d2999c0dbcd9) | tt-a1i |
| 2026-11-21 | [fix(seo): block explainer JSON pointer 404s and ship GEO v3 supersess…](https://github.com/tt-a1i/archify/commit/2ce3549b845db894e4fa7391260fed91f90aa0ee) | tt-a1i |
| 2026-11-17 | [Merge pull request #1390 from tt-a1i/feat/geo-universal-positioning-main](https://github.com/tt-a1i/archify/commit/44781293f38728baf04dbad33ce1a0cef8c39cca) | tt-a1i |
| 2026-11-17 | [docs(geo): qualify explainer opt-in browser check per review](https://github.com/tt-a1i/archify/commit/d9b4f0961f669dffd9805fe117d5bc1603ee6c88) | tt-a1i |
| 2026-11-17 | [docs(geo): align waterfall description with execution-span schema](https://github.com/tt-a1i/archify/commit/a0613c95e8287178152129598e294c768df6211d) | tt-a1i |
| 2026-11-17 | [docs(geo): broaden positioning to universal interactive diagrams and …](https://github.com/tt-a1i/archify/commit/a2dc77804ecc6f415b594b553b40ba1e91d48da1) | tt-a1i |
| 2026-11-15 | [Merge pull request #1369 from tt-a1i/feat/geo-upgrade-main](https://github.com/tt-a1i/archify/commit/a7ed6fd6657da90414831d1d42cf95987188750c) | tt-a1i |
| 2026-11-15 | [fix(geo): resolve CI Cloudflare regressions and address review feedback](https://github.com/tt-a1i/archify/commit/ca846760ff380b2f32cd799c4fe8e0accb9aacdc) | tt-a1i |

[See all commits ↗](https://github.com/tt-a1i/archify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tt-a1i/archify.git
```
