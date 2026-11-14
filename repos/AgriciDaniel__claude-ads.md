# AgriciDaniel/claude-ads

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/AgriciDaniel/claude-ads)

> Claude-first paid-media operations skill for Claude Code across 12 ad platforms (Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, X): source-grounded audits, deterministic findings and evidence coverage, versioned JSON reports, and capability-gated account changes.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Claude Code skill for paid-ads work across 12 ad platforms |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 11.0k |
| 🍴 **Forks** | 1.6k |
| 🐞 **Open issues + PRs** | [5](https://github.com/AgriciDaniel/claude-ads/issues) |
| 💻 **Languages** | Python 84% · JavaScript 8% · TypeScript 4% · Shell 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `claude-code` `claude-code-skill` `ai-marketing` `ai` `marketing-automation` `open-source` `agent-skills` `google-ads` `meta-ads` `paid-advertising` `ppc` |
| 🕒 **Last activity** | 2026-11-01 (12d ago) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v2.1.0](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.1.0) — 2026-10-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 6.0 MB |
| 🌐 **Website** | skool.com/ai-marketing-hub-pro |

## 📦 Recent releases

### [v2.1.0](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.1.0) — v2.1.0: Cockpit companion, routing, evidence and installer updates
<sub>2026-10-16 · 28d ago</sub>

> **Claude Ads v2.1.0**
> This update adds the optional Cockpit companion, sharper command routing, fresher platform evidence, safer installers, and a plain-language README.
> - **Claude Ads Cockpit (optional, off by default).** A local workbench that opens next to Claude Code and shows a finished audit at a glance: how much of the audit could be judged, a meter per platform and per topic, and what to fix first. Open a check to read what was seen, what it means, and what to do. It also covers input files, comparison with an earlier run, and report receipts. Every screen fits the pane without scrolling. It never writes to ad accounts. Try it with the synthetic demo: `/ads-cockpit demo`.
> - **Routing.** Every `/ads` command maps to one named skill, each contested trigger phrase has one owner, and the copy, strategy, and format agents are read-only.
> - **Current evidence.** Platform references and ledgers were refreshed on 12 and 16 October 2026, including Microsoft SOAP support through 31 January 2027, Google Smart Campaigns, Reddit lead forms, the LinkedIn API schedule, Apple, Meta, Pinterest, and EU AI Act timing.
> - **Installers.** Temporary directories are cleaned up on every exit path, `--ref` (`-Ref` in PowerShell) pins a git install to an exact commit and fails closed, and `install.sh --source=git` no longer refuses its own clone on macOS.
> …

### [v2.0.2](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.0.2) — v2.0.2: report safety, platform fixes, and installer improvements
<sub>2026-09-10 · 2mo ago</sub>

> **Claude Ads v2.0.2**
> This update improves installation guidance, report safety, platform evidence, and release validation.
> - Adds Google Search/DSA overlap and duplicate-keyword checks based on account routing evidence.
> - Makes Meta planning and creative workflows distinguish account, Pixel, and conversion cold starts.
> - Corrects Microsoft native-export conversion mapping to ConversionsQualified.
> - Escapes untrusted PDF report text and captions.
> …

### [v2.0.1](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.0.1) — v2.0.1: public mirror release
<sub>2026-07-13 · 4mo ago</sub>

