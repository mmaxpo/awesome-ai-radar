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
| ⭐ **Stars** | 151.5k |
| 🍴 **Forks** | 14.6k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/Graphify-Labs/graphify/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `claude-code` `graphrag` `knowledge-graph` `codex` `openclaw` `skills` `antigravity` `gemini` `leiden` `rag` `tree-sitter` `ai-agents` `ast` `code-analysis` `code-search` `cursor` `developer-tools` `llm` `mcp` `graphify` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-04-03 |
| 📦 **Latest release** | [v0.9.114](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.114) — 2026-11-20 |
| 🌿 **Default branch** | `v8` |
| 💾 **Size** | 36.4 MB |
| 🌐 **Website** | https://www.graphify.com |

## 📦 Recent releases

### [v0.9.114](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.114) — graphify 0.9.114
<sub>2026-11-20 · today</sub>

> Performance work on the extract/build/update pipeline, plus a batch of extractor and build fixes. Every entry marked Perf preserves graph output exactly (byte-identical); the extractor fixes change output and share one AST cache schema bump (see the note at the end).
> - Perf: **ids** `normalize_id` gets an ASCII fast-path, pre-compiled regexes and an LRU cache, so the common (ASCII, repeated) identifier case skips the Unicode normalization loop. ~1.26x on the compute path and a large win on repeated ids, which recurs heavily across a corpus.
> - Perf: **cache** `save_cached` builds the portable on-disk payload copy-on-write instead of `copy.deepcopy`-ing every per-file result; ~20% faster on the cache-write transform, scaling with per-file graph size. The input is never mutated and the on-disk bytes are identical.
> - Perf: **extract** each source file is read from disk once (the key hash and the parse share one buffer) instead of twice on a cold build, and the tree-sitter `Parser` is reused per language within a worker instead of rebuilt per file (file reads roughly halved on the worker path).
> - Perf: **extract** the cross-file resolution finalize builds its shared node/edge indexes in a few fused passes instead of ~6 independent full scans of the graph; ~15% faster on the finalize stage.
> - Perf: **watch** the no-change topology comparison uses an order-independent content hash computed in one pass instead of sorting and re-serializing the whole graph; ~1.4x on that compare.
> …

### [v0.9.113](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.113) — graphify 0.9.113
<sub>2026-11-19 · yesterday</sub>

