# Graphify-Labs/graphify

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Graphify-Labs/graphify)

> Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | TCOS |
| **Why it's worth a look** | Turn a codebase + docs + schemas into a queryable knowledge graph |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 154.1k |
| 🍴 **Forks** | 14.8k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/Graphify-Labs/graphify/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `claude-code` `graphrag` `knowledge-graph` `codex` `openclaw` `skills` `antigravity` `gemini` `leiden` `rag` `tree-sitter` `ai-agents` `ast` `code-analysis` `code-search` `cursor` `developer-tools` `llm` `mcp` `graphify` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-04-03 |
| 📦 **Latest release** | [v0.9.121](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.121) — 2026-11-26 |
| 🌿 **Default branch** | `v8` |
| 💾 **Size** | 36.4 MB |
| 🌐 **Website** | graphify.com |

## 📦 Recent releases

### [v0.9.121](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.121)
<sub>2026-11-26 · today</sub>

> A large batch across community pull requests: extractor accuracy (C#, TypeScript, Rust, COBOL, Python), node-id and edge correctness on incremental rebuilds, a self-contained Canvas renderer for large graphs, and a wave of byte-identical performance work. The C#, TypeScript, Rust, COBOL and Python changes alter node/edge output, so the AST cache schema bumps (56 to 57) and those languages re-extract on the first build after upgrading; everything else needs no rebuild.
> **Features**
> - **serve/viz** `graph.html` gains a self-contained Canvas 2D renderer for large graphs: above the vis-network comfort threshold (and within `--node-limit`/`GRAPHIFY_VIZ_NODE_LIMIT`) it emits a deterministic, community-packed Canvas view with viewport culling and sparse labels at low zoom, embedded as a base64 payload with no external scripts. Small graphs keep the existing vis-network output (#5521, thanks @GwungTz).
> **Extractor fixes**
> - **csharp** a call through a namespace-qualified receiver (`Acme.Audio.Mixer.Instance.Play()`, `Acme.Audio.Mixer.Reset()`, or a `var m = Acme.Audio.Mixer.Instance; m.Play()` chain, plus null-conditional forms) resolves through the named type the same way the short name under `using` already did, binding the exact namespace and failing closed on an unknown or ambiguous path (#5473, thanks @aliyapici).
> - **typescript** a named object type alias (`type Port = { read(): number }`, including an unqualified `Readonly<{...}>`) retains its method signatures as method nodes so a typed-receiver call resolves to them, while the signatures stay out of bare-call, static-call and module-symbol lookup (#5455, thanks @rvitaliy).
> …

### [v0.9.120](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.120)
<sub>2026-11-25 · 2d ago</sub>

> A batch of resolution, serve, export, clustering and performance fixes across nine community pull requests. The Python function-local-import change alters node/edge output, so the AST cache schema bumps (55 to 56) and Python re-extracts on the first build after upgrading; the other fixes need no rebuild.
> - Feat: **serve** a new `affected` MCP tool reports the reverse-dependency blast radius of a symbol (what breaks if you change it), and `query_graph` gains an optional `seeds` argument to start a traversal from known nodes; both resolve a node by name, file path, or id the same way the CLI does (#5254, thanks @ArnabOPP; proposed by @ramarro123).
> - Perf: **query** per-node search fields, degrees and the hub threshold, an integer-indexed adjacency for BFS/DFS, and rendered NODE lines are each computed once per loaded graph and reused by every later query, and document frequency is taken through the trigram index; query output is byte-identical (#5476, thanks @nothariharan).
> - Fix: **python** a bare call inside a function whose name is bound by a function-local import (`from m import x`, `import x`) no longer binds to an unrelated same-named module-level definition in the same file; the import shadows the twin within that function only (#5427, thanks @ayushcodes10).
> - Fix: **python** a function-local import no longer leaks its binding into a sibling function at the same scope, so a same-named call elsewhere in the file resolves to its own target rather than the imported one (#5436, thanks @ayushcodes10).
> - Fix: **watch** the watcher test helper replaces the clock in `watch.py` only, instead of patching the process-wide `time.sleep`, which had broken the subprocess waits a rebuild performs and made the watch tests flaky under the parallel suite (#5444, thanks @Deepjyoti-Sarmah).
> …

### [v0.9.119](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.119)
<sub>2026-11-24 · 2d ago</sub>

> A fix for a core-install regression in 0.9.118, plus a batch of resolution, extractor, export and performance fixes across ten community pull requests. The Python, Go and COBOL changes alter node/edge output, so the AST cache schema bumps (53 to 55) and those languages re-extract on the first build after upgrading; the other fixes need no rebuild.
> - Fix: **serve** graph commands (`query`, `path`, `explain`, `affected`, `benchmark`) run again on a core install without the `[mcp]` extra. 0.9.118 imported `anyio` (an mcp-extra-only dependency) at the top of `graphify/serve.py`, so loading it raised `ModuleNotFoundError` for those commands; the import is moved back inside the MCP server path where `anyio` is always present (#5320, thanks @Deepjyoti-Sarmah).
> - Fix: **python** a call to a name that a lambda parameter shadows no longer binds to a module-level definition inside the lambda body; the shadow is scoped to the lambda body only, so a genuine outer call elsewhere still resolves (#5417, thanks @melhusl-hs).
> - Fix: **python** a call made through a function parameter (the enclosing function's own parameter, or one captured from an outer function) is likewise no longer bound to a module-level definition of that name; the parameter is a runtime callback whose target is unknown (#5418, thanks @Deepjyoti-Sarmah).
> - Fix: **go** a local variable that shadows an imported package name resolves as a local receiver, not the package, so its member calls bind to the local's type; the shadow is lexically scoped and an unknown local fails closed rather than falling back to a package call (#5409, thanks @sdivyanshu90).
> - Fix: **go** a type declared across sibling files in a package folds to one node per directory even when a same-named package exists elsewhere, so its member calls resolve instead of being dropped as ambiguous; the two same-named packages stay distinct (#5304 follow-up, thanks @PravalVerma).
> …

### [v0.9.118](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.118)
<sub>2026-11-23 · 4d ago</sub>

> A batch of extractor, resolution, serve, export, clustering and reporting fixes across fourteen community pull requests. The Objective-C, C and C# changes alter node/edge output, so the AST cache schema bumps (51 to 53) and the first build after upgrading re-extracts the affected languages; the other fixes need no rebuild.
> - Fix: **csharp** a local, parameter or field named `partial`, `required`, `async`, `nint`, `nuint` or `with` (contextual keywords) that tree-sitter-c-sharp mis-parses where a statement starts with it no longer derails the file; it is rewritten to its verbatim `@name` form before parsing (byte-length preserving), so the enclosing type and the members after it are kept instead of being silently dropped (#5043, thanks @ThatAblaze).
> - Fix: **c** a call through a struct function-pointer field (`ops->run()`, `ops.run()`) no longer fabricates a `calls` edge to a same-named free function; the field name is no evidence of the pointer's runtime target, so the guess is dropped. A plain direct call still resolves (#5410, thanks @sdivyanshu90).
> - Fix: **objc** an Objective-C method whose name folds onto a sibling's id within one `@interface`/`@implementation`/`@protocol` (a leading/trailing `_` as in `-setup`/`-_setup`, or a case-only difference) gets its own salted node id instead of overwriting it; the declaration and definition of one method still share a single node (#5390, thanks @ayushcodes10).
> - Fix: **go** a struct field's owner type is scoped to its own package, so a field of a type whose name is declared in two packages binds to the right one and its member calls resolve instead of being dropped as ambiguous (#5408, thanks @azizur100389).
> - Fix: **extract** a Svelte import that comes through an `export *` barrel now resolves to the real defining module, matching plain `.ts`. The cross-file resolver was masking `.vue` but not `.svelte`, so the Svelte `<script>` imports were lost to a template parse error; chained barrels resolve and ambiguous re-exports fail closed. Run `graphify extract . --force` once to repair an already-cached graph (#5403, thanks @Max17190).
> …

### [v0.9.115](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.115)
<sub>2026-11-21 · 5d ago</sub>

> Security fix for a forced-SMB-authentication issue on Windows (GHSA-g6c9-j4vm-mwq4), plus a batch of extractor, resolution and incremental-update fixes. The extractor fixes that change output share one AST cache schema bump (50 → 51), so the first build after upgrading re-extracts the affected languages.
> **Security**
> - **extract/detect**: indexing a repository no longer stats a corpus-chosen path that resolves outside the scan root. A `.sh` `source`/script-invocation line or a `.git` file naming a UNC `gitdir:`/`commondir` could coerce outbound SMB authentication on Windows (leaking a NetNTLMv2 response) on default offline settings. Probes are now bounded to the scan root and UNC paths are refused before they are resolved (GHSA-g6c9-j4vm-mwq4, thanks @Torch4084).
> **Fixes**
> - **path**: an exact node id resolves before tier matching, so an id is no longer refused as ambiguous (#5367, thanks @Arav-Arun).
> - **python**: a cross-file call through an explicit `from ... import ...` is constrained to the imported name and module (#5229, thanks @Arav-Arun).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Merge pull request #5523 from SyedFahad7/readme-graphify-name](https://github.com/Graphify-Labs/graphify/commit/0f22ae762e3e3d0b689fc7ad2b8192740628413b) | safishamsi |
| 2026-11-26 | [use plain graphify in the mcp section of the readme](https://github.com/Graphify-Labs/graphify/commit/dfeb271a6b77bcc359d760956adf8b2383e6b9a7) | SyedFahad7 |
| 2026-11-26 | [Merge pull request #5522 from SyedFahad7/readme-website-link](https://github.com/Graphify-Labs/graphify/commit/87cd9bdef7720605601da031a752605363fadb0f) | safishamsi |
| 2026-11-26 | [use plain graphify for the hosted product in the readme](https://github.com/Graphify-Labs/graphify/commit/f1c000044eaba4bab7cdfd38eccb6a5aa767c77d) | SyedFahad7 |
| 2026-11-26 | [add a graphify.com link at the top of the readme](https://github.com/Graphify-Labs/graphify/commit/f12287aaaee35e9f390e4ba129ed8efc9ddaed55) | SyedFahad7 |
| 2026-11-26 | [chore(release): 0.9.121 — schema 57, ~27 community PRs](https://github.com/Graphify-Labs/graphify/commit/6f2359fe67983a653207b2b4f8377d1d59fc90e1) | safishamsi |
| 2026-11-26 | [chore(schema): fold Rust #5398 and COBOL #5424/#5425/#5426 into schem…](https://github.com/Graphify-Labs/graphify/commit/78cab0b77b24e299252e5770012f60297393af5d) | safishamsi |
| 2026-11-26 | [test(5398): expect the module node for a Rust wildcard use](https://github.com/Graphify-Labs/graphify/commit/5db50ae78fc9783e974cb0efa15e4d35b7dea728) | Deepjyoti-Sarmah |
| 2026-11-26 | [test(5398): pin Rust module-path import resolution](https://github.com/Graphify-Labs/graphify/commit/178938abbb05fbdc206aab65e15ac75243c58f84) | Deepjyoti-Sarmah |
| 2026-11-26 | [fix(5398): resolve Rust module imports for plain and grouped use](https://github.com/Graphify-Labs/graphify/commit/2f6e4b6b1cbb256ec7fba1a766a4f20d6a7f52a2) | Deepjyoti-Sarmah |

[See all commits ↗](https://github.com/Graphify-Labs/graphify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Graphify-Labs/graphify.git
```