> Claude Ads v2 goes public. This is a documentation and metadata patch on top of [v2.0.0](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.0.0), adapting the release surface for the public repository. No code-contract, scoring, catalog, or behavior changes.
> **Changed**
> - User-facing repository links (README install paths, `SUPPORT.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, issue templates, `CITATION.cff`, plugin and marketplace manifests) now point to this public repository, so installation, issues, discussions, and private vulnerability reporting work without AI-Marketing-Hub org access.
> - Installer default clone source (`install.sh`, `install.ps1`) retargeted to this repository.
> - PDF report footer and page-fetch User-Agent contact URL now reference this repository.
> - README documents the dual-distribution model and the native Claude Code plugin flow.
> …

### [v2.0.0](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.0.0) — v2.0.0: 12-platform paid-media operating skill
<sub>2026-07-13 · 4mo ago</sub>

> Major architecture release: professional paid-media operations across 12 advertising platforms, source-grounded and safe by default.
> **Highlights**
> - One skill covering Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, and X.
> - Read-only by default; account mutations require preview, approval, idempotency, verification, and rollback.
> - Every platform claim ties to a dated source via the source and claim ledgers.
> **Added**
> …

### [v1.8.1](https://github.com/AgriciDaniel/claude-ads/releases/tag/v1.8.1) — v1.8.1 — docs + metadata patch
<sub>2026-07-13 · 4mo ago</sub>

> Documentation and metadata patch on top of v1.8.0. No code, check-catalog, or
> behavior changes; 59/59 pytest still green. (Caught by a post-ship review.)
> **Fixed**
> * **README "What's new" section** updated from v1.7.0 (Wave 2) to v1.8.0 (Wave 3): the +91 checks (catalog 300), the new `audit-regulatory-compliance` agent, and the agentic-era reference docs. It had been left headlining the prior release.
> * **Stale test count corrected: 41 to 59** (actual pytest collected and passing) in README, `CITATION.cff`, `plugin.json`, and `marketplace.json`. The v1.7.0 CHANGELOG entry retains 41 (accurate for that release).
> * **Roadmap framing** refreshed: v1.8.0 is shipped / current, not "in active development"; removed the inaccurate "v1.8.0 visual system" diagram alt-text.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-17 | [Merge pull request #96 from AgriciDaniel/claude/ci-speed](https://github.com/AgriciDaniel/claude-ads/commit/fc3908e786c318776df89a3a098333da377364be) | AgriciDaniel |
| 2026-10-17 | [chore(deps): group action updates and stop routine pip bumps](https://github.com/AgriciDaniel/claude-ads/commit/73428b8d35e035bafc8a38513e9bb620898a2452) | AgriciDaniel |
| 2026-10-16 | [ci: cancel superseded PR runs and stop Intel macOS timeouts](https://github.com/AgriciDaniel/claude-ads/commit/3e3276a734805bfcef803f4bb0a272b5f49691cf) | AgriciDaniel |
| 2026-10-16 | [release: Claude Ads 2.1.0 (#92)](https://github.com/AgriciDaniel/claude-ads/commit/77304e24bba6f3cc39eaa96d893b4018814ddc64) | AgriciDaniel |
| 2026-10-16 | [release: Claude Ads 2.1.0](https://github.com/AgriciDaniel/claude-ads/commit/4a74a5a2237caf2bc81091108164fe20e178818c) | AgriciDaniel |
| 2026-10-16 | [Merge pull request #91 from AgriciDaniel/codex/ads-cockpit-v1](https://github.com/AgriciDaniel/claude-ads/commit/2d304bd9f35d81e65175a8157acab9d7f7f32c5b) | AgriciDaniel |
| 2026-10-16 | [feat(cockpit): screens that fit, a story Overview, paging and a plain…](https://github.com/AgriciDaniel/claude-ads/commit/93b23c6578525758532af8626e5bbf31e8d1e311) | AgriciDaniel |
| 2026-10-16 | [docs(evidence): refresh the LinkedIn API lifecycle claim after the 20…](https://github.com/AgriciDaniel/claude-ads/commit/4c3f13e9da6c6188fe7942765c079a7f04ebb5c8) | AgriciDaniel |
| 2026-10-16 | [docs: stop advertising deterministic scoring, link the unreachable re…](https://github.com/AgriciDaniel/claude-ads/commit/ba683f7b04e1a57cb022a4ae73a3db4a076af4e2) | AgriciDaniel |
| 2026-10-16 | [docs(readme): cycle the typed command through all twelve platforms, m…](https://github.com/AgriciDaniel/claude-ads/commit/8c3700c9896f279146ffb532c28e5ba64b27ab89) | AgriciDaniel |

[See all commits ↗](https://github.com/AgriciDaniel/claude-ads/commits)

## ⬇️ Get it

```bash
git clone https://github.com/AgriciDaniel/claude-ads.git
```
