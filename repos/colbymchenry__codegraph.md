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
| ⭐ **Stars** | 78.3k |
| 🍴 **Forks** | 5.2k |
| 🐞 **Open issues + PRs** | [232](https://github.com/colbymchenry/codegraph/issues) |
| 💻 **Languages** | TypeScript 90% · Rust 5% · Svelte 2% · JavaScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-01-18 |
| 📦 **Latest release** | [v1.6.4](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.4) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 58.1 MB |
| 🌐 **Website** | https://colbymchenry.github.io/codegraph/ |

## 📦 Recent releases

### [v1.6.4](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.4)
<sub>2026-11-20 · yesterday</sub>

> **[1.6.4] - 2026-11-20**
> **Highlights**
> - **Small questions cost less.** Ask your agent what a function or constant is, or who calls it, and `codegraph_explore` now answers with the definition and every line that uses it, instead of a long answer about related files.
> - **Faster answers in Claude Code.** The prompt hook now asks the CodeGraph server already running for your project instead of loading the index again on every prompt, which matters most in large projects, and `codegraph impact` is as fast as it was in 1.6.2 again.
> - **Safer on a shared computer.** Each agent session now checks that the background server it connects to runs as you before sending it anything.
> - **More of your code in the graph.** Elysia (Bun) routes, PHP includes built from the web server's root or the file's own folder, Dart 3.13 primary constructors and newer Kotlin syntax are now read, and ASP.NET Core routes are named the way ASP.NET serves them.
> …

### [v1.6.3](https://github.com/colbymchenry/codegraph/releases/tag/v1.6.3)
<sub>2026-11-17 · 4d ago</sub>

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
<sub>2026-08-26 · 2mo ago</sub>

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
| 2026-11-20 | [docs(changelog): promote [Unreleased] into [1.6.4]](https://github.com/colbymchenry/codegraph/commit/461a5d87a873a4932997cd9a49042ab30e45a675) | github-actions[bot] |
| 2026-11-20 | [docs(site): document what 1.6.4 adds (#3425)](https://github.com/colbymchenry/codegraph/commit/b4392571214f0ac1177d352abbb394c6aaf6df8c) | colbymchenry |
| 2026-11-20 | [docs: the one-symbol explore answer in the README, and a command name…](https://github.com/colbymchenry/codegraph/commit/20d6e93854b040cb9da68c8a536e4d318ccfe983) | colbymchenry |
| 2026-11-20 | [release: 1.6.4 (#3424)](https://github.com/colbymchenry/codegraph/commit/ee73cec63bbb79cd3db6b380308bf07d5e04d639) | colbymchenry |
| 2026-11-20 | [feat(explore): answer a one-symbol question with its definition and e…](https://github.com/colbymchenry/codegraph/commit/337a41f50bef48f5b8f3330cbfa1342098d3b382) | colbymchenry |
| 2026-11-19 | [fix(kotlin): read calls named after a modifier keyword, on a newer gr…](https://github.com/colbymchenry/codegraph/commit/69bbb389780410f43de7b514b90b2f7ba6b12584) | colbymchenry |
| 2026-11-19 | [feat(php): work out the web root from the project's own includes when…](https://github.com/colbymchenry/codegraph/commit/eb992b5257611793f54cf47806dbfbd00114240e) | colbymchenry |
| 2026-11-19 | [feat(php): link includes built from $_SERVER['DOCUMENT_ROOT'] under a…](https://github.com/colbymchenry/codegraph/commit/67178d8f42469995bbba9ec760207efd30dfa696) | colbymchenry |
| 2026-11-19 | [chore(extraction): bump EXTRACTION_VERSION to 29 (#3411)](https://github.com/colbymchenry/codegraph/commit/1f1bfaafaed7cd2e9007d45436c4810375654889) | colbymchenry |
| 2026-11-19 | [fix(dart): index classes with Dart 3.13 primary constructors, on a ne…](https://github.com/colbymchenry/codegraph/commit/9f0ed70428f6a6547f8b102f452568aed56ef296) | colbymchenry |

[See all commits ↗](https://github.com/colbymchenry/codegraph/commits)

## ⬇️ Get it

```bash
git clone https://github.com/colbymchenry/codegraph.git
```
