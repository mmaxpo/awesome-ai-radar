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
| ⭐ **Stars** | 334.1k |
| 🍴 **Forks** | 28.1k |
| 🐞 **Open issues + PRs** | [255](https://github.com/mattpocock/skills/issues) |
| 💻 **Languages** | Shell 67% · JavaScript 33% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (2d ago) |
| 📅 **Created** | 2026-02-03 |
| 📦 **Latest release** | [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2) — 2026-10-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2.4 MB |
| 🌐 **Website** | https://aihero.dev/skills |

## 📦 Recent releases

### [v1.3.2](https://github.com/mattpocock/skills/releases/tag/v1.3.2)
<sub>2026-10-29 · 29d ago</sub>

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
| 2026-11-25 | [Merge pull request #1485 from mattpocock/glossary-bold-terms](https://github.com/mattpocock/skills/commit/6f7f7831a625f040a8e06a0e7954826b87ce775a) | mattpocock |
| 2026-11-25 | [domain-modeling: express term relationships inside definitions](https://github.com/mattpocock/skills/commit/2b7ab8c9471fad3fca0a9c0c9e1f52153408172b) | bot |
| 2026-11-24 | [Merge pull request #1474 from mattpocock/chief-of-staff-soften](https://github.com/mattpocock/skills/commit/d65391149dbb5fe76478e76fa8d5122b2aa5a70e) | mattpocock |
| 2026-11-24 | [chief-of-staff: delegate the work, offer convention fixes](https://github.com/mattpocock/skills/commit/742afa6b936d17c8dcc790748840e4992edd42fa) | bot |
| 2026-11-24 | [chief-of-staff: relay target, friction-only offers, keep conversation](https://github.com/mattpocock/skills/commit/419dac71f1dfe95e378bc1009f0b0fad2a3cb6ed) | bot |
| 2026-11-24 | [Merge pull request #1473 from mattpocock/chief-of-staff-delegate-reme…](https://github.com/mattpocock/skills/commit/6bb33ef4dd4f12cec18a1a4b7f1446508e624bb2) | mattpocock |
| 2026-11-24 | [chief-of-staff: refocus on delegate and remember](https://github.com/mattpocock/skills/commit/4edd64a19537607848e8ab999f95a370d3af8a49) | bot |
| 2026-11-19 | [Merge pull request #1455 from mattpocock/ci-frontmatter-check](https://github.com/mattpocock/skills/commit/abeeaf95660ba9e8b7c753eb38f441ca707a8823) | mattpocock |
| 2026-11-19 | [ci: check every SKILL.md's frontmatter parses with the installer's YA…](https://github.com/mattpocock/skills/commit/37209058e45b7c60b36218b7392df0ebcceb247a) | bot |
| 2026-11-19 | [Merge pull request #1453 from mattpocock/fix-software-factory-frontma…](https://github.com/mattpocock/skills/commit/3a05171775a49076900759e0dd1b3ef8e2671323) | mattpocock |

[See all commits ↗](https://github.com/mattpocock/skills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mattpocock/skills.git
```
