# mattpocock/skills

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/mattpocock/skills)

> Skills for Real Engineers. Straight from my .agents directory.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Matt Pocock's agent skills |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 324.3k |
| 🍴 **Forks** | 27.2k |
| 🐞 **Open issues + PRs** | [243](https://github.com/mattpocock/skills/issues) |
| 💻 **Languages** | Shell 73% · JavaScript 27% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-13 (yesterday) |
| 📅 **Created** | 2026-02-03 |
| 📦 **Latest release** | [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2) — 2026-10-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2.3 MB |
| 🌐 **Website** | https://aihero.dev/skills |

## 📦 Recent releases

### [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2)
<sub>2026-10-29 · 16d ago</sub>

> **Patch Changes**
> - [#1194](https://github.com/mattpocock/skills/pull/1194) [`b645f47`](https://github.com/mattpocock/skills/commit/b645f47de3e17ed3bf60586c9bebb8092e0f79fd) Thanks [@mattpocock](https://github.com/mattpocock)! - `ask-matt` now reads a skill's `SKILL.md` before stating what it does or recommending a step be skipped, instead of trusting its own one-line summaries ([#614](https://github.com/mattpocock/skills/issues/614)).
> - [#1304](https://github.com/mattpocock/skills/pull/1304) [`5beb35b`](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) Thanks [@mattpocock](https://github.com/mattpocock)! - `chief-of-staff` now keeps its memory in an LLM wiki (an `index.md` plus one page per topic, maintained through ingest, query and lint) and writes it as a historical record: every claim is dated, and every claim about code cites the commit it was true at.
> - [#1208](https://github.com/mattpocock/skills/pull/1208) [`3da8c01`](https://github.com/mattpocock/skills/commit/3da8c01116264675eeefbd6e9d59c734de9095cc) Thanks [@mattpocock](https://github.com/mattpocock)! - `code-review` now searches the repo for standards files and always hands `CODING_STANDARDS.md` / `CONTRIBUTING.md` to the Standards sub-agent ([#1065](https://github.com/mattpocock/skills/issues/1065)), runs both sub-agents in the foreground and uses their returned reports ([#1073](https://github.com/mattpocock/skills/issues/1073)), and resolves the issue tracker through the provided tracker doc instead of a hard-coded path ([#937](https://github.com/mattpocock/skills/issues/937)).
> - [#1209](https://github.com/mattpocock/skills/pull/1209) [`f3fc563`](https://github.com/mattpocock/skills/commit/f3fc5632f401156837ee3872f14fe33ccf1024ea) Thanks [@mattpocock](https://github.com/mattpocock)! - `diagnosing-bugs` Phase 5 now has the agent `diff` a forced mutation against a pristine copy before trusting the red, so an edit that silently changed nothing can't pass as a failing test ([#955](https://github.com/mattpocock/skills/issues/955)).
> - [#1187](https://github.com/mattpocock/skills/pull/1187) [`e0efb6e`](https://github.com/mattpocock/skills/commit/e0efb6e7435ebb420d8a25d6816ed1ebaa2d23d2) Thanks [@mattpocock](https://github.com/mattpocock)! - Fixed the GitHub tracker template's external-PR listing, which failed on `authorAssociation` ([#468](https://github.com/mattpocock/skills/issues/468), thanks @lofi-coding). Re-run `/setup-matt-pocock-skills` to refresh `docs/agents/issue-tracker.md`.
> …

### [v1.3.1](https://github.com/mattpocock/skills/releases/tag/v1.3.1)
<sub>2026-10-04 · 1mo ago</sub>

> **Minor Changes**
> - [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`implement-spec`** into the **Engineering** bucket, so it ships in the Claude Code plugin, gets a docs page, and is routed by `ask-matt` as the parallel alternative to per-ticket `implement`.
>   `implement-spec` (user-invoked) implements a whole spec in one run. It reads the tickets as a **task graph**, runs implementer subagents in their own worktrees across the ready **frontier**, and lands everything on one **integration branch**, closing out with `code-review`. Ahead of graduating:
>   - The goal is now the integration branch, not a PR. A draft PR opens only when the issue tracker closes work through PRs or you ask for one, and only after the first merge (a branch with no commits ahead of main can't open one). Without a PR, the tickets are resolved the way the tracker closes work.
>   - It points at the issue tracker like its siblings, telling you to run `/setup-matt-pocock-skills` when none has been provided, rather than silently defaulting to `gh`.
>   - Each implementer confirms its worktree is based on the integration branch, builds its ticket with `tdd`, and merges the integration tip into its own branch before reporting done, so each merge is a fast-forward.
> …

### [v1.3.0](https://github.com/mattpocock/skills/releases/tag/v1.3.0)
<sub>2026-10-04 · 1mo ago</sub>

> **Minor Changes**
> - [#1120](https://github.com/mattpocock/skills/pull/1120) [`2aecca1`](https://github.com/mattpocock/skills/commit/2aecca12ea9ff047f76c8178cb64dfeafd192abe) Thanks [@mattpocock](https://github.com/mattpocock)! - Graduate **`implement-spec`** into the **Engineering** bucket, so it ships in the Claude Code plugin, gets a docs page, and is routed by `ask-matt` as the parallel alternative to per-ticket `implement`.
>   `implement-spec` (user-invoked) implements a whole spec in one run. It reads the tickets as a **task graph**, runs implementer subagents in their own worktrees across the ready **frontier**, and lands everything on one **integration branch**, closing out with `code-review`. Ahead of graduating:
>   - The goal is now the integration branch, not a PR. A draft PR opens only when the issue tracker closes work through PRs or you ask for one, and only after the first merge (a branch with no commits ahead of main can't open one). Without a PR, the tickets are resolved the way the tracker closes work.
>   - It points at the issue tracker like its siblings, telling you to run `/setup-matt-pocock-skills` when none has been provided, rather than silently defaulting to `gh`.
>   - Each implementer confirms its worktree is based on the integration branch, builds its ticket with `tdd`, and merges the integration tip into its own branch before reporting done, so each merge is a fast-forward.
> …

### [v1.2.3](https://github.com/mattpocock/skills/releases/tag/v1.2.3)
<sub>2026-08-06 · 3mo ago</sub>

> **Patch Changes**
> - [#779](https://github.com/mattpocock/skills/pull/779) [`efce423`](https://github.com/mattpocock/skills/commit/efce423018fc6468a3239621f1c1bcaacc723801) Thanks [@mattpocock](https://github.com/mattpocock)! - Make `diagnosing-bugs` redact secrets.
>   - Add a **Redact** section to `SKILL.md`. The skill has the agent show commands, outputs and captured artifacts; the section makes redaction the first move on each — write `<REDACTED>`, build loops against env vars so the credential stays in the environment, and quote only the signal-carrying lines of a captured artifact.
>   - The Phase 1 completion criterion said "paste the invocation and its output". It now says show it redacted, and Phase 1 asks the user for a **redacted** captured artifact.
>   - Note in `scripts/hitl-loop.template.sh` that `capture` prints its value back to the terminal, so it takes observations while signing in stays a `step`.
> - [#781](https://github.com/mattpocock/skills/pull/781) [`14bfbbd`](https://github.com/mattpocock/skills/commit/14bfbbd8654a8d2910299e1a004c19c1979687d8) Thanks [@mattpocock](https://github.com/mattpocock)! - Drop Claude Code's tool and agent-type names from the subagent-dispatch instructions in `code-review`, `codebase-design`, and `improve-codebase-architecture`, so the step is followable on Codex and other harnesses.
> …

### [v1.2.2](https://github.com/mattpocock/skills/releases/tag/v1.2.2)
<sub>2026-08-05 · 3mo ago</sub>

> **Patch Changes**
> - [#766](https://github.com/mattpocock/skills/pull/766) [`4aaccb5`](https://github.com/mattpocock/skills/commit/4aaccb58d40559d7e3c59a029b2290ae5ba538de) Thanks [@mattpocock](https://github.com/mattpocock)! - Make `writing-for-agents` model-invokable in Codex again.
>   - Drop `policy.allow_implicit_invocation: false` from `agents/openai.yaml`. Codex filtered the skill out of the model-visible skills list, so its description could not trigger it — only an explicit `$writing-for-agents` mention worked.
>   - Update the stale `interface.display_name` and `interface.short_description`, which still named the old `writing-great-skills` skill.
>   - Move the skill from the **User-invoked** list to the **Model-invoked** list in `README.md` and `skills/productivity/README.md`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [Merge pull request #1416 from mattpocock/software-factory-task-wording](https://github.com/mattpocock/skills/commit/5863806dd4e15c63174bee4e7515a4256792ecfa) | mattpocock |
| 2026-11-11 | [software-factory: "job" is the CI vendor's word; explore leaves findings](https://github.com/mattpocock/skills/commit/d18183fe9d96e1240105a8534e53591e9b49afd7) | Matt Pocock |
| 2026-10-31 | [software-factory: glossary skill for designing a factory (#1316)](https://github.com/mattpocock/skills/commit/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) | mattpocock |
| 2026-10-31 | [chief-of-staff: shared wiki first; retro and implement-spec as proced…](https://github.com/mattpocock/skills/commit/5ae481693d13b37d4d2c2c92d0b66d299c93e695) | mattpocock |
| 2026-10-29 | [implement-spec: a fresh implementer subagent per ticket (#1342)](https://github.com/mattpocock/skills/commit/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) | mattpocock |
| 2026-10-29 | [chore: version skills (#1161)](https://github.com/mattpocock/skills/commit/d1478fcb140db0b93c0c8df17bcfd311844749d0) | github-actions[bot] |
| 2026-10-29 | [Start subagents with a fresh context window, not a fork (#1341)](https://github.com/mattpocock/skills/commit/7739eaed7f8f3915437a8def198a6d0d7206dbc7) | mattpocock |
| 2026-10-27 | [Close blank issues and route requests by kind (#1169)](https://github.com/mattpocock/skills/commit/59db609eb1e18aaf59b63284d0e52255aff0c63c) | mattpocock |
| 2026-10-27 | [setup-matt-pocock-skills: reachable repo, legacy CONTEXT.md, tracker …](https://github.com/mattpocock/skills/commit/ed0de59eb5de8c2730a650cc69f588ffa64c1040) | mattpocock |
| 2026-10-19 | [chief-of-staff: keep memory in a dated, commit-cited wiki (#1304)](https://github.com/mattpocock/skills/commit/5beb35b040e3de97e54fa9e386d7e42d15c295c2) | mattpocock |

[See all commits ↗](https://github.com/mattpocock/skills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mattpocock/skills.git
```
