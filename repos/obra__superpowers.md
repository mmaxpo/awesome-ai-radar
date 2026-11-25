# obra/superpowers

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/obra/superpowers)

> An agentic skills framework & software development methodology that works.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Agentic skills framework & dev methodology — one of the most-starred skill sets |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 326.4k |
| 🍴 **Forks** | 29.0k |
| 🐞 **Open issues + PRs** | [372](https://github.com/obra/superpowers/issues) |
| 💻 **Languages** | Shell 57% · JavaScript 35% · Python 4% · TypeScript 2% · HTML 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `brainstorming` `coding` `obra` `sdlc` `skills` `superpowers` `subagent-driven-development` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-10-09 |
| 📦 **Latest release** | [v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2) — 2026-11-03 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 8.0 MB |

## 📦 Recent releases

### [v7.0.2](https://github.com/obra/superpowers/releases/tag/v7.0.2)
<sub>2026-11-03 · 21d ago</sub>

> This release further tunes brainstorming's questions. It asks fewer of them, starts by asking why, and when there's a choice to make it gives you options to pick from. It also fixes bootstrap problems on six harnesses, and makes the SDD and executing-plans helper scripts much harder to point at the wrong repository or the wrong task.
> **Brainstorming**
> - **It asks a question only when the answer would change what gets built and nothing already answers it.** Otherwise it states its call as a proposal you can correct. It also stops asking about process: writing things up, where files go, whether to look further, and how to show you something are its own calls, and it tells you what it decided. (#2644)
> - **When you haven't said why you want something, that's the first thing it asks.** It asks openly, with no example answers to pick from. (#2644)
> - **When there's a choice it can name, it shows you the options with a recommendation.** In one of our test scenarios, where a spec gives Ctrl+K to two features, 7.0.1 found the conflict every time but asked a bare "which one?" in 8 of 8 runs. This release laid out the options and recommended one in 8 of 8. (#2644)
> - **It reads from how you talk whether you want to discuss the technical choices,** and when your request leaves nothing open, its first message is a short design for you to approve. (#2644)
> …

### [v7.0.1](https://github.com/obra/superpowers/releases/tag/v7.0.1)
<sub>2026-10-21 · 1mo ago</sub>

> This release retunes brainstorming after its rebuild in v7.0.0. Many of you told us, rightly, that the new default questions got annoying fast and felt formulaic. Brainstorming now digs for context before it asks anything, and tries to ask better questions. We expect to keep tuning it, but we think it's better than it was.
> It also trims three long skills so they better survive compaction on Claude Code, and changes the issue and PR templates to ask for a summary written by a human.
> **Brainstorming**
> - **It digs for context first.** In an existing project, or when you point it at a spec, plan, or files, it reads them before its first message and doesn't ask what they already answer. (#2560)
> - **It tries to ask better questions.** v7.0.0 opened every session the same way: an offer to skip the questions, then a generic question about "the moment you wished this existed." Now, when you've already said what you want, it plays your request back with what it found in the project and asks about the one thing still open. Later questions build on your answers and on what it found, and say what the answer would change. (#2560, #2571)
> - **It offers to skip the questions only when it started on its own.** If you asked for brainstorming by name or with `/brainstorming`, it no longer offers to skip it. (#2560)
> …

### [v7.0.0](https://github.com/obra/superpowers/releases/tag/v7.0.0)
<sub>2026-10-10 · 1mo ago</sub>

> We rebuilt brainstorming from scratch so it does a much better job of what it was always for: helping you work out what you actually want and put it into words before anything gets built. The new skill asks you to describe what you're after and why, plays back what it heard so you can correct it, and keeps asking good questions until the picture is clear. Then it matches the process to the work, from just doing it to writing a full design.
> This release also adds a native plugin manifest for the Antigravity Marketplace and fixes Windows hook discovery, Git Bash paths, Hermes skill descriptions, and several smaller bugs.
> **Brainstorming**
> - **Brainstorming draws out what you want before it proposes anything.** Its first message offers to skip the questions and asks one open question about a real moment or a concrete picture. It offers a menu only when you're stuck. Along the way, it offers to look at prior art, your project, or the web. As it understands each part, it plays that part back in a few hundred words and marks its guesses as guesses. (#2463)
> - **It sizes the work after it understands what you want, and says so in plain words.** It does a quick, clear task right away, agrees a small change with you in chat, and writes a design document for a project. You can override its call, and it steps up a size if the work grows. (#2463)
> - **A builder check replaces the spec-document reviewer.** A fresh subagent reads the design as the person who'll build it and lists what they'd still need to ask. Brainstorming answers what it can, makes the minor calls itself and marks them as its own, and brings you the questions that change what gets built, in one round. (#2463)
> …

### [v6.4.2](https://github.com/obra/superpowers/releases/tag/v6.4.2)
<sub>2026-09-25 · 2mo ago</sub>

> `writing-plans` produces leaner plans, faster. Plans now record the decisions an implementer needs (signatures, test assertions, the spec's values) instead of writing out the code. Some frontier models, including Opus 5.5, could get overzealous during plan writing and, with certain prompting, would sometimes try to implement the entire project while designing the plan. The new skill keeps planning focused on the plan. When we reproduced the original report, the scratch builds went away, and plans took a quarter of the time and about a third of the tokens. Thanks to Harper Reed for the report and session bundle. (#2333)
> **Writing Plans**
> - **A plan records decisions. It's not a transcript of the code.** "What a Step Contains" replaces the "No Placeholders" section. A test step names the test and its assertions. A code step gives the exact signature, the file, and the spec's values, and includes a body only for an algorithm those don't determine. A verification step gives the command and its passing output. A reference to another task goes through that task's Interfaces block. Placeholders are still called out as the opposite failure. (#2333)
> - **Self-review checks proportion.** The plan compares its own length to the spec's. A plan several times longer than the spec is a transcript, and when code blocks dominate, bodies get replaced with signatures and test assertions. (#2333)
> - **The plan's reader is described as capable:** an engineer who writes idiomatic code once they know the exact interface and test. This replaces "zero context, questionable taste." Steps are now sized as "one action with a checkable result" instead of "2-5 minutes." (#2333)
> - Every plan written by the new skill executed 9/9 against planted-defect probes on Sonnet 5, the same result as full-code plans. (#2333)
> …

### [v6.4.1](https://github.com/obra/superpowers/releases/tag/v6.4.1)
<sub>2026-09-19 · 2mo ago</sub>

> v6.4.0 was never shipped. v6.4.1 is the first release with these changes. It holds back the new `proving-it-works-with-a-movie` skill, which is getting cleanup and robustness work and will return in a later release.
> The new `diagnosing-superpowers` skill figures out what went wrong in a session. `executing-plans` is rebuilt as Native execution, a cheaper alternative to subagent-driven development. This release also adds support for three new harnesses: OpenCode 2.0, Muse, and Qwen Code.
> **New Skills**
> - **`diagnosing-superpowers`**: when a session goes wrong (repeated work, an ignored plan, a skill that didn't fire, a surprising bill), ask your agent to "figure out what went wrong with superpowers in this session." It pins down the problem with you, reads the transcripts on disk, and reports what happened with `path:line` evidence for every finding. On request it builds a scrubbed bundle or drafts a GitHub issue for your approval, with the cited evidence left intact. Works on the current session or a past one. (#2236, #2287)
> **Executing Plans**
> **Heads up:** `executing-plans` no longer stops every few tasks to check in with you. It runs the whole plan, then gets one review at the end.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-03 | [Release v7.0.2: brainstorming tuning, harness bootstrap fixes, SDD he…](https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7) | obra |
| 2026-10-21 | [Release v7.0.1: brainstorming retune, skills that better survive comp…](https://github.com/obra/superpowers/commit/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) | obra |
| 2026-10-20 | [Templates: require a human-written summary and the filer's instructio…](https://github.com/obra/superpowers/commit/b739a8af570e10a95898f2bdf6cec97467fa6c12) | obra |
| 2026-10-10 | [Release v7.0.0: rebuilt brainstorming, Antigravity Marketplace manife…](https://github.com/obra/superpowers/commit/bb92a77741419a4ab5f06e711a283343f1ada0c3) | obra |
| 2026-09-25 | [Release v6.4.2: leaner plans from writing-plans (#2384)](https://github.com/obra/superpowers/commit/8ca22dba9a94f28898bbce59f2537ff4d87c747d) | obra |
| 2026-09-19 | [Release v6.4.1: diagnosing-superpowers, Native plan execution, OpenCo…](https://github.com/obra/superpowers/commit/5bf4e78011075bcfc0dc295f0724994cd123ee71) | obra |
| 2026-08-12 | [Release v6.3.0: Devin CLI and Hermes Agent support, brainstorming thr…](https://github.com/obra/superpowers/commit/b36e0829c6d0140e93cfef2ca599b1b07d4a7797) | obra |
| 2026-07-28 | [docs: remove the "We're Hiring" section from the README](https://github.com/obra/superpowers/commit/44c9b2d6e889982ac18c27d05a19fefe335194e1) | obra |
| 2026-07-24 | [Release v6.2.0: SDD plan-scoped workspace and resume-based fix loop, …](https://github.com/obra/superpowers/commit/3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9) | obra |
| 2026-07-24 | [fix(systematic-debugging): find-polluter accepts ./-prefixed patterns…](https://github.com/obra/superpowers/commit/c8921b5156562b61af253150a4d1d01a71705be8) | obra |

[See all commits ↗](https://github.com/obra/superpowers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/obra/superpowers.git
```
