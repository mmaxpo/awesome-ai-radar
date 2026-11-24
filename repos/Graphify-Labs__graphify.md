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
| ⭐ **Stars** | 152.8k |
| 🍴 **Forks** | 14.7k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/Graphify-Labs/graphify/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `claude-code` `graphrag` `knowledge-graph` `codex` `openclaw` `skills` `antigravity` `gemini` `leiden` `rag` `tree-sitter` `ai-agents` `ast` `code-analysis` `code-search` `cursor` `developer-tools` `llm` `mcp` `graphify` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-04-03 |
| 📦 **Latest release** | [v0.9.119](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.119) — 2026-11-24 |
| 🌿 **Default branch** | `v8` |
| 💾 **Size** | 36.0 MB |
| 🌐 **Website** | graphify.com |

## 📦 Recent releases

### [v0.9.119](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.119)
<sub>2026-11-24 · today</sub>

> A fix for a core-install regression in 0.9.118, plus a batch of resolution, extractor, export and performance fixes across ten community pull requests. The Python, Go and COBOL changes alter node/edge output, so the AST cache schema bumps (53 to 55) and those languages re-extract on the first build after upgrading; the other fixes need no rebuild.
> - Fix: **serve** graph commands (`query`, `path`, `explain`, `affected`, `benchmark`) run again on a core install without the `[mcp]` extra. 0.9.118 imported `anyio` (an mcp-extra-only dependency) at the top of `graphify/serve.py`, so loading it raised `ModuleNotFoundError` for those commands; the import is moved back inside the MCP server path where `anyio` is always present (#5320, thanks @Deepjyoti-Sarmah).
> - Fix: **python** a call to a name that a lambda parameter shadows no longer binds to a module-level definition inside the lambda body; the shadow is scoped to the lambda body only, so a genuine outer call elsewhere still resolves (#5417, thanks @melhusl-hs).
> - Fix: **python** a call made through a function parameter (the enclosing function's own parameter, or one captured from an outer function) is likewise no longer bound to a module-level definition of that name; the parameter is a runtime callback whose target is unknown (#5418, thanks @Deepjyoti-Sarmah).
> - Fix: **go** a local variable that shadows an imported package name resolves as a local receiver, not the package, so its member calls bind to the local's type; the shadow is lexically scoped and an unknown local fails closed rather than falling back to a package call (#5409, thanks @sdivyanshu90).
> - Fix: **go** a type declared across sibling files in a package folds to one node per directory even when a same-named package exists elsewhere, so its member calls resolve instead of being dropped as ambiguous; the two same-named packages stay distinct (#5304 follow-up, thanks @PravalVerma).
> …

### [v0.9.118](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.118)
<sub>2026-11-23 · yesterday</sub>

> A batch of extractor, resolution, serve, export, clustering and reporting fixes across fourteen community pull requests. The Objective-C, C and C# changes alter node/edge output, so the AST cache schema bumps (51 to 53) and the first build after upgrading re-extracts the affected languages; the other fixes need no rebuild.
> - Fix: **csharp** a local, parameter or field named `partial`, `required`, `async`, `nint`, `nuint` or `with` (contextual keywords) that tree-sitter-c-sharp mis-parses where a statement starts with it no longer derails the file; it is rewritten to its verbatim `@name` form before parsing (byte-length preserving), so the enclosing type and the members after it are kept instead of being silently dropped (#5043, thanks @ThatAblaze).
> - Fix: **c** a call through a struct function-pointer field (`ops->run()`, `ops.run()`) no longer fabricates a `calls` edge to a same-named free function; the field name is no evidence of the pointer's runtime target, so the guess is dropped. A plain direct call still resolves (#5410, thanks @sdivyanshu90).
> - Fix: **objc** an Objective-C method whose name folds onto a sibling's id within one `@interface`/`@implementation`/`@protocol` (a leading/trailing `_` as in `-setup`/`-_setup`, or a case-only difference) gets its own salted node id instead of overwriting it; the declaration and definition of one method still share a single node (#5390, thanks @ayushcodes10).
> - Fix: **go** a struct field's owner type is scoped to its own package, so a field of a type whose name is declared in two packages binds to the right one and its member calls resolve instead of being dropped as ambiguous (#5408, thanks @azizur100389).
> - Fix: **extract** a Svelte import that comes through an `export *` barrel now resolves to the real defining module, matching plain `.ts`. The cross-file resolver was masking `.vue` but not `.svelte`, so the Svelte `<script>` imports were lost to a template parse error; chained barrels resolve and ambiguous re-exports fail closed. Run `graphify extract . --force` once to repair an already-cached graph (#5403, thanks @Max17190).
> …

### [v0.9.115](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.115)
<sub>2026-11-21 · 2d ago</sub>

> Security fix for a forced-SMB-authentication issue on Windows (GHSA-g6c9-j4vm-mwq4), plus a batch of extractor, resolution and incremental-update fixes. The extractor fixes that change output share one AST cache schema bump (50 → 51), so the first build after upgrading re-extracts the affected languages.
> **Security**
> - **extract/detect**: indexing a repository no longer stats a corpus-chosen path that resolves outside the scan root. A `.sh` `source`/script-invocation line or a `.git` file naming a UNC `gitdir:`/`commondir` could coerce outbound SMB authentication on Windows (leaking a NetNTLMv2 response) on default offline settings. Probes are now bounded to the scan root and UNC paths are refused before they are resolved (GHSA-g6c9-j4vm-mwq4, thanks @Torch4084).
> **Fixes**
> - **path**: an exact node id resolves before tier matching, so an id is no longer refused as ambiguous (#5367, thanks @Arav-Arun).
> - **python**: a cross-file call through an explicit `from ... import ...` is constrained to the imported name and module (#5229, thanks @Arav-Arun).
> …

### [v0.9.114](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.114) — graphify 0.9.114
<sub>2026-11-20 · 3d ago</sub>

> Performance work on the extract/build/update pipeline, plus a batch of extractor and build fixes. Every entry marked Perf preserves graph output exactly (byte-identical); the extractor fixes change output and share one AST cache schema bump (see the note at the end).
> - Perf: **ids** `normalize_id` gets an ASCII fast-path, pre-compiled regexes and an LRU cache, so the common (ASCII, repeated) identifier case skips the Unicode normalization loop. ~1.26x on the compute path and a large win on repeated ids, which recurs heavily across a corpus.
> - Perf: **cache** `save_cached` builds the portable on-disk payload copy-on-write instead of `copy.deepcopy`-ing every per-file result; ~20% faster on the cache-write transform, scaling with per-file graph size. The input is never mutated and the on-disk bytes are identical.
> - Perf: **extract** each source file is read from disk once (the key hash and the parse share one buffer) instead of twice on a cold build, and the tree-sitter `Parser` is reused per language within a worker instead of rebuilt per file (file reads roughly halved on the worker path).
> - Perf: **extract** the cross-file resolution finalize builds its shared node/edge indexes in a few fused passes instead of ~6 independent full scans of the graph; ~15% faster on the finalize stage.
> - Perf: **watch** the no-change topology comparison uses an order-independent content hash computed in one pass instead of sorting and re-serializing the whole graph; ~1.4x on that compare.
> …

### [v0.9.113](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.113) — graphify 0.9.113
<sub>2026-11-19 · 4d ago</sub>

> - Change: **packaging** the minimum Python is now 3.11.5 (was 3.11), and soupsieve is pinned to 4.1.1 for every interpreter. soupsieve's patched releases require 3.11.5, so raising the floor clears the open soupsieve advisories (ReDoS and recursion/polynomial-DoS in the CSS selector parser, reached transitively through beautifulsoup4 in the optional `svg`/`all`/`pdf` extras). Installs on Python 3.11.0-3.11.4 keep resolving to 0.9.112; everyone on 3.11.5 and up is unaffected (#5301, thanks @TPAteeq).
> - Fix: **ruby** methods of one class or module whose names differ only by a leading/trailing `_` or by case (`_read_attribute`/`read_attribute`, `_where!`/`where!`), including those in a `class << self`, get distinct node ids instead of one swallowing the other (#5292, thanks @rohit-jsfreaky).
> - Fix: **lua** table-field functions whose names differ only by a leading/trailing `_` (`M._load`/`M.load`, `Runner:_start`/`Runner:start`) get distinct node ids; `M.f`/`M:f` still name one field (#5294, thanks @rohit-jsfreaky).
> - Fix: **scala** members whose names differ only by a leading `_`, a `_=` setter suffix, or case (`_enter`/`enter`, `size`/`size_=`, `forEach`/`foreach`), including across a class and its companion object, get distinct node ids (#5296, thanks @rohit-jsfreaky).
> - Fix: **elixir** defs whose names differ only by a leading/trailing `_`, a `!`/`?` suffix, or case (`_name`/`name`, `get`/`get!`, `__schema__`/`schema`) get distinct node ids, so a `get!` call no longer lands on `get` (#5298, thanks @rohit-jsfreaky).
> - Fix: **rust** a prelude trait's type argument (`Celsius` in `impl From<Celsius>` or a `T: Into<Celsius>` bound) is read as a generic-argument reference instead of being mistaken for the trait itself, so it no longer emits a wrong `implements`/`inherits` edge (#5332, thanks @azeemshaik025).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [docs(changelog): ship both dev trains as one 0.9.119 release](https://github.com/Graphify-Labs/graphify/commit/ba33a181f88b6ff675699decf4878566af851ab3) | safishamsi |
| 2026-11-24 | [test: mark the watchdog-driven watch-override test serial](https://github.com/Graphify-Labs/graphify/commit/42362dc8cfb8ed2e80836ae95aaee26748e735cf) | safishamsi |
| 2026-11-24 | [chore(release): schema 55, 0.9.120 changelog for the #5441..#5419 batch](https://github.com/Graphify-Labs/graphify/commit/53e64af8d0a8328fa099aef08e86b1ffef2b5ace) | safishamsi |
| 2026-11-24 | [test(5418): pin Python parameter call shadowing](https://github.com/Graphify-Labs/graphify/commit/492aa9265cda4add05a4553822e093fd331f6724) | Deepjyoti-Sarmah |
| 2026-11-24 | [fix(5418): respect parameters in the import-guided call pass](https://github.com/Graphify-Labs/graphify/commit/06e2364004d98943fb6f711a7830d4600838bc9e) | Deepjyoti-Sarmah |
| 2026-11-24 | [fix(5418): do not link a call made through a Python parameter](https://github.com/Graphify-Labs/graphify/commit/d760ad3994d8744783e78af839a156d465f13557) | Deepjyoti-Sarmah |
| 2026-11-24 | [refactor(5418): move _python_param_names into python_scope](https://github.com/Graphify-Labs/graphify/commit/a17fd50f1c66445cd7460ba53194d5843213a3dc) | Deepjyoti-Sarmah |
| 2026-11-24 | [fix(go): fold sibling-file type copies per directory when a same-name…](https://github.com/Graphify-Labs/graphify/commit/a13d7ac194846d4a8dc8182d1edf51a4a3e5510a) | PravalVerma |
| 2026-11-24 | [perf(build): optimize file label disambiguation from O(M^2 * D) to O(…](https://github.com/Graphify-Labs/graphify/commit/0d4730f6a0893dd02f0bb4dce46ed410bbc2a834) | Gaurav-meena95 |
| 2026-11-24 | [fix(affected): replace O(/E/) full-graph scans with incident edge tra…](https://github.com/Graphify-Labs/graphify/commit/4b7306d80760c27c4b09938a943708b94ba6ccf5) | Gaurav-meena95 |

[See all commits ↗](https://github.com/Graphify-Labs/graphify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Graphify-Labs/graphify.git
```
