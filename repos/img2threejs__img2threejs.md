# img2threejs/img2threejs

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/img2threejs/img2threejs)

> Rebuild the object in a reference image as a code-only, procedural, quality-gated, animation-ready Three.js model. Token-efficient image-to-3D.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why it's worth a look** | Turn images into Three.js scenes |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 21.3k |
| 🍴 **Forks** | 1.8k |
| 🐞 **Open issues + PRs** | [120](https://github.com/img2threejs/img2threejs/issues) |
| 💻 **Languages** | Python 97% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `3d` `ai-agents` `claude-code` `computer-graphics` `generative` `image-to-3d` `procedural-generation` `threejs` `typescript` `webgl` |
| 🕒 **Last activity** | 2026-11-05 (8d ago) |
| 📅 **Created** | 2026-07-15 |
| 📦 **Latest release** | [v2.0.1](https://github.com/img2threejs/img2threejs/releases/tag/v2.0.1) — 2026-11-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 35.5 MB |
| 🌐 **Website** | https://img2threejs.io |

## 📦 Recent releases

### [v2.0.1](https://github.com/img2threejs/img2threejs/releases/tag/v2.0.1)
<sub>2026-11-05 · 8d ago</sub>

> **What's Changed**
> **Other Changes**
> * docs(skill): document the img2 harness in SKILL.md by @kokorolx in https://github.com/img2threejs/img2threejs/pull/132
> * feat: img2threejs CLI package (npx img2threejs install) by @kokorolx in https://github.com/img2threejs/img2threejs/pull/146
> * ci: add docs-quality gates and stricter PR template by @kokorolx in https://github.com/img2threejs/img2threejs/pull/173
> * docs: add PLUGINS.md — installing and using plugins from the pipeline side by @kokorolx in https://github.com/img2threejs/img2threejs/pull/166
> …

### [v2.0.0](https://github.com/img2threejs/img2threejs/releases/tag/v2.0.0) — 2.0.0: The Plugin Update
<sub>2026-09-06 · 2mo ago</sub>

> **The Plugin Update.** The plugin ecosystem — domain registry, img2 harness, plugin-served domains — ships as its own major, pulled forward from the original Procedural World bundle.
> **Breaking**
> - **`animated-character` is served by the installed [plugin-character](https://github.com/img2threejs/plugin-character)** (`img2 add img2threejs/plugin-character`, harness >= 0.2.3). The in-repo domain module is removed; without the plugin the profile fails loud naming what is available, and an in-flight workspace is refused while the provider is absent, resuming unchanged on reinstall.
> - **CS2 is extracted into [plugin-cs2](https://github.com/img2threejs/plugin-cs2)** and **a domain is no longer inferred from the target's name** — `detect_cs2_intent` and its 17-keyword table are removed; declare the domain (`--profile cs2`) instead.
> - Local spec search defaults to `core_3d` rather than `cs2`; `objectClass.cs2` is replaced by `objectClass.domain: "<id>"`; `weapon-v1.4` no longer requires a CS2 marker to pass strict validation.
> **Added**
> …

### [v1.5.2](https://github.com/img2threejs/img2threejs/releases/tag/v1.5.2) — 1.5.2: Support VFX / Animation for character
<sub>2026-09-03 · 2mo ago</sub>

> **Changelog**
> **[1.5.2] — 2026-09-03**
> **Theme: a clip that exists is not a clip that plays, and rigging may only add.** Rigging failures
> in 1.5.1 were total and silent: clips held actions, the mixer held state, buttons dispatched, and
> nothing moved. This release turns the measured repair pipeline into executable modules, wires it
> into the workflow, and freezes the source geometry so binding cannot silently damage the model.
> …

### [v1.5.1](https://github.com/img2threejs/img2threejs/releases/tag/v1.5.1) — 1.5.1: add the GLB-reference route
<sub>2026-08-23 · 2mo ago</sub>

> **[1.5.1] — 2026-08-23**
> **Theme: the GLB-reference route.** A GLB stops being an informal aid and becomes a measurement
> instrument with a packaged pipeline, three bounded prompts, and an explicit statement of which
> parameters it can be held to 1:1 and which it cannot.
> **Added**
> - Add `integrations/glb_character_pipeline`, an opt-in three-stage reconstruction — cross-section
> …

### [v1.5-beta](https://github.com/img2threejs/img2threejs/releases/tag/v1.5-beta) — v1.5 beta — character track, material pipeline, and a release path that actually…
<sub>2026-08-06 · 3mo ago</sub>

> **Why this is a beta of scripts only**
> The per-subject tuning artifacts (sculpt specs, assessments, feedback plans, comparison renders for
> individual characters and objects) are excluded and now git-ignored. They are outputs of a tuning
> session, never inputs to a build, and they carried multi-megabyte PNGs. Same reasoning `.gitignore`
> already applied to `.screenshot/`.
> **Added**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-05 | [Merge pull request #187 from img2threejs/release/skill-2.0.1](https://github.com/img2threejs/img2threejs/commit/0c0c49bc168e648dbaf9c8c080474de0b3a941b6) | kokorolx |
| 2026-11-05 | [docs(readme): version badge 2.0.1](https://github.com/img2threejs/img2threejs/commit/668aef21872229dd93e3dd6b080b9963bd2315c5) | kokorolx |
| 2026-11-05 | [release: skill 2.0.1 ships the post-2.0.0 SKILL.md routing guidance](https://github.com/img2threejs/img2threejs/commit/eb97dac5d8786445639d70fddd7361d3a1e5b4a6) | kokorolx |
| 2026-11-05 | [Merge pull request #189 from img2threejs/docs/update-existing-installs](https://github.com/img2threejs/img2threejs/commit/9e09f4b9d9a03051d6accbe5b8e8578a174fa80c) | kokorolx |
| 2026-11-05 | [Merge pull request #186 from img2threejs/feat/cli-update-latest-release](https://github.com/img2threejs/img2threejs/commit/adae75f64ff6540ac7e2e2d3a94ea2b7e45cfa07) | kokorolx |
| 2026-11-04 | [docs(install): tighten the agent update procedure after a scenario dr…](https://github.com/img2threejs/img2threejs/commit/299cbdd6919470c32fba437529c6293ee4c2a3d6) | kokorolx |
| 2026-11-04 | [docs(install): write the update section as an agent procedure](https://github.com/img2threejs/img2threejs/commit/4de3e7fa266d15463a4f2c46aa4463b40da2a0d0) | kokorolx |
| 2026-11-04 | [docs(install): update guide for existing installs](https://github.com/img2threejs/img2threejs/commit/fc7153ecab33fb5edc8ca36c4114c7ea2a15766b) | kokorolx |
| 2026-11-04 | [feat(cli): install and update follow the latest GitHub release](https://github.com/img2threejs/img2threejs/commit/a83fab99d04c08fe57c3f27914831ce21a7f9859) | kokorolx |
| 2026-10-27 | [Merge pull request #177 from img2threejs/docs/minimax-sponsor](https://github.com/img2threejs/img2threejs/commit/3e7099e1b7fe93e187e06db4bdbe1e1906c21a28) | kokorolx |

[See all commits ↗](https://github.com/img2threejs/img2threejs/commits)

## ⬇️ Get it

```bash
git clone https://github.com/img2threejs/img2threejs.git
```
