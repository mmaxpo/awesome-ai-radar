# Fission-AI/OpenSpec

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Fission-AI/OpenSpec)

> Spec-driven development (SDD) for AI coding assistants.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Spec-driven development for AI coding assistants |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 75.9k |
| 🍴 **Forks** | 5.2k |
| 🐞 **Open issues + PRs** | [218](https://github.com/Fission-AI/OpenSpec/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `spec` `ai` `context-engineering` `engineering` `planning` `prd` `sdlc` `spec-driven-development` `specification` `sdd` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2025-08-05 |
| 📦 **Latest release** | [v2.2.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.2.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 13.2 MB |
| 🌐 **Website** | https://openspec.dev/ |

## 📦 Recent releases

### [v2.2.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.2.0) — v2.2.0 - The /openspec skill router
<sub>2026-11-24 · 2d ago</sub>

> **What's New in v2.2.0**
> **OpenSpec now has a skill router.** Type `/openspec`, say what you want, and the router picks the right OpenSpec skill and runs it.
> **How to upgrade**
> Run `openspec update`. The update adds the `openspec` router skill and changes no other skill.
> **New: the `/openspec` skill router**
> - **One command for everything** - `/openspec` accepts any OpenSpec request in plain words. In Codex the command is `$openspec`.
> …

### [v2.1.1](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.1.1) — v2.1.1 - Offline skill installs, safer archive
<sub>2026-11-19 · 7d ago</sub>

> **OpenSpec 2.1.1**
> This release smooths out a handful of rough edges. Skills now install straight from the CLI, with no Git and no network needed. Archive is more careful with your main specs, and `validate --strict` catches two problems before they reach archive. Your workflows don't change.
> **How to upgrade**
> Update the OpenSpec CLI, then run this in each project:
> ```bash
> openspec update
> …

### [v2.1.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.1.0) — v2.1.0 - Global skills
<sub>2026-11-17 · 10d ago</sub>

> **OpenSpec 2.1**
> OpenSpec now supports global skills for coding agents. Install the skills once and your agent can use them in every project on your machine.
> As more teams adopt Vercel’s `skills` installer, it’s becoming a common way to install skills across coding tools. OpenSpec is adopting it too, so we can spend less time maintaining installer code and more time improving the skills themselves.
> The OpenSpec workflows themselves haven't changed.
> **What changed**
> - **Skills can be installed globally.** Vercel’s installer handles the location for each supported agent, whether it reads `~/.agents/skills/` or uses its own folder.
> …

### [v2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0) — v2.0.0 - Skills in .agents/skills, /opsx commands removed
<sub>2026-11-11 · 15d ago</sub>

> **OpenSpec 2.0**
> OpenSpec now installs skills in `.agents/skills/` instead of keeping a separate copy for each coding agent. Tools that don't read this folder, like Claude Code and Kiro, get links to the same skills.
> We're also removing the `/opsx:*` slash commands. Each command already has a matching skill, so there's no need to maintain both.
> The OpenSpec workflows themselves haven't changed.
> **What changed**
> - **Skills are installed in `.agents/skills/`.** Every tool uses the same skills, without duplicate files across folders.
> …

### [v1.17.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v1.17.0) — v1.17.0 - Safe upgrades, 2.0 notice
<sub>2026-11-09 · 17d ago</sub>

> **What's New in v1.17.0**
> `openspec update` now upgrades a project from any older release in one run, and announces that command files go away in OpenSpec 2.0.
> > **Heads-up: command files (`/opsx:*`) go away in OpenSpec 2.0.** Your OpenSpec skills stay and do the same work. To switch now, run `openspec config set delivery skills && openspec update`. The plan is in [#2022](https://github.com/Fission-AI/OpenSpec/issues/2022).
> **New**
> - **2.0 notice** - While a configured tool still gets command files, `openspec update` ends with a short notice that they go away in 2.0, plus the one command to switch early. It stays silent once you use skills only, and for tools without command files, such as Codex.
> **Improved**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Version Packages (#2301)](https://github.com/Fission-AI/OpenSpec/commit/f1cd852f4edce22b8df9548a4df889172ca8ff25) | openspec-release-bot[bot] |
| 2026-11-24 | [fix(install): retry the move when Windows still has the new exe locke…](https://github.com/Fission-AI/OpenSpec/commit/b30672cce4937f0a598dd793ae1a5eda23606e25) | clay-good |
| 2026-11-24 | [feat(skills): add an /openspec router with references, keeping every …](https://github.com/Fission-AI/OpenSpec/commit/8ad4406a7f47b7d66b66b3b52ed4eef1de7a2a7f) | clay-good |
| 2026-11-24 | [chore(deps-dev): bump vitest and @vitest/ui to 5.1.1 (#2296)](https://github.com/Fission-AI/OpenSpec/commit/1f846e64b0dffa47e0590078cfc7121cc7f59f7b) | clay-good |
| 2026-11-24 | [chore(deps): bump the website-dependencies group (#2294)](https://github.com/Fission-AI/OpenSpec/commit/4abd55cea98acd8e587abd8d4f6bb9fbe3687ea5) | dependabot[bot] |
| 2026-11-19 | [Version Packages (#2284)](https://github.com/Fission-AI/OpenSpec/commit/0c737dc1b543249b38b0f4716816fcf493d894dd) | openspec-release-bot[bot] |
| 2026-11-19 | [fix(update): refresh skills that npx skills put in a project (#2269)](https://github.com/Fission-AI/OpenSpec/commit/a0993e9d56d503148f13b10ea0e8f4eec2f8ce68) | clay-good |
| 2026-11-19 | [fix(skills): install skills from the npm package instead of cloning (…](https://github.com/Fission-AI/OpenSpec/commit/4ff226bbd11645b7c6ae48332f8c87ff94212aa1) | clay-good |
| 2026-11-19 | [fix(skills): hand off to apply when continue completes planning (#2274)](https://github.com/Fission-AI/OpenSpec/commit/ad0579d3ff89459154220b68a834aed125d9c1f2) | clay-good |
| 2026-11-18 | [fix(archive): check the archive target before syncing specs (#2277)](https://github.com/Fission-AI/OpenSpec/commit/e6539de023915e36848b351ea737ca8e192e8538) | clay-good |

[See all commits ↗](https://github.com/Fission-AI/OpenSpec/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Fission-AI/OpenSpec.git
```
