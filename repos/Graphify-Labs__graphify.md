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
| ⭐ **Stars** | 153.2k |
| 🍴 **Forks** | 14.7k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/Graphify-Labs/graphify/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `claude-code` `graphrag` `knowledge-graph` `codex` `openclaw` `skills` `antigravity` `gemini` `leiden` `rag` `tree-sitter` `ai-agents` `ast` `code-analysis` `code-search` `cursor` `developer-tools` `llm` `mcp` `graphify` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-04-03 |
| 📦 **Latest release** | [v0.9.120](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.120) — 2026-11-25 |
| 🌿 **Default branch** | `v8` |
| 💾 **Size** | 36.1 MB |
| 🌐 **Website** | graphify.com |

## 📦 Recent releases

### [v0.9.120](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.120)
<sub>2026-11-25 · today</sub>

> A batch of resolution, serve, export, clustering and performance fixes across nine community pull requests. The Python function-local-import change alters node/edge output, so the AST cache schema bumps (55 to 56) and Python re-extracts on the first build after upgrading; the other fixes need no rebuild.
> - Feat: **serve** a new `affected` MCP tool reports the reverse-dependency blast radius of a symbol (what breaks if you change it), and `query_graph` gains an optional `seeds` argument to start a traversal from known nodes; both resolve a node by name, file path, or id the same way the CLI does (#5254, thanks @ArnabOPP; proposed by @ramarro123).
> - Perf: **query** per-node search fields, degrees and the hub threshold, an integer-indexed adjacency for BFS/DFS, and rendered NODE lines are each computed once per loaded graph and reused by every later query, and document frequency is taken through the trigram index; query output is byte-identical (#5476, thanks @nothariharan).
> - Fix: **python** a bare call inside a function whose name is bound by a function-local import (`from m import x`, `import x`) no longer binds to an unrelated same-named module-level definition in the same file; the import shadows the twin within that function only (#5427, thanks @ayushcodes10).
> - Fix: **python** a function-local import no longer leaks its binding into a sibling function at the same scope, so a same-named call elsewhere in the file resolves to its own target rather than the imported one (#5436, thanks @ayushcodes10).
> - Fix: **watch** the watcher test helper replaces the clock in `watch.py` only, instead of patching the process-wide `time.sleep`, which had broken the subprocess waits a rebuild performs and made the watch tests flaky under the parallel suite (#5444, thanks @Deepjyoti-Sarmah).
> …

### [v0.9.119](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.119)
<sub>2026-11-24 · yesterday</sub>

> A fix for a core-install regression in 0.9.118, plus a batch of resolution, extractor, export and performance fixes across ten community pull requests. The Python, Go and COBOL changes alter node/edge output, so the AST cache schema bumps (53 to 55) and those languages re-extract on the first build after upgrading; the other fixes need no rebuild.
> - Fix: **serve** graph commands (`query`, `path`, `explain`, `affected`, `benchmark`) run again on a core install without the `[mcp]` extra. 0.9.118 imported `anyio` (an mcp-extra-only dependency) at the top of `graphify/serve.py`, so loading it raised `ModuleNotFoundError` for those commands; the import is moved back inside the MCP server path where `anyio` is always present (#5320, thanks @Deepjyoti-Sarmah).
> - Fix: **python** a call to a name that a lambda parameter shadows no longer binds to a module-level definition inside the lambda body; the shadow is scoped to the lambda body only, so a genuine outer call elsewhere still resolves (#5417, thanks @melhusl-hs).
> - Fix: **python** a call made through a function parameter (the enclosing function's own parameter, or one captured from an outer function) is likewise no longer bound to a module-level definition of that name; the parameter is a runtime callback whose target is unknown (#5418, thanks @Deepjyoti-Sarmah).
> - Fix: **go** a local variable that shadows an imported package name resolves as a local receiver, not the package, so its member calls bind to the local's type; the shadow is lexically scoped and an unknown local fails closed rather than falling back to a package call (#5409, thanks @sdivyanshu90).
> - Fix: **go** a type declared across sibling files in a package folds to one node per directory even when a same-named package exists elsewhere, so its member calls resolve instead of being dropped as ambiguous; the two same-named packages stay distinct (#5304 follow-up, thanks @PravalVerma).
> …

### [v0.9.118](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.118)
<sub>2026-11-23 · 2d ago</sub>

> A batch of extractor, resolution, serve, export, clustering and reporting fixes across fourteen community pull requests. The Objective-C, C and C# changes alter node/edge output, so the AST cache schema bumps (51 to 53) and the first build after upgrading re-extracts the affected languages; the other fixes need no rebuild.
> - Fix: **csharp** a local, parameter or field named `partial`, `required`, `async`, `nint`, `nuint` or `with` (contextual keywords) that tree-sitter-c-sharp mis-parses where a statement starts with it no longer derails the file; it is rewritten to its verbatim `@name` form before parsing (byte-length preserving), so the enclosing type and the members after it are kept instead of being silently dropped (#5043, thanks @ThatAblaze).
> - Fix: **c** a call through a struct function-pointer field (`ops->run()`, `ops.run()`) no longer fabricates a `calls` edge to a same-named free function; the field name is no evidence of the pointer's runtime target, so the guess is dropped. A plain direct call still resolves (#5410, thanks @sdivyanshu90).
> - Fix: **objc** an Objective-C method whose name folds onto a sibling's id within one `@interface`/`@implementation`/`@protocol` (a leading/trailing `_` as in `-setup`/`-_setup`, or a case-only difference) gets its own salted node id instead of overwriting it; the declaration and definition of one method still share a single node (#5390, thanks @ayushcodes10).
> - Fix: **go** a struct field's owner type is scoped to its own package, so a field of a type whose name is declared in two packages binds to the right one and its member calls resolve instead of being dropped as ambiguous (#5408, thanks @azizur100389).
> - Fix: **extract** a Svelte import that comes through an `export *` barrel now resolves to the real defining module, matching plain `.ts`. The cross-file resolver was masking `.vue` but not `.svelte`, so the Svelte `<script>` imports were lost to a template parse error; chained barrels resolve and ambiguous re-exports fail closed. Run `graphify extract . --force` once to repair an already-cached graph (#5403, thanks @Max17190).
> …

### [v0.9.115](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.115)
<sub>2026-11-21 · 3d ago</sub>

> Security fix for a forced-SMB-authentication issue on Windows (GHSA-g6c9-j4vm-mwq4), plus a batch of extractor, resolution and incremental-update fixes. The extractor fixes that change output share one AST cache schema bump (50 → 51), so the first build after upgrading re-extracts the affected languages.
> **Security**
> - **extract/detect**: indexing a repository no longer stats a corpus-chosen path that resolves outside the scan root. A `.sh` `source`/script-invocation line or a `.git` file naming a UNC `gitdir:`/`commondir` could coerce outbound SMB authentication on Windows (leaking a NetNTLMv2 response) on default offline settings. Probes are now bounded to the scan root and UNC paths are refused before they are resolved (GHSA-g6c9-j4vm-mwq4, thanks @Torch4084).
> **Fixes**
> - **path**: an exact node id resolves before tier matching, so an id is no longer refused as ambiguous (#5367, thanks @Arav-Arun).
> - **python**: a cross-file call through an explicit `from ... import ...` is constrained to the imported name and module (#5229, thanks @Arav-Arun).
> …

### [v0.9.114](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.114) — graphify 0.9.114
<sub>2026-11-20 · 4d ago</sub>

> Performance work on the extract/build/update pipeline, plus a batch of extractor and build fixes. Every entry marked Perf preserves graph output exactly (byte-identical); the extractor fixes change output and share one AST cache schema bump (see the note at the end).
> - Perf: **ids** `normalize_id` gets an ASCII fast-path, pre-compiled regexes and an LRU cache, so the common (ASCII, repeated) identifier case skips the Unicode normalization loop. ~1.26x on the compute path and a large win on repeated ids, which recurs heavily across a corpus.
> - Perf: **cache** `save_cached` builds the portable on-disk payload copy-on-write instead of `copy.deepcopy`-ing every per-file result; ~20% faster on the cache-write transform, scaling with per-file graph size. The input is never mutated and the on-disk bytes are identical.
> - Perf: **extract** each source file is read from disk once (the key hash and the parse share one buffer) instead of twice on a cold build, and the tree-sitter `Parser` is reused per language within a worker instead of rebuilt per file (file reads roughly halved on the worker path).
> - Perf: **extract** the cross-file resolution finalize builds its shared node/edge indexes in a few fused passes instead of ~6 independent full scans of the graph; ~15% faster on the finalize stage.
> - Perf: **watch** the no-change topology comparison uses an order-independent content hash computed in one pass instead of sorting and re-serializing the whole graph; ~1.4x on that compare.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [docs(changelog): correct 0.9.120 PR count (eight -> nine)](https://github.com/Graphify-Labs/graphify/commit/02c27dc246cd7bc359d0f4acaf53a3fce595bc1e) | safishamsi |
| 2026-11-25 | [chore(release): 0.9.120 — schema 56, eight community PRs](https://github.com/Graphify-Labs/graphify/commit/16127eb30892f997d758efdd894e5e04264edbbb) | safishamsi |
| 2026-11-25 | [perf(serve): compute document frequency through the trigram index](https://github.com/Graphify-Labs/graphify/commit/626dd601c15d67de7991d1a4c893bea4c0ae3268) | nothariharan |
| 2026-11-25 | [fix(serve): drop structure caches inherited by the traversal view](https://github.com/Graphify-Labs/graphify/commit/7df2eeed453bbc500481533d8255e01faa45a849) | nothariharan |
| 2026-11-25 | [perf(serve): render NODE lines once and skip unreachable EDGE lines](https://github.com/Graphify-Labs/graphify/commit/98cabf2809d9b0a46e64a264136873b82be7ebf3) | nothariharan |
| 2026-11-25 | [perf(serve): walk BFS/DFS on integer-indexed adjacency](https://github.com/Graphify-Labs/graphify/commit/99e14849e21c4c35056af133b20a99646cd17f76) | nothariharan |
| 2026-11-25 | [perf(serve): cache degrees and the hub threshold per graph](https://github.com/Graphify-Labs/graphify/commit/0a09c8670094592b0683fffb022f5557ce4c7c67) | nothariharan |
| 2026-11-25 | [perf(serve): precompute per-node query fields once per graph](https://github.com/Graphify-Labs/graphify/commit/8624fb7a8189b1857927f2a430f3a7be78638594) | nothariharan |
| 2026-11-25 | [fix(python): stop a function local import leaking into a sibling call](https://github.com/Graphify-Labs/graphify/commit/640a7abd25a1874bc8368532e3ba318660f2cdd8) | ayushcodes10 |
| 2026-11-25 | [fix(python): stop a function local import call binding to a same file…](https://github.com/Graphify-Labs/graphify/commit/db57319819982cd39b96d51d5d02bd4d871775bc) | ayushcodes10 |

[See all commits ↗](https://github.com/Graphify-Labs/graphify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Graphify-Labs/graphify.git
```
