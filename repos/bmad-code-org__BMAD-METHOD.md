# bmad-code-org/BMAD-METHOD

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/bmad-code-org/BMAD-METHOD)

> Breakthrough Method for Agile Ai Driven Development

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Agile method + agent roles for AI-driven development |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 55.7k |
| 🍴 **Forks** | 6.2k |
| 🐞 **Open issues + PRs** | [114](https://github.com/bmad-code-org/BMAD-METHOD/issues) |
| 💻 **Languages** | Python 80% · HTML 12% · JavaScript 6% · CSS 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agile` `ai` `context-engineering` `spec-driven-development` `sdlc` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-04-13 |
| 📦 **Latest release** | [v6.12.4](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.4) — 2026-10-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 55.6 MB |

## 📦 Recent releases

### [v6.12.4](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.4)
<sub>2026-10-14 · 1mo ago</sub>

> **🐛 Fixes**
> * A module pinned in the registry (TEA, at v1.27.2) no longer shows the channel picker, since stable or next would pick a version this installer cannot install. The installer prints the pin and the v7 install command instead. `--pin CODE=TAG` still overrides it.

### [v6.12.3](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.3)
<sub>2026-10-14 · 1mo ago</sub>

> **🐛 Fixes**
> * Choosing a channel for a module with a registry pin now takes effect. The TEA pin (v1.27.2) used to win over the picker with no message.
> * The channel picker offers stable and pin. `next` is gone from the install picker and the channel review, and `--next=CODE` stays for headless use.

### [v6.12.2](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.2)
<sub>2026-10-11 · 1mo ago</sub>

> **🐛 Fixes**
> * `install --yes` without `--directory` installs into the current directory instead of stopping at a prompt (#3064).
> * Helper scripts write UTF-8 on Windows (#3050).
> * CIS and TEA install at their last v6 releases (v0.3.2 and v1.27.2); newer releases target v7.
> * The installer notes that v7 is available for preview.

### [v6.12.1](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.1)
<sub>2026-10-04 · 1mo ago</sub>

> **Every skill now reads the same merged config**, so overrides in `_bmad/custom/config.toml` and `config.user.toml` apply everywhere (#3019).
> **🐛 Fixes**
> * 23 bmm skills, including the v6 shims, load config through `resolve_config.py` instead of reading `_bmad/bmm/config.yaml` directly (#3019).
> * `config.toml` now carries the defaults for user-scope keys, so `bmad-build` and `bmad-build-auto` render on a fresh clone without `config.user.toml`. Re-run the installer to pick this up (#3016).
> * `bmad-create-epics-and-stories` writes `status: draft` and keeps it when final validation fails, listing the open checks. `status: final` is set only when every check passes (#3020).
> * Party mode's create-party collision check now sees aliases and custom-only member codes, via `resolve_party.py --list-codes` (#3015).

### [v6.12.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.0)
<sub>2026-09-04 · 2mo ago</sub>

> **Build decides how much ceremony a change needs after investigating it, not before.** Simple changes now get a two-section spec and finish in one session.
> **Review triage logs a verdict and evidence for every finding**, so nothing gets dropped silently. Several review bugs went with it: layers that returned nothing, serial launches, and re-reviews redoing settled work.
> **💥 Breaking**
> * `persistent_facts` ships empty. Re-add `project-context.md` to your override if you relied on the auto-load.
> * `{diff_output}` is now `{diff_file}`. Update custom review overrides.
> * Deprecated shims are opt-in on fresh installs. Pass `--shims` to keep them.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [style(memlog): drop the extra blank line ruff format rejects in test_…](https://github.com/bmad-code-org/BMAD-METHOD/commit/e435a22574fe55722841086e5566420178b98df3) | alexeyv |
| 2026-11-12 | [fix(skills): route skill and agent authoring to Toolsmith, test that …](https://github.com/bmad-code-org/BMAD-METHOD/commit/06c1f851c1c93eb8c24f8ce83ca2776d7f65498e) | alexeyv |
| 2026-11-12 | [fix(po): offer bmad-retrospective before closing an epic (#3184)](https://github.com/bmad-code-org/BMAD-METHOD/commit/7d95282fa32ec18c4fe2e3ba7b5f2828adcd4d1c) | alexeyv |
| 2026-11-12 | [fix(memlog): read and write frontmatter with PyYAML instead of a hand…](https://github.com/bmad-code-org/BMAD-METHOD/commit/c67a00d1a384d8d77cbce8db589ecb0f733493da) | alexeyv |
| 2026-11-12 | [fix(po): stop the Outcome from carrying an empty signal sentence (#3183)](https://github.com/bmad-code-org/BMAD-METHOD/commit/ff6bb860e12735b19eded159cf950e6f0262f13f) | alexeyv |
| 2026-11-11 | [refactor!: group skills into one folder per module (#3181)](https://github.com/bmad-code-org/BMAD-METHOD/commit/3cf35b6dc97fb8d7e319287a680a9197a8e1036a) | bmadcode |
| 2026-11-11 | [feat(founder): Nadia the Founder Advisor, a single-skill module (#3180)](https://github.com/bmad-code-org/BMAD-METHOD/commit/e9cbe2b2962eb7ee544b1512b0e3fada7ed0144e) | bmadcode |
| 2026-11-08 | [feat(facilitate)!: Mary and John on bmad-facilitate, paced templates,…](https://github.com/bmad-code-org/BMAD-METHOD/commit/a867e1604b365d48ea03cbd109da1066ba0c84bc) | bmadcode |
| 2026-11-08 | [feat(shard-pro): editable shards, safer rebuilds, and split-by-defaul…](https://github.com/bmad-code-org/BMAD-METHOD/commit/96ebd0320e0986b6317a1e305b426efd73fae6cc) | bmadcode |
| 2026-11-06 | [refactor(build): write plan enum values bare, quoting only what YAML …](https://github.com/bmad-code-org/BMAD-METHOD/commit/d74453f5e6295fffec8161c9df96f256fe51aa5a) | alexeyv |

[See all commits ↗](https://github.com/bmad-code-org/BMAD-METHOD/commits)

## ⬇️ Get it

```bash
git clone https://github.com/bmad-code-org/BMAD-METHOD.git
```
