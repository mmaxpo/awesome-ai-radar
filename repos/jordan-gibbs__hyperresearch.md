# jordan-gibbs/hyperresearch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/jordan-gibbs/hyperresearch)

> Convert Claude Code or Codex into the most intelligent Deep Research Agent. Collect, search, and synthesize web research into a persistent, searchable wiki that builds on itself. Hosted API + MCP: hyperresearch.ai

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Turns Claude Code or Codex into a deep-research agent |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.9k |
| 🍴 **Forks** | 500 |
| 🐞 **Open issues + PRs** | [15](https://github.com/jordan-gibbs/hyperresearch/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `agentskills` `claude-code` `deep-research` `deep-research-agent` `codex` `deepresearch` `research` `research-agent` `research-tools` `codex-plugin` `codex-skill` `citations` `mcp-server` |
| 🕒 **Last activity** | 2026-11-17 (yesterday) |
| 📅 **Created** | 2026-04-09 |
| 📦 **Latest release** | [v0.13.3](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.13.3) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 6.9 MB |
| 🌐 **Website** | https://hyperresearch.ai |

## 📦 Recent releases

### [v0.13.3](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.13.3)
<sub>2026-11-16 · yesterday</sub>

> **Fixed**
> - **`run verify` has no unit cliff for mixed Chinese/English reports (#71, reported by @redmyapple).** Length and citation density switched from whitespace words to characters / 3 at a spaceless-script ratio of exactly 0.3, so a mixed report 0.1% under the cutoff was measured at about a third of its length and blocked on `length-in-range`, while ~600 more characters of Chinese made the same report pass. Across a band from 0.2 to 0.4 the count now blends linearly between the two measures, and so does the length target. Text below 0.2 (English, Korean) and above 0.4 (Chinese, Japanese, Thai) is counted exactly as before. A blended check says so in its detail (`mixed script, N% counted as chars / 3`).
> - **Generated instructions no longer prefix commands with `PYTHONIOENCODING=utf-8` (#205, reported by @vik-borisov).** That is bash syntax; Windows PowerShell reads `PYTHONIOENCODING=utf-8` as a command name and fails before hyperresearch starts, and every reinstall wrote the prefix back into the fetcher, cite-checker, corpus-critic, draft-orchestrator, source-analyst and browser-fetcher agents and steps 2 and 8. The prefix was never needed: on Windows the CLI already switches its own stdout and stderr to UTF-8 at startup. A test installs both targets and checks that no installed instruction carries the prefix.
> - **Install no longer deletes a user's own `hyperresearch-*` skill folder (#206, from @ray910408).** The step-skill prunes treated any `SKILL.md` that mentions hyperresearch as ours, so a hand-written `.claude/skills/hyperresearch-my-notes/` (or a `~/.claude/skills/hyperresearch-2024-...` under `--global`) was deleted with everything in it. A prefix-matched folder is now removed only when its `SKILL.md` carries the rendered-install provenance header or its name is a step the package ships.
> - **MCP `search_notes`, `get_hubs` and `list_sources` cap `limit` at 1-200 (#206, from @ray910408).** The value went straight into SQL, and SQLite reads a negative `LIMIT` as no limit, so one call could return every note with its full body. `list_notes` keeps its documented `limit=0` for all, since it returns summaries only.

### [v0.13.2](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.13.2)
<sub>2026-11-12 · 5d ago</sub>

> **Fixed**
> - **Installed agents show valid JSON in their output examples (#203, from @rsloveless).** The instruction-critic, readability-recommender and corpus-critic templates kept `str.format()` brace escapes, but none of the three goes through `.format()`, so a clean install wrote `{{` and `}}` into their JSON schema examples, on both the Claude and Codex targets. An agent that copied its example emitted invalid JSON. The escapes are gone from those three templates, and a new test installs every agent for both targets and parses each fenced `json` example.
> - **`run verify` leaves the Sources section out of citation density (#202, from @SID-6921).** The `citation-density` gate counted every `[N]` and `[[...]]` in the whole report, including the numbered entries of `## Sources` / `## References`, so a long source list could carry a thinly cited body over the floor. The gate now counts citations and words in the body only, matching cite-check and the instruction critic. The length, heading and scaffold-leak checks still read the full report.
> - **Sync picks the same winner for duplicate note ids on every filesystem (#201, from @jackiectl2).** Sync scanned notes in `rglob` order, so when two files declared the same `id:` the one kept depended on directory traversal order; an import of `a/note.md` and `b/note.md` could keep `b`. Sync now scans in lexical path order.

### [v0.13.1](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.13.1)
<sub>2026-11-09 · 8d ago</sub>

> - **`hpr search --semantic` scores every note with one numpy matmul instead of one Python `cosine()` call each (#59).** `cosine()` did three generator passes per candidate in pure Python; at 512-dim that's ~49µs/vector, so a one-second query capped out around 15k notes (5k at 1536-dim) — well past any real vault, but the module docstring's "fine to ~50k notes" was already off by about an order of magnitude, having been written as if the vectorized loop it never got already existed. `semantic_search` now loads the stored vectors with `np.frombuffer` and scores the whole set in a single matmul, which is unaffected by a note embedded under a stale model/dimension mid-migration — it scores 0, same as `cosine()` did on a length mismatch, instead of joining the matrix. The scholarly-metadata filters and index-note exclusion added in #119 are applied in the SQL fetch before the matmul, so a filtered semantic search still only scores the filtered candidate set. Measured sub-second up to ~50k notes; larger vaults are untested. A stored all-zero vector, or an all-zero query, scores 0 with no NaN. numpy was already an unlisted transitive dependency via Crawl4AI; it's now declared directly. `cosine()` itself is untouched and still covered by its own test.
> - **Sync renames a note's row in place when its `id:` changes (#159, from @fduple).** An edited `id:` went through the upsert as an insert of the new id, which `UNIQUE(notes.path)` refused on every sync; the stale row kept the old id and collided with the file that really owned it. Sync now moves the row to the new id, keeps the rows only the database holds (claims, embeddings, assets, and the `sources` and `escalations` rows for its URL), rebuilds the rest from the markdown, and frees the old id in the same pass. Updates run before adds so a new file named after the freed id indexes in one run. A rename is refused, with an error naming the file, when the frontmatter declares no id or does not parse, or when a new file named after the target id claims it. If SQLite rolls the whole sync transaction back mid-pass, sync stops and reports that nothing from the pass was kept.
> - **`note rm` removes the asset files its own rows name (#159, from @fduple).** After an id rename a note's asset files stay in `research/assets/<old id>/`, so removing `research/assets/<id>/` wholesale could delete another note's files and leave the removed note's own behind. `note rm` now removes the files the note's `assets` rows name anywhere under `research/assets/`, plus what `research/assets/<id>/` holds that no other note's row names, never a file another note's row names, and nothing outside `research/assets/`. Symlinks are unlinked as links, a symlinked `research/assets/<id>` is left alone, and a file that cannot be removed is listed under `assets_not_removed` without stopping the delete.
> - **BEHAVIOR CHANGE — `install <path>` refuses a path that does not exist unless `--create` (#155, contributed by @fduple).** `hyperresearch install` and `install --steps-only` create missing parents, and with no TTY nothing stood in between, so a stale or mistyped path came back as a new empty vault with exit 0 while the real vault kept its old skills. Both now check the path before writing anything: a missing path fails with `PATH_NOT_FOUND`, and a file, as the path itself or as one of its parents, fails with `NOT_A_DIRECTORY`. `--create` makes the directory and any missing parents first (a failure there is `CREATE_FAILED`); it cannot help when a file is in the way. The check runs before the interactive setup route too, so from a terminal `install <new-dir>`, which used to open setup and create the directory, is now refused the same way; `hyperresearch setup <path>` still creates it, and setup's non-TTY / `--json` handoff to install passes `--create`. An existing directory without a vault is the normal first-time install and is unchanged, as is `--global`. Scripts that install into a directory they have not made yet need `--create`.
> - **The Codex Stop hook stays in the project.** A vault at the home directory (where `install` or the first-run bootstrap was run from `~`) made `<root>/.codex/hooks.json` Codex's user-level hooks file, so the stop gate ran in every Codex session. It finds a vault by walking up from the session's directory, so a home-vault run that was mid-pipeline would force-continue unrelated sessions anywhere under `~`. The hook is now skipped, with a "NOT installed" note, whenever the project's `.codex/` is `$CODEX_HOME` (default `~/.codex`). Separately, the first-run bootstrap inside a Codex session crashed with `OSError: Read-only file system`, after writing the step files, because the workspace-write sandbox keeps `.codex/` read-only. It now reports the hook as NOT installed together with the command to run outside the sandbox, and the entry skill tells the orchestrator to re-run that command once with escalated permissions.
> - **`keenable` web provider.** Web search with page text in each result, plus page fetch, with no key required; `KEENABLE_API_KEY` lifts the per-IP rate limits. Opt-in via `[web] provider = "keenable"`, no new dependency.
> …

### [v0.13.0](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.13.0)
<sub>2026-10-27 · 21d ago</sub>

> - **Step prompts agree with each other (#102).** Settles the contract conflicts listed in the issue: the no-re-synthesis invariant names the ship gate's compression pass as its one exception; width-sweep fetchers take no new topic searches but still chase the primary sources their batch cites; step 7 has a documented path for fewer than the target tensions when step 4 justified zero loci; a failed critic is re-spawned once and otherwise leaves an empty `critic_failed` findings file, since the ship gate checks all four exist; the step 11 outline leaves out Opinionated Synthesis for `short` reports; the step 1 example no longer shows a wrapper requirement in the decomposition; the readability recommender writes a JSON object, matching its schema; the polish auditor receives `wrapper_contract_path` so it knows whether to keep YAML frontmatter; step 16 hands off to the ship gate instead of declaring the run done; the one-chapter case in step 1.5 is described as an escape hatch; and the cite-check Goal states that non-numeric citations are sampled.
> - **The pipeline runs on the OpenAI Codex CLI.** `hyperresearch install . --target codex` installs the entry skill at `.agents/skills/hyperresearch/`, invoked as `$hyperresearch <query>`, along with the 18 step procedures as plain files under `.hyperresearch/codex/steps/`, the subagent roster as custom agents in `.codex/agents/*.toml`, a Stop hook in `.codex/hooks.json`, and an `AGENTS.md` block. The step procedures are plain files because Codex caps the skill listing and has no skill-to-skill invocation. `--target all` installs both platforms. `--global --target codex` writes the skill to `~/.agents/skills/` and the agents to `~/.codex/agents/`. `--target claude` is the default and installs the same layout as before. Differences on Codex: there is no browser lane, so blocked fetches stay queued and are listed for the user; the Read+Edit tool locks are instructions rather than enforcement; and the Stop hook (`hyperresearch run stop-gate`) blocks the session from ending mid-pipeline. The Stop hook exists because an earlier Codex attempt answered inline and never touched the vault. Codex's sandbox defaults to read-only with no network, so a session needs `--sandbox workspace-write -c sandbox_workspace_write.network_access=true`. hyperresearch documents these flags and never writes to Codex's config.
> - **The repo is a Codex plugin marketplace too.** `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` publish the same `deep-research` bootstrap skill as the Claude Code plugin: `codex plugin marketplace add jordan-gibbs/hyperresearch`, then `codex plugin add hyperresearch@hyperresearch`. The skill no longer assumes Claude Code. On Codex it runs `install --target codex` and then reads the entry skill directly, because Codex discovers skills when a session starts. It gains `license` and `compatibility` frontmatter and an `agents/openai.yaml`. Codex namespaces plugin skills, so from the plugin it is `$hyperresearch:deep-research`; installed standalone with `npx skills add jordan-gibbs/hyperresearch -a codex` (to `.agents/skills/deep-research/`) it is `$deep-research`. The `openai.yaml` starter prompt names the skill in words rather than by a `$` mention that would only match one of those. The README now leads with Claude Code and Codex install paths side by side.
> - **`run resume` follows the tier step 1 declared.** A run is initialized with the installed gear's step list, and step 1 can reclassify it (usually to `light`) in `prompt-decomposition.json`. The ship gate already honoured that tier; `resume_position` did not, so a light-tier run that finished step 2 was told to resume at step 3, a step its tier skips. `run resume`, `run status` and the Codex Stop gate now use the declared tier's steps. Found during the first live Codex run.
> - **The SSRF gate resolves the name httpx connects to (#161).** `check_url` looked up the hostname as urlparse returns it, and `getaddrinfo` encodes a non-ASCII name with the stdlib IDNA 2003 codec, while httpx connects with IDNA 2008. For `http://straße.attacker.example/` the gate resolved `strasse.attacker.example` and httpx connected to `xn--strae-oqa.attacker.example`, two separate DNS names. The gate now resolves `httpx.URL(url).raw_host`. `allow_private_hosts` entries and the URL host go through one normalization (lowercase, IDNA 2008 via `idna.encode`, trailing dot stripped), so an entry matches its unicode/punycode and root-dot spellings; an entry that can never match raises an error naming it. A URL httpx cannot parse, and a name `getaddrinfo` cannot encode, raise `SafeHTTPError` instead of escaping and failing a whole batch. `idna` is now a declared dependency.
> - **The SSRF gate refuses URLs a browser reads differently.** `check_url` learns the host from urlparse and httpx (RFC 3986), but the crawl4ai lane hands the URL to Chromium (WHATWG). For `http://127.0.0.1\@evil.com/` the gate checked `evil.com` while Chromium, which reads `\` as `/`, connected to 127.0.0.1; the final-URL recheck only ran after the request was sent. The gate now refuses a backslash in the authority, a percent-encoded hostname (`127.0.0.%31`, which Chromium decodes), and a host whose last label is numeric unless it is a canonical dotted quad (`127.1`, `0x7f.1`, `2130706433`: Chromium parses these as IPv4 in its own grammar, getaddrinfo varies by platform). Tabs, newlines and other control characters inside the URL were already refused by the httpx parse. A backslash in the path, query or fragment is still allowed: it cannot move the host. The check is in `check_url`, so every lane gets it.
> …

### [v0.12.0](https://github.com/jordan-gibbs/hyperresearch/releases/tag/v0.12.0)
<sub>2026-09-24 · 1mo ago</sub>

> Scholarly search filters, a Serply web provider, and the repo as a Claude Code plugin (`/plugin marketplace add jordan-gibbs/hyperresearch`).
> **Behaviour change:** crawl4ai's headless browser now verifies TLS certificates. A bad certificate raises `CertVerificationError`; `[fetch] browser_verify_tls = false` opts out.
> **Migration:** the v13 migration makes `is_retracted` nullable (unknown vs. checked) and runs on first open.
> **Security:** IPv4-mapped IPv6 classified by its IPv4; run tags and note ids confined to the vault; OA URLs through the SSRF gate.
> Also: Python 3.14, a PDF lane for the builtin provider, fence-length-aware code stripping, and an OpenAlex outage no longer erases a known retraction. Full list in CHANGELOG.md.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix: sync indexes the final report, which has no frontmatter by desig…](https://github.com/jordan-gibbs/hyperresearch/commit/8f192b88bf777e2ad6da5e07e4b2ad7af40e2d7c) | fduple |
| 2026-11-16 | [release: v0.13.3 (#211)](https://github.com/jordan-gibbs/hyperresearch/commit/30d5231bfa1802b1723e4b93b3baf2a9e5e1b5a3) | jordan-gibbs |
| 2026-11-16 | [fix(verify): blend word and char counts across the spaceless cutoff (…](https://github.com/jordan-gibbs/hyperresearch/commit/04ffc84447a9ca8d3432d3102d63c165d377176e) | jordan-gibbs |
| 2026-11-16 | [fix: drop the POSIX PYTHONIOENCODING prefix from generated instructio…](https://github.com/jordan-gibbs/hyperresearch/commit/3c6b7111fefb315c4376923a988b60b04cee25ed) | jordan-gibbs |
| 2026-11-16 | [fix: spare user-authored skill dirs on install prune; clamp MCP resul…](https://github.com/jordan-gibbs/hyperresearch/commit/6b63b941768a872183973415d8db68839bbf470f) | ray910408 |
| 2026-11-12 | [release: v0.13.2 (#204)](https://github.com/jordan-gibbs/hyperresearch/commit/8cd41d1e2f527009d65f73630756142c8262e5e0) | jordan-gibbs |
| 2026-11-12 | [fix: make duplicate-id sync order deterministic (#201)](https://github.com/jordan-gibbs/hyperresearch/commit/fd4718194dbc5906d5f48b471560763efc464408) | jackiectl2 |
| 2026-11-12 | [fix(verify): exclude Sources/References section from citation-density…](https://github.com/jordan-gibbs/hyperresearch/commit/670d09e2572b8d016df39bed034b84187cec951c) | SID-6921 |
| 2026-11-12 | [fix: render literal JSON braces in installed agent prompts (#203)](https://github.com/jordan-gibbs/hyperresearch/commit/d6c531f61a85ddf0188c2fe9f7ab2c4e3d65601c) | rsloveless |
| 2026-11-09 | [release: v0.13.1 (#199)](https://github.com/jordan-gibbs/hyperresearch/commit/db119c3ea2e7a134a20c981d8c6166ab7f5a7396) | jordan-gibbs |

[See all commits ↗](https://github.com/jordan-gibbs/hyperresearch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jordan-gibbs/hyperresearch.git
```
