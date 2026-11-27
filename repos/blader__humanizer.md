# blader/humanizer

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/blader/humanizer)

> Agent skill that removes signs of AI-generated writing from text

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Skill that removes signs of AI-generated writing |
| **Added** | 2026-11-15 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 74.2k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [9](https://github.com/blader/humanizer/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-writing` `claude-code` `codex` `cursor` `prompt-engineering` `writing-tools` `ai-humanizer` `chatgpt` `claude` `humanize-ai-text` `humanizer` `llm` |
| 🕒 **Last activity** | 2026-11-19 (7d ago) |
| 📅 **Created** | 2026-01-18 |
| 📦 **Latest release** | [v4.0.0](https://github.com/blader/humanizer/releases/tag/v4.0.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 0.3 MB |
| 🌐 **Website** | https://skills.sh/blader/humanizer |

## 📦 Recent releases

### [v4.0.0](https://github.com/blader/humanizer/releases/tag/v4.0.0) — Humanizer v4.0.0
<sub>2026-11-10 · 17d ago</sub>

> Humanizer 4.0.0 lets the skill add a specific detail where the text is generic, and it rewrites the skill's own instructions and examples to be clearer.
> A rewrite may now contain a detail that was not in your text. If you rely on the old rule, stay on v3.1.0.
> **What changed**
> - The skill no longer forbids adding facts. Where the text is generic, it now adds a specific detail it knows to be true. It still keeps every claim the original made and treats a lost or changed claim as an error. This reverses the no-invention rule from 2.9.0. Patterns 14 and 17 follow the same change.
> - Reworked 15 "After" examples in `SKILL.md` and both README examples. Several were vaguer or stiffer than the text they replaced, used phrases from the skill's own watch lists, or changed a stated fact.
> - File mode now reads the whole current file before editing, even one written in the same session. Its summary says how many sections it reviewed, so a partial pass is visible (#326, #327).
> …

### [v3.1.0](https://github.com/blader/humanizer/releases/tag/v3.1.0) — Humanizer v3.1.0
<sub>2026-09-28 · 2mo ago</sub>

> Humanizer 3.1.0 adds a pattern for replies that re-explain what the reader already knows, and it tightens the skill so each rule is stated once.
> **What changed**
> - Added pattern #26 and section F for replies that re-explain context the reader already has (#269). It acts on replies, not standalone writing. 26 patterns total.
> - Extended the core rule so "something the reader did not already have" counts the surrounding conversation, not only earlier text.
> - Widened #25 to text that describes its own sourcing, assembly, or layout (#290), and added headings written for effect to #20.
> - Extended #2 to "That distinction matters." (#277) and to a sentence that explains what an example already showed (#295).
> …

### [v3.0.0](https://github.com/blader/humanizer/releases/tag/v3.0.0) — Humanizer v3.0.0
<sub>2026-09-06 · 2mo ago</sub>

> Humanizer 3.0.0 rebuilds the skill around one account of why AI text sounds the way it does, and consolidates 35 patterns into 25 with nothing dropped.
> **What changed**
> - **One account up front.** The skill opens with why AI text sounds the way it does: a model makes the choice that fits the widest range of readers, and every tell is a form of that default. Two rules follow: every kept sentence must add something the reader did not have, and a tell counts in proportion to how rarely a careful writer would make it on purpose.
> - **Patterns grouped in five sections and ordered by strength and frequency.** Staging instead of stating (1 to 5), Rhythm by rule (6 to 11), Inflation and borrowed authority (12 to 18), Formatting by rule (19 to 21), Leftovers from the chat and the draft (22 to 25). The not-X-but-Y contrast and the one-line closer come first and get the fullest treatment: every variant named, the paragraph-scale form, a one-sighting rule, and a final scan step.
> - **Duplicate guidance merged.** The workflow is one section instead of five. The dash rule is stated once. Each false-positive guard lives inside the pattern it guards, marked *weak alone* where one sighting should not trigger an edit.
> - **Aligned with the current Wikipedia article.** Dropped false ranges and synonym cycling, which Wikipedia now lists as a human habit and a historical indicator. Added vague connection or association. Extended the watch lists for words, notability, copulatives, sales language, disclaimers, and Markdown formatting. Moved dashes below triads.
> …

### [v2.11.1](https://github.com/blader/humanizer/releases/tag/v2.11.1) — Humanizer v2.11.1
<sub>2026-08-18 · 3mo ago</sub>

> Claude Desktop can now install or replace Humanizer from the `humanizer-skill.zip` release asset. The archive contains one regular `humanizer/SKILL.md` file and no symbolic links, while the plugin package keeps its single canonical prompt.
> Fixes #224.

### [v2.11.0](https://github.com/blader/humanizer/releases/tag/v2.11.0) — Humanizer v2.11.0
<sub>2026-08-17 · 3mo ago</sub>

> Humanizer now uses Plain Language throughout the skill and repository.
> **Highlights**
> - Rewrote the runtime skill with shorter sentences, common words, active voice, and clearer headings.
> - Shortened `SKILL.md` by about 750 words.
> - Rewrote the README, repo guidance, agent metadata, plugin descriptions, workflow labels, and validation messages.
> - Added a checked Plain Language contract for future changes.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Merge pull request #344 from kelsey-fecho/patch-1](https://github.com/blader/humanizer/commit/a32f24407364c74c812b43c15926d638bee1e072) | blader |
| 2026-11-19 | [Enhance cfo.ai link in README](https://github.com/blader/humanizer/commit/a91adfa20ca2f1538d93c88b640fb21735fd4fe7) | kelsey-fecho |
| 2026-11-19 | [Merge pull request #318 from wahid-slimani/informal-text-and-cross-ge…](https://github.com/blader/humanizer/commit/a48c60c2a3f7a0f6ecc8f9b8d2b1ef71c7927155) | blader |
| 2026-11-19 | [Stop over-editing informal human text](https://github.com/blader/humanizer/commit/3e5f816b5609c4002aebb69f12c6476fe3347d0a) | wahid-slimani |
| 2026-11-19 | [Merge pull request #342 from TanmayShah29/fix/340-duplicate-pattern-n…](https://github.com/blader/humanizer/commit/3a06208d7f8e57f2f4378e79c233cd52ecba5c0e) | blader |
| 2026-11-19 | [Fail validation when a pattern number repeats](https://github.com/blader/humanizer/commit/1d09f33e3fc9bdb90b9c85f90db2cb98cbe11739) | TanmayShah29 |
| 2026-11-19 | [Merge pull request #343 from blader/improve-skill-and-readme](https://github.com/blader/humanizer/commit/732e48abbe80850a74d0a1e2c4b9b6c926213161) | blader |
| 2026-11-19 | [Tighten skill and README wording, polish After examples, and add 'the…](https://github.com/blader/humanizer/commit/3d556c3b5af1691b0976f4945d41018f845abf2c) | blader |
| 2026-11-10 | [Merge pull request #333 from blader/release-4.0.0](https://github.com/blader/humanizer/commit/b48c832f0f809c1b5658edbb838c2521b72f2413) | blader |
| 2026-11-10 | [Release 4.0.0](https://github.com/blader/humanizer/commit/8b067c507fd14e9472164511fd0f77258ee46136) | blader |

[See all commits ↗](https://github.com/blader/humanizer/commits)

## ⬇️ Get it

```bash
git clone https://github.com/blader/humanizer.git
```
