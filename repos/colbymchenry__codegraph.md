# colbymchenry/codegraph

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/colbymchenry/codegraph)

> Pre-indexed code knowledge graph, auto syncs on code changes, for Claude Code, Codex, Gemini, Cursor, OpenCode, AntiGravity, Kiro, CoPilot, and Hermes Agent — fewer tokens, fewer tool calls, 100% local

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | TCOS |
| **Why it's worth a look** | Pre-indexed code knowledge graph that auto-syncs for coding agents |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 78.8k |
| 🍴 **Forks** | 5.3k |
| 🐞 **Open issues + PRs** | [259](https://github.com/colbymchenry/codegraph/issues) |
| 💻 **Languages** | TypeScript 90% · Rust 5% · Svelte 2% · JavaScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-23 (2d ago) |
| 📅 **Created** | 2026-01-18 |
| 📦 **Latest release** | [v1.6.4](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.4) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 59.1 MB |
| 🌐 **Website** | https://colbymchenry.github.io/codegraph/ |

## 📦 Recent releases

### [v1.6.4](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.4)
<sub>2026-11-20 · 6d ago</sub>

> **[1.6.4] - 2026-11-20**
> **Highlights**
> - **Small questions cost less.** Ask your agent what a function or constant is, or who calls it, and `codegraph_explore` now answers with the definition and every line that uses it, instead of a long answer about related files.
> - **Faster answers in Claude Code.** The prompt hook now asks the CodeGraph server already running for your project instead of loading the index again on every prompt, which matters most in large projects, and `codegraph impact` is as fast as it was in 1.6.2 again.
> - **Safer on a shared computer.** Each agent session now checks that the background server it connects to runs as you before sending it anything.
> - **More of your code in the graph.** Elysia (Bun) routes, PHP includes built from the web server's root or the file's own folder, Dart 3.13 primary constructors and newer Kotlin syntax are now read, and ASP.NET Core routes are named the way ASP.NET serves them.
> …

### [v1.6.3](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.3)
<sub>2026-11-17 · 8d ago</sub>

> **[1.6.3] - 2026-11-17**
> **Highlights**
> - **Nine more agents and editors.** `codegraph install` now sets up IBM Bob, Factory Droid, Windsurf, Qwen Code, DeepSeek Harness, Grok Build, Kimi Code, the Qoder CLI and Pi.
> - **Security fixes.** A sensitive folder such as `~/.ssh` can no longer be opened as a project through a link, a junction or another spelling of its path, and the bundled Node.js moves to 24.22.1, which fixes CVE-2026-111497.
> - **More accurate links in every language.** Hundreds of fixes help calls, imports and types reach the code they mean, most of all in JavaScript and TypeScript, Go, C and C++, Rust, Python, C#, Java and Dart. Tauri, CodeIgniter 3, Drupal services and plugins, Next.js middleware and MediatR handlers are now covered too.
> - **Better answers for your agent.** `codegraph_explore` no longer stalls on a large project, answers a pasted log or file in seconds, finds code named in Chinese, Japanese or Korean, and its Flow reaches every symbol your query names.
> …

### [v1.6.2](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.2)
<sub>2026-10-03 · 1mo ago</sub>

> **[1.6.2] - 2026-10-03**
> **Highlights**
> - **Far fewer wrong links, in every language.** A call, import or type now resolves the way its language scopes names — through imports, packages, namespaces and the class it is written in — so it stops landing on an unrelated symbol that only shares its name. This covers TypeScript and JavaScript, Python, Java, Kotlin, Scala, C#, VB.NET, Swift, Objective-C, Go, Rust, C and C++, PHP, Ruby, Dart, Lua, R and more, and makes callers, impact and `codegraph_explore` answers more trustworthy.
> - **Overloads, `super` and recursion resolve correctly.** A call reaches the overload its arguments fit, a `super` call reaches the parent's method, and a method that calls another overload, or another object's method of the same name, no longer looks like it calls itself.
> - **Routes for more frameworks.** Angular (including Nx libraries), Vue Router admin apps, Rails nested routes, Flask's `add_url_rule`, ASP.NET FastEndpoints, Play subprojects, Vapor closure routes and Expo Router API routes are found. NestJS and Laravel routes are named by the path a request actually takes, and a Spring or Laravel test that calls a route by URL counts as covering it.
> - **More of your code in the graph.** Vue Options API components, Java and Kotlin enum constants with bodies, Flow-typed JavaScript, Kotlin infix calls, React Native native views and events, Expo modules, tag-based CFML and Delphi `.inc` files are all indexed now.
> …

### [v1.6.1](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.1)
<sub>2026-09-29 · 1mo ago</sub>

> **[1.6.1] - 2026-09-29**
> **Highlights**
> - **Sharper answers from `codegraph_explore`.** It returns the functions and methods you name — even from a very large file, or one full of same-named overrides — honours line numbers in a query, and says when it shortened an answer instead of calling it complete.
> - **Your app's navigation and requests are in the graph.** Expo Router, Next.js, React Router, TanStack Router, Vue Router / Nuxt and SvelteKit pages and the links between them are routes and `navigates` edges, and a page's `fetch` reaches the route that serves it, so "where does this go" and "what calls this endpoint" are one question to `codegraph_explore`.
> - **Explore says when a call happens.** Each hop in `codegraph_explore`'s Flow section carries the condition it runs under, for JavaScript, TypeScript, Swift, Python, Java, Kotlin, C#, Go and C.
> - **Fewer wrong links.** Many fixes to how calls, imports and inheritance resolve in TypeScript, JavaScript, Python, Java, Kotlin, Go, Rust, Scala, PHP and C/C++, so a call stops landing on an unrelated symbol that happens to share its name.
> …

### [v1.6.0](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.0)
<sub>2026-08-26 · 3mo ago</sub>

> **[1.6.0] - 2026-08-26**
> **Highlights**
> - **GitHub Copilot is now supported** — `codegraph install` sets it up in VS Code, the Copilot CLI, and JetBrains IDEs, next to the agents it already knew.
> - **Set up in one command** — `codegraph install --yes --init` wires up your agents and indexes your project with no prompts, ideal for a fresh container or CI.
> - **Better answers for your agent** — `codegraph_explore` no longer repeats code it already showed you, always brings back the files and symbols you asked for by name, and spends its space on the code that actually answers the question rather than look-alikes, generated files, and type shims.
> - **Your graph stays right as you keep coding** — a long-running index no longer drifts from a fresh one, and edits to `codegraph.json` (such as `exclude`) apply immediately without a restart.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(pascal): a routine whose {$ifdef} branches each open a block ends…](https://github.com/colbymchenry/codegraph/commit/73c6cff66e525a92bff65675b6b0c46687e91ef1) | colbymchenry |
| 2026-11-23 | [fix(pascal): an inherited call links the ancestor method it runs (#3477)](https://github.com/colbymchenry/codegraph/commit/b9285eb7bf0c327e5f712bc50abbc50e7df64a82) | colbymchenry |
| 2026-11-23 | [fix(pascal): a bare call links what its scope declares, across a unit…](https://github.com/colbymchenry/codegraph/commit/f4c37e4e9c90cefb5ca56e98ce3b31ae00c28921) | colbymchenry |
| 2026-11-23 | [fix(pascal): index class and record helpers as types with methods (#3…](https://github.com/colbymchenry/codegraph/commit/7fbc66b7e25b50760b3cbe65703eea6d99e2e39e) | colbymchenry |
| 2026-11-23 | [fix(kotlin): a class implements the interface it delegates `by`; supe…](https://github.com/colbymchenry/codegraph/commit/0442e322efea69efb056f337315896d9806c8bf7) | colbymchenry |
| 2026-11-23 | [fix(pascal): a bare call links only what its scope declares, a with s…](https://github.com/colbymchenry/codegraph/commit/8763586ce06e8be2a0723a7713eac1565a7ace9e) | colbymchenry |
| 2026-11-23 | [perf(resolution): start the resolver pool sooner near the gate, and i…](https://github.com/colbymchenry/codegraph/commit/103782193328e2eef5692eac3f4cbecf9adcffd0) | colbymchenry |
| 2026-11-23 | [fix(kotlin): calls written in a bodied class's header link from the c…](https://github.com/colbymchenry/codegraph/commit/358c2734a7ab9b21cafcd9537fd7fc898eac14b1) | colbymchenry |
| 2026-11-23 | [fix(pascal): calls reach the overload their arguments fit; more imple…](https://github.com/colbymchenry/codegraph/commit/f5a2cd737fd3d52e3224f1fd61913c13fafc3a20) | colbymchenry |
| 2026-11-23 | [fix(pascal): show implementation bodies for declared routines (#3453)…](https://github.com/colbymchenry/codegraph/commit/06803b28abb40dd36dfc81fa10d573abac98aca5) | yang0228 |

[See all commits ↗](https://github.com/colbymchenry/codegraph/commits)

## ⬇️ Get it

```bash
git clone https://github.com/colbymchenry/codegraph.git
```
