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
| ⭐ **Stars** | 19.8k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [129](https://github.com/vercel-labs/json-render/issues) |
| 💻 **Languages** | TypeScript 71% · Swift 12% · MDX 11% · Svelte 4% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-16 (yesterday) |
| 📅 **Created** | 2026-01-14 |
| 📦 **Latest release** | [v0.23.1](https://github.com/vercel-labs/json-render/releases/tag/v0.23.1) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 7.9 MB |
| 🌐 **Website** | https://json-render.dev |

## 📦 Recent releases

### [v0.23.1](https://github.com/vercel-labs/json-render/releases/tag/v0.23.1)
<sub>2026-11-16 · yesterday</sub>

> **Bug Fixes**
> - **Swift render tree limits:** Bound the child ids a build holds, so a spec that lists the same child many times with a long state value stops at a limit instead of holding a copy of that value once per child. Bound the issues the validator reports and the message bytes they hold, and end a shortened result with one `specTooComplex` issue that keeps its severity, so a spec whose only dropped issues were warnings stays valid (#477)
> **Improvements**
> - **Swift package installation:** Made the repository root a Swift package, so Xcode and SwiftPM can add `JSONRender` by URL from 0.23.1 on, with the `JSONRenderCore`, `JSONRenderSwiftUI`, and `JSONRenderCatalog` products. The nested package at `swift/JSONRender` remains for local checkouts (#478)
> **Contributors**
> - @ctate

### [v0.23.0](https://github.com/vercel-labs/json-render/releases/tag/v0.23.0)
<sub>2026-11-15 · yesterday</sub>

> **New Features**
> - **Swift package and SwiftUI renderer:** Added a `JSONRender` Swift package with a `JSONRenderCore` model for specs, streaming, state, expressions, actions, visibility, and validation, a `JSONRenderSwiftUI` renderer with built-in views, a native catalog, and macOS and streaming example apps. Conformance fixtures compare the Swift render tree with the React renderer, and CI builds and tests the package (#470)
> **Bug Fixes**
> - **Spec replay:** Deep-copy message parts before replaying so repeated replays no longer mutate the parts or duplicate state items and children in React, Vue, Solid, Svelte, and Devtools. Devtools also skips malformed spec parts instead of crashing (#453)
> - **Spec fences:** Reset unfinished spec fences at text block boundaries so prose after an interrupted fence is no longer dropped by the core and YAML transforms (#426)
> - **Code generation:** Emit string props as JSX expressions so quotes, backslashes, and newlines survive code export (#427)
> …

### [v0.22.0](https://github.com/vercel-labs/json-render/releases/tag/v0.22.0)
<sub>2026-11-04 · 12d ago</sub>

> **New Features**
> - **Chat SDK renderer:** Added `@json-render/chat` to render specs as Chat SDK cards, so one catalog posts natively on Slack, Teams, and the other Chat SDK platforms. `streamCard` streams a card into a thread and edits it as elements arrive, and `toCard` validates specs against per-component schemas and optional platform limits. State expressions, `visible`, and `repeat` resolve against `spec.state` (#451)
> - **Chat SDK example:** Added a playground that previews generated messages as Slack renders them, with a Teams Adaptive Card view and a copy button for Block Kit Builder (#451)
> **Contributors**
> - @Railly

### [v0.21.4](https://github.com/vercel-labs/json-render/releases/tag/v0.21.4)
<sub>2026-11-01 · 15d ago</sub>

> **Documentation**
> - Added the **eve TanStack Agent template** to the examples page, with links to its source repository and Vercel template (#442)
> - Added shared **technical writing guidance** for documentation changes (#441)
> **Contributors**
> - @bensabic

### [v0.21.3](https://github.com/vercel-labs/json-render/releases/tag/v0.21.3)
<sub>2026-10-24 · 24d ago</sub>

> **Bug Fixes**
> - **YAML patch state:** Keep move and copy operations in sync with later YAML edits, isolate copied and emitted values, and bound copy growth (#411)
> - **JSON Pointer paths:** Keep path helpers on own properties and dense arrays, ignoring inherited paths and out-of-range array indexes (#411)
> - **Repeated stream operations:** Apply every SpecStream JSONL line, including repeated append operations (#414)
> - **Chat example styling:** Correct Tailwind source paths so chat examples include Streamdown and shadcn styles (#415)
> - **shadcn skill installation:** Rename the skill to `json-render-shadcn` to avoid replacing the official shadcn skill (#417)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [Prepare v0.23.1 release (#479)](https://github.com/vercel-labs/json-render/commit/5e99a387536a1528d8113eb929ab4b7e611701ae) | ctate |
| 2026-11-15 | [fix(swift): bound rendered child ids and validation issue output (#477)](https://github.com/vercel-labs/json-render/commit/b72f44772820f797193d6a82f7c309646a4ad254) | ctate |
| 2026-11-15 | [Make the repository root a Swift package (#478)](https://github.com/vercel-labs/json-render/commit/d3648df4214c4f6bf707f512c47d5d9f370261ea) | ctate |
| 2026-11-15 | [Prepare v0.23.0 release (#476)](https://github.com/vercel-labs/json-render/commit/6e19a593af4847b9a21c22c1849d050c21708048) | ctate |
| 2026-11-15 | [Add a Swift package and SwiftUI renderer (#470)](https://github.com/vercel-labs/json-render/commit/229be36d40199b30a2e1d770bc4cb6e8e02b513c) | ctate |
| 2026-11-13 | [fix: stop spec replay from mutating message parts (#453)](https://github.com/vercel-labs/json-render/commit/f5c12405a19c45be5e0e90778ef888ed541b208f) | Railly |
| 2026-11-12 | [fix(core): accept numeric strings in min and max validation (#429)](https://github.com/vercel-labs/json-render/commit/5e30a6f9425cd5ffb5038ba44352ab4b1feb3fc7) | lahfir |
| 2026-11-12 | [fix(core): ignore surrounding whitespace in the email validator (#430)](https://github.com/vercel-labs/json-render/commit/1adfc4d6eb9b9d45c6dc58dfb7f2c432a859b4a1) | lahfir |
| 2026-11-12 | [docs(next): fix the quick start to use getPageData (#428)](https://github.com/vercel-labs/json-render/commit/13c9786164139fae424e6449cd36ecea7641fe4d) | lahfir |
| 2026-11-12 | [fix(codegen): emit string props as JSX expressions (#427)](https://github.com/vercel-labs/json-render/commit/41f70a30d70a085209c7ea1b3260fbac5164d9de) | lahfir |

[See all commits ↗](https://github.com/vercel-labs/json-render/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/json-render.git
```
