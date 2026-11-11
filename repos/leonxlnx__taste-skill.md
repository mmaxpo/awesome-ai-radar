# leonxlnx/taste-skill

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/leonxlnx/taste-skill)

> Agent skills that give coding agents taste: art direction, reference images and a browser check instead of generic AI pages

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why I saved it** | Skill that gives AI better design taste |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 113.2k |
| 🍴 **Forks** | 7.6k |
| 🐞 **Open issues + PRs** | [5](https://github.com/leonxlnx/taste-skill/issues) |
| 💻 **Languages** | JavaScript 61% · HTML 28% · CSS 11% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `anti-slop` `claude-code` `codex` `cursor` `design-system` `frontend` `landing-page` `ui-design` `web-design` |
| 🕒 **Last activity** | 2026-11-08 (2d ago) |
| 📅 **Created** | 2026-02-19 |
| 📦 **Latest release** | [v2.5.1](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.5.1) — 2026-11-07 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 101.8 MB |
| 🌐 **Website** | https://tasteskill.dev |

## 📦 Recent releases

### [v2.5.1](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.5.1) — tasteskill v2.5.1
<sub>2026-11-07 · 3d ago</sub>

> What a 44-site test of 2.5.0 showed, fixed: builds now iterate until the checker is clean, every page moves, products without photographs are shown in photographs, palettes fit the trade, the copy gets a voice of its own, and nothing lies on anything else on a phone. The install name did not change.
> - **A finish gate:** `scripts/gate.mjs` runs the checker, the layout check and a copy lint, and a build is not done until its last line reads `GATE: PASS` (three rounds, five waivers with reasons at most). In Claude Code it runs as a Stop hook from the skill itself. It never traps an agent: a question to the user costs no round, and `gate.mjs --done` ends a build at the user's word.
> - **Motion on every page:** every hero enters once on load, and every page carries one or two scroll moments. Cafes, shops and services get photo- and type-led ones (new `photo-chapters`, a film look for `picture-develops`); shader effects stay on tech pages.
> - **Photographs over renders:** a product without the client's pictures is shown in licensed stand-in photographs (`photos.mjs search`: Wikimedia Commons, CC0, CC BY, CC BY-SA and public domain only). A 3D render only when the brief asks for one.
> - **Palettes by trade:** `start.mjs deal --trade cafe` deals palettes made for that trade, so two cafes no longer start alike. Eight new place palettes.
> - **A copy layer:** a fact sheet, a voice card, one register and the moves for each part of the page, plus `copy-lint.mjs`, which counts the tells of model-written copy. The gate runs it.
> …

### [v2.5.0](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.5.0) — tasteskill v2.5
<sub>2026-11-04 · 6d ago</sub>

> A complete rebuild of `design-taste-frontend` around professional company websites at the figma.com and x.ai bar. The install name did not change.
> - **One page system:** every build starts from the same starter. The hero fills the first screen, one section per screen, equal left and right edges.
> - **Effects only where they fit:** shader grounds, scroll moments and big scenes only on software, tech and gaming pages. Cafes, shops, hotels and services get real photographs and no effects.
> - **Real product UI:** 19 HTML UI fragments (chat, diff review, terminal, pipeline board, voice and more), and a software page shows its product in one app window.
> - **Real photographs and icons:** vetted Unsplash and Wikimedia Commons frames by trade, no captions, one footer credit line; real brand icons, never drawn.
> - **No two pages alike:** the hero layout, palette, type pairing and ground are dealt at random.
> …

### [v2.1.5](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.1.5) — tasteskill v2.1.5
<sub>2026-10-24 · 17d ago</sub>

> Fixes from the community. Thanks to everyone who reported and sent them.
> - **Safe text in charts and split headings** (#160, #169, thanks @jcastilla89 and @Pablolakotek): `charts.js` and the `Stage.split` fallback escape the text they insert, so a label or heading from user data can no longer inject markup.
> - **No lost screenshots when two widths share a class** (#162, #165, thanks @nosawavey-spec and @ketpatil77).
> - **Keyboard and accessible names** (#170, thanks @MrBinnacle): every control works from the keyboard and has an accessible name.
> - **The italic faces load** (#161, fix from #166, thanks @nosawavey-spec and @ketpatil77): Boska, Erode and Sentient request their italic weight.
> - **`edge-text` no longer fails ellipsised lines** (#156, thanks @shoctroper).
> …

### [v2.1.4](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.1.4) — tasteskill v2.1.4
<sub>2026-10-20 · 21d ago</sub>

> This release makes the inspector's browser profiles safe when several runs go at once ([#157](https://github.com/Leonxlnx/taste-skill/issues/157), [#158](https://github.com/Leonxlnx/taste-skill/pull/158), [#159](https://github.com/Leonxlnx/taste-skill/pull/159)). The rules of `design-taste-frontend` are unchanged; only `scripts/lib/cdp.mjs` changed.
> - **Fix: one inspector run could delete the browser profile of another run that was still going.** Chrome keeps no `lockfile` on macOS and Linux, so the sweep added in 2.1.0 judged a profile unused by its age alone. A second run started during a long one could then pull that run's profile away. Thanks to @t4sh for the report and the fix.
> - **Leftover profiles are cleaned up again, safely.** Every profile now carries `taste-skill-owner.json` with the machine and the process IDs of the run and its Chrome. A later run removes a profile left by a killed run only when that file names this machine and neither process is alive. A profile without the file is never touched.
> Profiles left by earlier versions are not removed automatically. To clear them, delete the `ad-chrome-*` folders in your temp folder (or in `TASTE_SKILL_TMP`).
> Update:
> ```bash
> …

### [v2.1.3](https://github.com/Leonxlnx/taste-skill/releases/tag/v2.1.3) — tasteskill v2.1.3
<sub>2026-10-19 · 22d ago</sub>

> One repo, one skill. `design-taste-frontend` itself is unchanged; this release cleans up the repo around it ([#153](https://github.com/Leonxlnx/taste-skill/issues/153), [#155](https://github.com/Leonxlnx/taste-skill/pull/155)).
> **The other skills moved to repos of their own and kept their install names:**
> - The classic styles and earlier versions (`high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `gpt-taste`, `stitch-design-taste`, `design-taste-frontend-v1`, `design-taste-frontend-v2-experimental`) are in **[Leonxlnx/taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics)**.
> - The image-generation skills (`imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`, `image-to-code`) are in **[Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills)**.
> - `redesign-existing-projects` is part of `design-taste-frontend`.
> Installed a classic skill from this repo before? Install it from its new home under the same name:
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-07 | [Merge pull request #196 from Leonxlnx/v2.5.1](https://github.com/Leonxlnx/taste-skill/commit/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | Leonxlnx |
| 2026-11-07 | [tasteskill 2.5.1: finish gate, motion on every page, copy layer, photos over renders, trade palettes…](https://github.com/Leonxlnx/taste-skill/commit/b900a8075fd7a2449bd6f414a2ae79657e95363c) | Leonxlnx |
| 2026-11-05 | [font-load: warn for each web font that never loads (#186)](https://github.com/Leonxlnx/taste-skill/commit/9b4bf937a1f69348126959c15d2f99a73e65699b) | Leonxlnx |
| 2026-11-05 | [Merge main (#181, #182) into portfolio/alan/e596f504b4a2](https://github.com/Leonxlnx/taste-skill/commit/f578e23218be09ffd5b70debbfdec9fe8286d310) | Leonxlnx |
| 2026-11-05 | [--root for the scripts that serve a page file (#182)](https://github.com/Leonxlnx/taste-skill/commit/151afddbe3be2bd5cadd4884d381dfa13fc920ff) | Leonxlnx |
| 2026-11-05 | [Merge main (#181) into fix/grok-build/inspect-root](https://github.com/Leonxlnx/taste-skill/commit/7a373bf2ed1cb6799fe87816005e499435253dec) | Leonxlnx |
| 2026-11-05 | [Each checked page gets its own report folder (#181)](https://github.com/Leonxlnx/taste-skill/commit/8fcde309b31c9d857c51a504548d95de12eb0e89) | Leonxlnx |
| 2026-11-05 | [Port to 2.5: font-load warns for each web font that never loads](https://github.com/Leonxlnx/taste-skill/commit/386d187d8637d35a9f282ff4da2edfc857ea6b32) | Leonxlnx |
| 2026-11-05 | [Port to 2.5: --root for the scripts that serve a page file](https://github.com/Leonxlnx/taste-skill/commit/4c492ecf6d59a19fd31b4516f98e502129da50d5) | Leonxlnx |
| 2026-11-05 | [Port to 2.5: each checked page gets its own report folder](https://github.com/Leonxlnx/taste-skill/commit/3324132353b0ef22388f60262a42bc06677111f9) | Leonxlnx |

[See all commits ↗](https://github.com/leonxlnx/taste-skill/commits)

## 👥 Top contributors

[Leonxlnx](https://github.com/Leonxlnx) (277) · [cursoragent](https://github.com/cursoragent) (9) · [HugoSpy](https://github.com/HugoSpy) (5) · [bougieL](https://github.com/bougieL) (3) · [flexi767](https://github.com/flexi767) (2)

## ⬇️ Get it

```bash
git clone https://github.com/leonxlnx/taste-skill.git
```
