# pbakaus/impeccable

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pbakaus/impeccable)

> The design vocabulary for your coding agent. Steer with polish and bolder, review with critique and audit, catch AI slop before it ships.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Front-end design quality skill: shape, critique, polish, animate |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 113.3k |
| 🍴 **Forks** | 6.7k |
| 🐞 **Open issues + PRs** | [61](https://github.com/pbakaus/impeccable/issues) |
| 💻 **Languages** | Rust 75% · JavaScript 23% · TypeScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai` `anti-slop` `design` `slop` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2025-11-16 |
| 📦 **Latest release** | [skill-v4.10.0](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.10.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 908.3 MB |
| 🌐 **Website** | https://impeccable.style |

## 📦 Recent releases

### [skill-v4.10.0](https://github.com/pbakaus/impeccable/releases/tag/skill-v4.10.0) — Skill 4.10.0
<sub>2026-11-18 · today</sub>

> - **DESIGN.md as a map.** A long DESIGN.md reaches your agent as a short map of where tokens, components and layouts live, and the agent looks up one token, component or section when it needs it. `design-compact` proposes the map and writes it only when you agree.
> - **Drift you can act on.** When the code contradicts DESIGN.md, Impeccable names what it contradicts.
> - **Motion you can check.** `animate` captures the motion it built and reviews it from that evidence.
> - **Finished world runs.** A world run ends with the site, walks its direction over the captures before the final review, and records DESIGN.md from what shipped.
> - **Steadier Live.** The Live bar stays still under the pointer, and the missing PRODUCT.md notice shows once.

### [cli-v4.10.0](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.10.0) — CLI 4.10.0
<sub>2026-11-18 · today</sub>

> - **Your switches, in every agent.** The switches you turn on in Impeccable reach your agents' rule files within seconds. `switches-refresh --now` syncs them on the spot.
> - **Page shots.** `shot` saves a page at desktop and phone widths.
> - **Side tabs on rounded boxes.** The detector catches a bar down one side of a rounded box, whether it is a border, an inset shadow or a pseudo-element. A bar on a square box is fine and no longer flagged.
> - **Every clone finds its repository.** Remotes through an SSH host alias, or spelled in another case, match the repository on GitHub.
> - **Codex: trust Impeccable's hooks.** Codex runs a new or changed hook only after you trust it. When Codex says "Hooks need review", choose Trust all and continue, or trust Impeccable's hooks in `/hooks`. A later release will trust them for you when you connect.

### [engine-v0.1.27](https://github.com/pbakaus/impeccable/releases/tag/engine-v0.1.27) — impeccable engine engine-v0.1.27
<sub>2026-11-18 · today</sub>

> Prebuilt impeccable engine binaries (engine-v0.1.27). The launcher, the npm shim and impeccable install download these on first run. Docs: https://impeccable.style

### [loop-v0.2.0](https://github.com/pbakaus/impeccable/releases/tag/loop-v0.2.0) — Impeccable Loop 0.2.0
<sub>2026-11-18 · today</sub>

> Answers in Loop now wake Codex, Cursor, GitHub Copilot CLI and opencode, as they already did Claude Code. An answer that lands while an agent is mid-turn, or after its session ended, still reaches it.

### [cli-v4.9.2](https://github.com/pbakaus/impeccable/releases/tag/cli-v4.9.2) — CLI 4.9.2
<sub>2026-11-16 · 3d ago</sub>

> - **Loop 0.1.3.** `loop install` and `loop update` verify it against its pinned checksum.
> - **Your taste in every agent.** `loop connect` offers to add your Impeccable taste to your agents' rule files. Answer ahead of time with `--taste` or `--no-taste`.
> - **Signing in does more.** `login` offers Loop when your plan includes it, and the first sign-in inside a repository adds that repository to your account.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Carry engine 0.1.27 checksums into every harness's skill copy](https://github.com/pbakaus/impeccable/commit/b49177d32788f2dc585c42831d845dacf1ebed2c) | pbakaus |
| 2026-11-18 | [Record engine 0.1.27 checksums and pin its platform packages](https://github.com/pbakaus/impeccable/commit/ab3617920fcdb5009163a725ba8ff59927a63474) | pbakaus |
| 2026-11-18 | [Engine 0.1.27 with side-tab on rounded boxes only](https://github.com/pbakaus/impeccable/commit/645925acd71b18558488c5b8d8f263404cb68db8) | pbakaus |
| 2026-11-18 | [Merge remote-tracking branch 'origin/next' into release/cli-4.10.0](https://github.com/pbakaus/impeccable/commit/109f9cf85d2497a1a906b7685a7c3a4afca7d3dc) | pbakaus |
| 2026-11-18 | [Merge pull request #1574 from pbakaus/detect/side-tab-inline-radius](https://github.com/pbakaus/impeccable/commit/8cd45c5fe5c884c95b02c1eb265f046bebfbfe08) | pbakaus |
| 2026-11-18 | [Merge pull request #1572 from pbakaus/foundations/scan-library](https://github.com/pbakaus/impeccable/commit/6cca7f25272822e5d5fd636f5769bad39d7aa289) | pbakaus |
| 2026-11-18 | [Read a spaced ! important on an inline radius](https://github.com/pbakaus/impeccable/commit/84e0096d22e66d9f097b8ba22d97e8cba4fc8b73) | pbakaus |
| 2026-11-18 | [Foundations: let a listing scan skip the secrets scan](https://github.com/pbakaus/impeccable/commit/e399cc317741403ac26207ae60dd36fb68cde887) | pbakaus |
| 2026-11-18 | [Merge pull request #1575 from pbakaus/ext/panel-only](https://github.com/pbakaus/impeccable/commit/a48d2f540baeb25c84c3cb0a6f0068233449c016) | pbakaus |
| 2026-11-18 | [Apply an inline important radius after the normal ones](https://github.com/pbakaus/impeccable/commit/db380f73cedbe66753e36ad2c6679b44d9753c2c) | pbakaus |

[See all commits ↗](https://github.com/pbakaus/impeccable/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pbakaus/impeccable.git
```