> - Change: **packaging** the minimum Python is now 3.11.5 (was 3.11), and soupsieve is pinned to 4.1.1 for every interpreter. soupsieve's patched releases require 3.11.5, so raising the floor clears the open soupsieve advisories (ReDoS and recursion/polynomial-DoS in the CSS selector parser, reached transitively through beautifulsoup4 in the optional `svg`/`all`/`pdf` extras). Installs on Python 3.11.0-3.11.4 keep resolving to 0.9.112; everyone on 3.11.5 and up is unaffected (#5301, thanks @TPAteeq).
> - Fix: **ruby** methods of one class or module whose names differ only by a leading/trailing `_` or by case (`_read_attribute`/`read_attribute`, `_where!`/`where!`), including those in a `class << self`, get distinct node ids instead of one swallowing the other (#5292, thanks @rohit-jsfreaky).
> - Fix: **lua** table-field functions whose names differ only by a leading/trailing `_` (`M._load`/`M.load`, `Runner:_start`/`Runner:start`) get distinct node ids; `M.f`/`M:f` still name one field (#5294, thanks @rohit-jsfreaky).
> - Fix: **scala** members whose names differ only by a leading `_`, a `_=` setter suffix, or case (`_enter`/`enter`, `size`/`size_=`, `forEach`/`foreach`), including across a class and its companion object, get distinct node ids (#5296, thanks @rohit-jsfreaky).
> - Fix: **elixir** defs whose names differ only by a leading/trailing `_`, a `!`/`?` suffix, or case (`_name`/`name`, `get`/`get!`, `__schema__`/`schema`) get distinct node ids, so a `get!` call no longer lands on `get` (#5298, thanks @rohit-jsfreaky).
> - Fix: **rust** a prelude trait's type argument (`Celsius` in `impl From<Celsius>` or a `T: Into<Celsius>` bound) is read as a generic-argument reference instead of being mistaken for the trait itself, so it no longer emits a wrong `implements`/`inherits` edge (#5332, thanks @azeemshaik025).
> …

### [v0.9.112](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.112) — graphify 0.9.112
<sub>2026-11-17 · 3d ago</sub>

> - Docs: **python** the README, its translations, CONTRIBUTING, RELEASING, the bug-report template and the ruff/pyright targets now state Python 3.11 as the minimum, matching the floor that shipped in 0.9.111 (#5238, thanks @Deepanshu-Mehta; @Max17190 sent the same fix in #5237).
> - Docs: **links** the Always-on setup link in the README and all translations points straight at docs.graphify.com/open-source/vibe-coding instead of going through a redirect from the old guides/always-on path (#5261, thanks @SyedFahad7).
> - Fix: **java** each overloaded method gets its own node keyed by arity and erased signature, instead of all overloads collapsing into one node that dropped members and misrouted calls; `affected` override-matching is now arity-aware so a split `run(int)` is not tied to a supertype `run()` by label, and cross-repo and generic-method overloads are handled too (#5251, thanks @deba2k5). Same-arity, type-only-distinct overloads still bind to the first declared one (mirroring the C# precedent #4584); literal-argument-type dispatch is a follow-up. Overloaded constructors still share one node.
> - Fix: **go** a bare receiver type (`func (s Service) m()`) resolves to its own package's type instead of being matched against every same-named type in the corpus, so two packages each declaring a `Service` keep their own member-call edges rather than both losing them to an ambiguity bail (#5242, thanks @ayushcodes10).
> - Fix: **rust** a `use crate::...` import resolves inside its own crate instead of leaking across crate boundaries to another crate's same-named item in a multi-crate workspace; a single-crate `crate::` import still resolves as before (#5240, thanks @Max17190).
> - Fix: **js** a `this.x = function (params) {...}` member no longer fabricates a false `indirect_call` when one of its parameters shadows a same-named corpus function used in argument position; its own params and names captured from the enclosing scope are treated as local bindings, while a genuinely unbound name still resolves (#5241, thanks @Max17190).
> …

### [v0.9.111](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.111) — graphify 0.9.111
<sub>2026-11-15 · 5d ago</sub>

> Maintenance and security release.
> - **Minimum Python is now 3.11** (was 3.10). Python 3.10 reached end of life in October 2026, and the patched releases of our optional and transitive dependencies no longer ship wheels for it. Raising the floor lets the lockfile move to those patched versions. Installs on Python 3.10 keep resolving to 0.9.110, the last 3.10-compatible release; everyone on 3.11 and up is unaffected.
> - **Security:** with 3.10 dropped, the committed lockfile resolves Pillow 13.0.0, filelock 4.2.4 and opentelemetry-api 1.45.2 for every supported interpreter, clearing the open Dependabot advisories against the older pins. Pillow is only pulled in by the optional `svg`/`all` extras, not the core install. This is a dependency and packaging change only: no change to extraction behaviour and the AST cache schema is unchanged.
> - **Test:** the backtick-substitution runtime tests now skip on bash older than 4.1 (they rely on `BASH_XTRACEFD`, added in 4.1) instead of misbehaving on the bash 3.2 that macOS ships.

### [v0.9.110](https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.110) — graphify 0.9.110
<sub>2026-11-15 · 5d ago</sub>

> - Fix: **python** a call through an aliased import (`from mod import foo as bar; bar()`) is linked from inside a method body and from a decorated function or class def, not just at module level (#5214, thanks @hementhu).
> - Fix: **go** a type's methods declared in an internal `_test.go` file (same `package foo`) fold into the type's package node instead of splitting it and dropping its method-call edges; an external `package foo_test` stays separate (#5209, thanks @Yi-111-a).
> - Fix: **js** a name bound in an enclosing scope and captured into a tracked nested closure no longer fabricates a false `indirect_call` to a same-named corpus function; a genuinely unbound name still resolves (#5217, thanks @Sidreyas).
> - Fix: **sql** a T-SQL procedure that parses structurally (rather than through ERROR recovery) keeps its INSERT/UPDATE/DELETE/SELECT INTO writes, and session temp objects (`#t`, `##t`, `@t`) are skipped (#5146, thanks @sunhouy).
> - Fix: **sql** an Oracle `CREATE PACKAGE`/`PACKAGE BODY`'s member procedures and functions, and their table reads and writes, are recovered instead of yielding only a file node (#5168, thanks @JaynouOliver).
> - Test: **llm** cover non-fragment array siblings and fragment-less arrays in the single-element-array unwrap (#5192 follow-up, thanks @rohanb123).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [docs(readme): add "When to reach for Graphify" task table to translat…](https://github.com/Graphify-Labs/graphify/commit/b582ad401aaef4378935ec6620e3b165ae8e03c1) | safishamsi |
| 2026-11-20 | [docs(readme): propagate hero, quickstart fix, and terminology to tran…](https://github.com/Graphify-Labs/graphify/commit/5d2e6487797b308fb37113fee72897a1f74cac5f) | safishamsi |
| 2026-11-20 | [docs(readme): add task-based "When to reach for Graphify" section](https://github.com/Graphify-Labs/graphify/commit/b2e0d16ae792c2f52de7ff3b4f3e416e7488951d) | safishamsi |
| 2026-11-20 | [docs(readme): blend hero, fix quickstart, clarify god-node/community …](https://github.com/Graphify-Labs/graphify/commit/15bf90831bf1fa8682b8d997b8fa62928864ae23) | safishamsi |
| 2026-11-20 | [docs(readme): add Install-in-Gemini-CLI badge to Connect section](https://github.com/Graphify-Labs/graphify/commit/1e8bb62be5b87edf3963bdd40a6089da495ccf6e) | safishamsi |
| 2026-11-20 | [docs(readme): add "Connect your agent over MCP" section](https://github.com/Graphify-Labs/graphify/commit/dfab9ccc05cfedb4ce98beea1809582ac7a9f62c) | safishamsi |
| 2026-11-20 | [chore(release): bump version to 0.9.114](https://github.com/Graphify-Labs/graphify/commit/ae37e0bd4d6dc95f3ea0f50d7c154603c6458b2e) | safishamsi |
| 2026-11-20 | [docs: fold the sql/vbnet/cpp/sys.path/serve/build fixes into 0.9.114 …](https://github.com/Graphify-Labs/graphify/commit/b2e61e4ccea16df79162aff9daa12ec533be2ed9) | safishamsi |
| 2026-11-20 | [fix(extract): bind plain-imported module member calls to function nod…](https://github.com/Graphify-Labs/graphify/commit/e68f46a048d3934a01386c69cc317b777c084573) | madhusudanpatnaik |
| 2026-11-20 | [fix(cpp): keep std-qualified type references off project symbols (#5219)](https://github.com/Graphify-Labs/graphify/commit/5aec2d1a849fb70e48da82cf0379ae75380b025e) | deba2k5 |

[See all commits ↗](https://github.com/Graphify-Labs/graphify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Graphify-Labs/graphify.git
```
