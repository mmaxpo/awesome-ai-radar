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
| ⭐ **Stars** | 75.4k |
| 🍴 **Forks** | 5.2k |
| 🐞 **Open issues + PRs** | [209](https://github.com/Fission-AI/OpenSpec/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `spec` `ai` `context-engineering` `engineering` `planning` `prd` `sdlc` `spec-driven-development` `specification` `sdd` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2025-08-05 |
| 📦 **Latest release** | [v2.1.1](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.1.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 12.9 MB |
| 🌐 **Website** | https://openspec.dev/ |

## 📦 Recent releases

### [v2.1.1](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.1.1) — v2.1.1 - Offline skill installs, safer archive
<sub>2026-11-19 · 2d ago</sub>

> **OpenSpec 2.1.1**
> This release smooths out a handful of rough edges. Skills now install straight from the CLI, with no Git and no network needed. Archive is more careful with your main specs, and `validate --strict` catches two problems before they reach archive. Your workflows don't change.
> **How to upgrade**
> Update the OpenSpec CLI, then run this in each project:
> ```bash
> openspec update
> …

### [v2.1.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.1.0) — v2.1.0 - Global skills
<sub>2026-11-17 · 5d ago</sub>

> **OpenSpec 2.1**
> OpenSpec now supports global skills for coding agents. Install the skills once and your agent can use them in every project on your machine.
> As more teams adopt Vercel’s `skills` installer, it’s becoming a common way to install skills across coding tools. OpenSpec is adopting it too, so we can spend less time maintaining installer code and more time improving the skills themselves.
> The OpenSpec workflows themselves haven't changed.
> **What changed**
> - **Skills can be installed globally.** Vercel’s installer handles the location for each supported agent, whether it reads `~/.agents/skills/` or uses its own folder.
> …

### [v2.0.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v2.0.0) — v2.0.0 - Skills in .agents/skills, /opsx commands removed
<sub>2026-11-11 · 10d ago</sub>

> **OpenSpec 2.0**
> OpenSpec now installs skills in `.agents/skills/` instead of keeping a separate copy for each coding agent. Tools that don't read this folder, like Claude Code and Kiro, get links to the same skills.
> We're also removing the `/opsx:*` slash commands. Each command already has a matching skill, so there's no need to maintain both.
> The OpenSpec workflows themselves haven't changed.
> **What changed**
> - **Skills are installed in `.agents/skills/`.** Every tool uses the same skills, without duplicate files across folders.
> …

### [v1.17.0](https://github.com/Fission-AI/OpenSpec/releases/tag/v1.17.0) — v1.17.0 - Safe upgrades, 2.0 notice
<sub>2026-11-09 · 12d ago</sub>

> **What's New in v1.17.0**
> `openspec update` now upgrades a project from any older release in one run, and announces that command files go away in OpenSpec 2.0.
> > **Heads-up: command files (`/opsx:*`) go away in OpenSpec 2.0.** Your OpenSpec skills stay and do the same work. To switch now, run `openspec config set delivery skills && openspec update`. The plan is in [#2022](https://github.com/Fission-AI/OpenSpec/issues/2022).
> **New**
> - **2.0 notice** - While a configured tool still gets command files, `openspec update` ends with a short notice that they go away in 2.0, plus the one command to switch early. It stays silent once you use skills only, and for tools without command files, such as Codex.
> **Improved**
> …

### [v1.16.1](https://github.com/Fission-AI/OpenSpec/releases/tag/v1.16.1) — v1.16.1 - Spec parsing, version checks
<sub>2026-11-07 · 15d ago</sub>

> **What's New in v1.16.1**
> A patch release that makes spec validation stricter and more forgiving in the right places, and makes `openspec version --check` reliable.
> **Fixed**
> - **Closed section headings** - `validate`, `show`, `list`, `view` and `archive` now read headings with a closing `#` run (`## Purpose ##`, `## ADDED Requirements ##`) the same as their unclosed forms.
> - **Unrecognized delta sections** - `validate` now fails, and `archive` refuses, when a delta spec puts a requirement under an unrecognized section such as `## DEPRECATED Requirements`, instead of passing with a warning and silently dropping that requirement.
> - **Version check with telemetry off** - `openspec version --check` now checks for a newer version even when telemetry is off or it runs in CI. Only `OPENSPEC_NO_UPDATE_CHECK` skips it; the background check in `openspec update` still honors the telemetry opt-out and CI.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Version Packages (#2284)](https://github.com/Fission-AI/OpenSpec/commit/0c737dc1b543249b38b0f4716816fcf493d894dd) | openspec-release-bot[bot] |
| 2026-11-19 | [fix(update): refresh skills that npx skills put in a project (#2269)](https://github.com/Fission-AI/OpenSpec/commit/a0993e9d56d503148f13b10ea0e8f4eec2f8ce68) | clay-good |
| 2026-11-19 | [fix(skills): install skills from the npm package instead of cloning (…](https://github.com/Fission-AI/OpenSpec/commit/4ff226bbd11645b7c6ae48332f8c87ff94212aa1) | clay-good |
| 2026-11-19 | [fix(skills): hand off to apply when continue completes planning (#2274)](https://github.com/Fission-AI/OpenSpec/commit/ad0579d3ff89459154220b68a834aed125d9c1f2) | clay-good |
| 2026-11-18 | [fix(archive): check the archive target before syncing specs (#2277)](https://github.com/Fission-AI/OpenSpec/commit/e6539de023915e36848b351ea737ca8e192e8538) | clay-good |
| 2026-11-18 | [fix(validate): allow frontmatter at the top of delta specs (#2273)](https://github.com/Fission-AI/OpenSpec/commit/e0fdff34466f1adf93d90cdb0e4382bcf0b6fd3d) | clay-good |
| 2026-11-18 | [fix(archive): read a wrapped line starting with `<` as part of its se…](https://github.com/Fission-AI/OpenSpec/commit/a1213fcdc768948034a48d8837c9e0543d124e16) | clay-good |
| 2026-11-18 | [fix(archive): put a blank line after ## Purpose in a new main spec (#…](https://github.com/Fission-AI/OpenSpec/commit/168a5eacc639f9625f6c151613bcb5c46cb2c236) | clay-good |
| 2026-11-18 | [fix(validate): warn when MODIFIED requirement grows past 500 chars (#…](https://github.com/Fission-AI/OpenSpec/commit/499602e82cd2e389586a8b781f27deb8737d8537) | clay-good |
| 2026-11-18 | [fix(version): stop telling Homebrew and Nix installs to update with n…](https://github.com/Fission-AI/OpenSpec/commit/efdf5319b58bcba3ea113528168793d2610ce5a4) | clay-good |

[See all commits ↗](https://github.com/Fission-AI/OpenSpec/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Fission-AI/OpenSpec.git
```
