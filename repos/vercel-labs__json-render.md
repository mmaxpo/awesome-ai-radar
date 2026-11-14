# vercel-labs/json-render

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/vercel-labs/json-render)

> The Generative UI framework

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Vercel's generative-UI framework |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 19.6k |
| 🍴 **Forks** | 1.0k |
| 🐞 **Open issues + PRs** | [124](https://github.com/vercel-labs/json-render/issues) |
| 💻 **Languages** | TypeScript 81% · MDX 12% · Svelte 5% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-01-14 |
| 📦 **Latest release** | [v0.22.0](https://github.com/vercel-labs/json-render/releases/tag/v0.22.0) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 6.3 MB |
| 🌐 **Website** | https://json-render.dev |

## 📦 Recent releases

### [v0.22.0](https://github.com/vercel-labs/json-render/releases/tag/v0.22.0)
<sub>2026-11-04 · 9d ago</sub>

> **New Features**
> - **Chat SDK renderer:** Added `@json-render/chat` to render specs as Chat SDK cards, so one catalog posts natively on Slack, Teams, and the other Chat SDK platforms. `streamCard` streams a card into a thread and edits it as elements arrive, and `toCard` validates specs against per-component schemas and optional platform limits. State expressions, `visible`, and `repeat` resolve against `spec.state` (#451)
> - **Chat SDK example:** Added a playground that previews generated messages as Slack renders them, with a Teams Adaptive Card view and a copy button for Block Kit Builder (#451)
> **Contributors**
> - @Railly

### [v0.21.4](https://github.com/vercel-labs/json-render/releases/tag/v0.21.4)
<sub>2026-11-01 · 13d ago</sub>

> **Documentation**
> - Added the **eve TanStack Agent template** to the examples page, with links to its source repository and Vercel template (#442)
> - Added shared **technical writing guidance** for documentation changes (#441)
> **Contributors**
> - @bensabic

### [v0.21.3](https://github.com/vercel-labs/json-render/releases/tag/v0.21.3)
<sub>2026-10-24 · 21d ago</sub>

> **Bug Fixes**
> - **YAML patch state:** Keep move and copy operations in sync with later YAML edits, isolate copied and emitted values, and bound copy growth (#411)
> - **JSON Pointer paths:** Keep path helpers on own properties and dense arrays, ignoring inherited paths and out-of-range array indexes (#411)
> - **Repeated stream operations:** Apply every SpecStream JSONL line, including repeated append operations (#414)
> - **Chat example styling:** Correct Tailwind source paths so chat examples include Streamdown and shadcn styles (#415)
> - **shadcn skill installation:** Rename the skill to `json-render-shadcn` to avoid replacing the official shadcn skill (#417)
> …

### [v0.21.2](https://github.com/vercel-labs/json-render/releases/tag/v0.21.2)
<sub>2026-10-23 · 22d ago</sub>

> **Bug Fixes**
> - **Code generation:** Quote non-identifier object keys and preserve `__proto__` as an own property when serializing props (#407)
> - **Production devtools:** Honor production bundle replacements for `process.env.NODE_ENV` so devtools stay disabled without a browser `process` global (#408)
> - **PDF repeats:** Render repeat containers once, including empty repeats, across server-side PDF output methods (#409)
> - **React registry actions:** Run actions with a no-op setter when no state setter is available (#410)
> **Contributors**
> …

### [v0.21.1](https://github.com/vercel-labs/json-render/releases/tag/v0.21.1)
<sub>2026-10-13 · 1mo ago</sub>

> **Bug Fixes**
> - **Dotted form values:** Preserve literal emails, URLs, and version strings in form value lookups instead of treating them as missing state paths (#353)
> - **Numeric validation:** Reject partially numeric strings such as `"123abc"`, empty strings, and whitespace-only strings instead of accepting them as numbers (#389)
> - **Schema type inference:** Infer `s.any()` fields as `any`, matching `z.any()`, so validated specs remain assignable to `Spec` without casts (#390)
> **Documentation**
> - Migrated the **docs site** to Geistdocs while preserving public URLs, page content, and anchors (#340)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [fix: stop spec replay from mutating message parts (#453)](https://github.com/vercel-labs/json-render/commit/f5c12405a19c45be5e0e90778ef888ed541b208f) | Railly |
| 2026-11-12 | [fix(core): accept numeric strings in min and max validation (#429)](https://github.com/vercel-labs/json-render/commit/5e30a6f9425cd5ffb5038ba44352ab4b1feb3fc7) | lahfir |
| 2026-11-12 | [fix(core): ignore surrounding whitespace in the email validator (#430)](https://github.com/vercel-labs/json-render/commit/1adfc4d6eb9b9d45c6dc58dfb7f2c432a859b4a1) | lahfir |
| 2026-11-12 | [docs(next): fix the quick start to use getPageData (#428)](https://github.com/vercel-labs/json-render/commit/13c9786164139fae424e6449cd36ecea7641fe4d) | lahfir |
| 2026-11-12 | [fix(codegen): emit string props as JSX expressions (#427)](https://github.com/vercel-labs/json-render/commit/41f70a30d70a085209c7ea1b3260fbac5164d9de) | lahfir |
| 2026-11-12 | [fix: reset spec fence state at text block boundaries (#426)](https://github.com/vercel-labs/json-render/commit/2fa9e3f598704864c4517f512a81e6eb7e6fb81f) | lahfir |
| 2026-11-04 | [chore(release): prepare v0.22.0 (#452)](https://github.com/vercel-labs/json-render/commit/18194121c8f087afacd9a8ef65fbda18374ee039) | Railly |
| 2026-11-04 | [feat(chat): add Chat SDK renderer (#451)](https://github.com/vercel-labs/json-render/commit/5074ec58f3b80115b955d0309592b4565a7ca3d8) | Railly |
| 2026-11-02 | [Route feature requests and questions to Discussions](https://github.com/vercel-labs/json-render/commit/1210a3825b7d3980e0978dfaa43d7b0c972ee11a) | ctate |
| 2026-10-30 | [Prepare v0.21.4 release (#446)](https://github.com/vercel-labs/json-render/commit/277df7f26d03e45c490ffb8d11a4dde488c5f289) | ctate |

[See all commits ↗](https://github.com/vercel-labs/json-render/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/json-render.git
```
