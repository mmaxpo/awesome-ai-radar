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
| ⭐ **Stars** | 152.4k |
| 🍴 **Forks** | 14.6k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/Graphify-Labs/graphify/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `claude-code` `graphrag` `knowledge-graph` `codex` `openclaw` `skills` `antigravity` `gemini` `leiden` `rag` `tree-sitter` `ai-agents` `ast` `code-analysis` `code-search` `cursor` `developer-tools` `llm` `mcp` `graphify` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-04-03 |
| 📦 **Latest release** | [v0.9.118](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.118) — 2026-11-23 |
| 🌿 **Default branch** | `v8` |
| 💾 **Size** | 36.0 MB |
| 🌐 **Website** | graphify.com |

## 📦 Recent releases

### [v0.9.118](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.118)
<sub>2026-11-23 · today</sub>

> A batch of extractor, resolution, serve, export, clustering and reporting fixes across fourteen community pull requests. The Objective-C, C and C# changes alter node/edge output, so the AST cache schema bumps (51 to 53) and the first build after upgrading re-extracts the affected languages; the other fixes need no rebuild.
> - Fix: **csharp** a local, parameter or field named `partial`, `required`, `async`, `nint`, `nuint` or `with` (contextual keywords) that tree-sitter-c-sharp mis-parses where a statement starts with it no longer derails the file; it is rewritten to its verbatim `@name` form before parsing (byte-length preserving), so the enclosing type and the members after it are kept instead of being silently dropped (#5043, thanks @ThatAblaze).
> - Fix: **c** a call through a struct function-pointer field (`ops->run()`, `ops.run()`) no longer fabricates a `calls` edge to a same-named free function; the field name is no evidence of the pointer's runtime target, so the guess is dropped. A plain direct call still resolves (#5410, thanks @sdivyanshu90).
> - Fix: **objc** an Objective-C method whose name folds onto a sibling's id within one `@interface`/`@implementation`/`@protocol` (a leading/trailing `_` as in `-setup`/`-_setup`, or a case-only difference) gets its own salted node id instead of overwriting it; the declaration and definition of one method still share a single node (#5390, thanks @ayushcodes10).
> - Fix: **go** a struct field's owner type is scoped to its own package, so a field of a type whose name is declared in two packages binds to the right one and its member calls resolve instead of being dropped as ambiguous (#5408, thanks @azizur100389).
> - Fix: **extract** a Svelte import that comes through an `export *` barrel now resolves to the real defining module, matching plain `.ts`. The cross-file resolver was masking `.vue` but not `.svelte`, so the Svelte `<script>` imports were lost to a template parse error; chained barrels resolve and ambiguous re-exports fail closed. Run `graphify extract . --force` once to repair an already-cached graph (#5403, thanks @Max17190).
> …

### [v0.9.115](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.115)
<sub>2026-11-21 · yesterday</sub>

> Security fix for a forced-SMB-authentication issue on Windows (GHSA-g6c9-j4vm-mwq4), plus a batch of extractor, resolution and incremental-update fixes. The extractor fixes that change output share one AST cache schema bump (50 → 51), so the first build after upgrading re-extracts the affected languages.
> **Security**
> - **extract/detect**: indexing a repository no longer stats a corpus-chosen path that resolves outside the scan root. A `.sh` `source`/script-invocation line or a `.git` file naming a UNC `gitdir:`/`commondir` could coerce outbound SMB authentication on Windows (leaking a NetNTLMv2 response) on default offline settings. Probes are now bounded to the scan root and UNC paths are refused before they are resolved (GHSA-g6c9-j4vm-mwq4, thanks @Torch4084).
> **Fixes**
> - **path**: an exact node id resolves before tier matching, so an id is no longer refused as ambiguous (#5367, thanks @Arav-Arun).
> - **python**: a cross-file call through an explicit `from ... import ...` is constrained to the imported name and module (#5229, thanks @Arav-Arun).
> …

### [v0.9.114](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.114) — graphify 0.9.114
<sub>2026-11-20 · 2d ago</sub>

> Performance work on the extract/build/update pipeline, plus a batch of extractor and build fixes. Every entry marked Perf preserves graph output exactly (byte-identical); the extractor fixes change output and share one AST cache schema bump (see the note at the end).
> - Perf: **ids** `normalize_id` gets an ASCII fast-path, pre-compiled regexes and an LRU cache, so the common (ASCII, repeated) identifier case skips the Unicode normalization loop. ~1.26x on the compute path and a large win on repeated ids, which recurs heavily across a corpus.
> - Perf: **cache** `save_cached` builds the portable on-disk payload copy-on-write instead of `copy.deepcopy`-ing every per-file result; ~20% faster on the cache-write transform, scaling with per-file graph size. The input is never mutated and the on-disk bytes are identical.
> - Perf: **extract** each source file is read from disk once (the key hash and the parse share one buffer) instead of twice on a cold build, and the tree-sitter `Parser` is reused per language within a worker instead of rebuilt per file (file reads roughly halved on the worker path).
> - Perf: **extract** the cross-file resolution finalize builds its shared node/edge indexes in a few fused passes instead of ~6 independent full scans of the graph; ~15% faster on the finalize stage.
> - Perf: **watch** the no-change topology comparison uses an order-independent content hash computed in one pass instead of sorting and re-serializing the whole graph; ~1.4x on that compare.
> …

### [v0.9.113](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.113) — graphify 0.9.113
<sub>2026-11-19 · 3d ago</sub>

> - Change: **packaging** the minimum Python is now 3.11.5 (was 3.11), and soupsieve is pinned to 4.1.1 for every interpreter. soupsieve's patched releases require 3.11.5, so raising the floor clears the open soupsieve advisories (ReDoS and recursion/polynomial-DoS in the CSS selector parser, reached transitively through beautifulsoup4 in the optional `svg`/`all`/`pdf` extras). Installs on Python 3.11.0-3.11.4 keep resolving to 0.9.112; everyone on 3.11.5 and up is unaffected (#5301, thanks @TPAteeq).
> - Fix: **ruby** methods of one class or module whose names differ only by a leading/trailing `_` or by case (`_read_attribute`/`read_attribute`, `_where!`/`where!`), including those in a `class << self`, get distinct node ids instead of one swallowing the other (#5292, thanks @rohit-jsfreaky).
> - Fix: **lua** table-field functions whose names differ only by a leading/trailing `_` (`M._load`/`M.load`, `Runner:_start`/`Runner:start`) get distinct node ids; `M.f`/`M:f` still name one field (#5294, thanks @rohit-jsfreaky).
> - Fix: **scala** members whose names differ only by a leading `_`, a `_=` setter suffix, or case (`_enter`/`enter`, `size`/`size_=`, `forEach`/`foreach`), including across a class and its companion object, get distinct node ids (#5296, thanks @rohit-jsfreaky).
> - Fix: **elixir** defs whose names differ only by a leading/trailing `_`, a `!`/`?` suffix, or case (`_name`/`name`, `get`/`get!`, `__schema__`/`schema`) get distinct node ids, so a `get!` call no longer lands on `get` (#5298, thanks @rohit-jsfreaky).
> - Fix: **rust** a prelude trait's type argument (`Celsius` in `impl From<Celsius>` or a `T: Into<Celsius>` bound) is read as a generic-argument reference instead of being mistaken for the trait itself, so it no longer emits a wrong `implements`/`inherits` edge (#5332, thanks @azeemshaik025).
> …

### [v0.9.112](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.112) — graphify 0.9.112
<sub>2026-11-17 · 6d ago</sub>

> - Docs: **python** the README, its translations, CONTRIBUTING, RELEASING, the bug-report template and the ruff/pyright targets now state Python 3.11 as the minimum, matching the floor that shipped in 0.9.111 (#5238, thanks @Deepanshu-Mehta; @Max17190 sent the same fix in #5237).
> - Docs: **links** the Always-on setup link in the README and all translations points straight at docs.graphify.com/open-source/vibe-coding instead of going through a redirect from the old guides/always-on path (#5261, thanks @SyedFahad7).
> - Fix: **java** each overloaded method gets its own node keyed by arity and erased signature, instead of all overloads collapsing into one node that dropped members and misrouted calls; `affected` override-matching is now arity-aware so a split `run(int)` is not tied to a supertype `run()` by label, and cross-repo and generic-method overloads are handled too (#5251, thanks @deba2k5). Same-arity, type-only-distinct overloads still bind to the first declared one (mirroring the C# precedent #4584); literal-argument-type dispatch is a follow-up. Overloaded constructors still share one node.
> - Fix: **go** a bare receiver type (`func (s Service) m()`) resolves to its own package's type instead of being matched against every same-named type in the corpus, so two packages each declaring a `Service` keep their own member-call edges rather than both losing them to an ambiguity bail (#5242, thanks @ayushcodes10).
> - Fix: **rust** a `use crate::...` import resolves inside its own crate instead of leaking across crate boundaries to another crate's same-named item in a multi-crate workspace; a single-crate `crate::` import still resolves as before (#5240, thanks @Max17190).
> - Fix: **js** a `this.x = function (params) {...}` member no longer fabricates a false `indirect_call` when one of its parameters shadows a same-named corpus function used in argument position; its own params and names captured from the enclosing scope are treated as local bindings, while a genuinely unbound name still resolves (#5241, thanks @Max17190).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [docs(changelog): consolidate the three dev trains into one 0.9.118 re…](https://github.com/Graphify-Labs/graphify/commit/5ce8fceff41d1b636f872b6206b917ec2af7ac54) | safishamsi |
| 2026-11-23 | [chore(release): schema 53 and 0.9.118 changelog for the #5382..#5262 …](https://github.com/Graphify-Labs/graphify/commit/39294d0d6bbe24e83df0fd8d31113e81a1f89c4e) | safishamsi |
| 2026-11-23 | [fix(csharp): escape contextual-keyword names the grammar rejects (#5043)](https://github.com/Graphify-Labs/graphify/commit/017d6ae84354e4fd1e53eb8252b2cbecf5ad021d) | ThatAblaze |
| 2026-11-23 | [fix(c): avoid guessing targets for struct callback calls](https://github.com/Graphify-Labs/graphify/commit/b7e8f9e9ba0201666ee7ea66fe4ab654a9d84e41) | sdivyanshu90 |
| 2026-11-23 | [fix(go): scope struct field owners to their package](https://github.com/Graphify-Labs/graphify/commit/3737e49e5bc15a5589238199661ec693da362462) | azizur100389 |
| 2026-11-23 | [fix(extract): report audio/video files detected but not extracted](https://github.com/Graphify-Labs/graphify/commit/5afc506da2ef756f5ab9607ede464c485e450cf4) | ayushcodes10 |
| 2026-11-23 | [perf(cluster): count community overlaps from shared nodes](https://github.com/Graphify-Labs/graphify/commit/e97409d12be4ec41c725089b86d6527ed6b1cb21) | Max17190 |
| 2026-11-23 | [chore(release): 0.9.117 changelog; hoist serve anyio import](https://github.com/Graphify-Labs/graphify/commit/e6d37d5ea84568d255cdcb35963c2835a6820b90) | safishamsi |
| 2026-11-23 | [test(5371): dispatch through the handler API of mcp 1.x and 2.x](https://github.com/Graphify-Labs/graphify/commit/fc6ab405c5b0e72c8720ac180d050622ae006708) | Deepjyoti-Sarmah |
| 2026-11-23 | [fix(serve): load graph.json off the event loop in call_tool/read_reso…](https://github.com/Graphify-Labs/graphify/commit/15e14eadf7201a714c7f41abf24be588ab5e7995) | Deepjyoti-Sarmah |

[See all commits ↗](https://github.com/Graphify-Labs/graphify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Graphify-Labs/graphify.git
```
