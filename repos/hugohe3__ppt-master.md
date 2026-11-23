# hugohe3/ppt-master

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/hugohe3/ppt-master)

> AI turns documents or topics into real, native PowerPoint decks—with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own .pptx templates. · by Hugo He

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Documents or topics to native PowerPoint decks |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 79.5k |
| 🍴 **Forks** | 6.2k |
| 🐞 **Open issues + PRs** | [2](https://github.com/hugohe3/ppt-master/issues) |
| 💻 **Languages** | Python 94% · JavaScript 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `powerpoint` `pptx` `presentation` `office` `slides` `powerpoint-generation` `ppt` `slide` `aippt` |
| 🕒 **Last activity** | 2026-11-20 (3d ago) |
| 📅 **Created** | 2025-12-10 |
| 📦 **Latest release** | [v6.10.0](https://github.com/hugohe3/ppt-master/releases/tag/v6.10.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 138.3 MB |
| 🌐 **Website** | https://hugohe3.github.io/ppt-master-examples/ |

## 📦 Recent releases

### [v6.10.0](https://github.com/hugohe3/ppt-master/releases/tag/v6.10.0)
<sub>2026-11-19 · 4d ago</sub>

> Personal templates created through Create Template now live in a Git-ignored local library so repository updates never trip over personal registrations, the OpenAI image backend defaults to `gpt-image-2.6-sunburst`, Volcengine adds Seedream 5.0 with Ark as the default gateway, and a set of conversion, icon, notes, and Edit Native round-trip fixes resolves silent content loss and export aborts.
> **Templates and repository updates**
> - Personal library workspaces and indexes now default to Git-ignored `skills/ppt-master/templates/local/<kind_dir>/` while official built-in templates stay read-only unless `--builtin` is passed to `register_template.py`. Confirm UI, chat discovery, `apply_template.py`, and `mirror_template_materialize.py` merge built-in and local layers in memory without mutating tracked files (`fd2f058d`, `7e0df670`).
> - `update_repo.py` automatically migrates additive unstaged personal entries out of tracked `*_index.json` files into `templates/local/` before `git pull --ff-only`, so existing clones with registered custom templates update cleanly (`fd2f058d`).
> **AI image generation**
> - The OpenAI backend defaults to `gpt-image-2.6-sunburst` across `image_gen.py`, `.env.example`, and documentation (`5495a5cb`).
> …

### [v6.9.0](https://github.com/hugohe3/ppt-master/releases/tag/v6.9.0)
<sub>2026-11-08 · 15d ago</sub>

> Image to PPTX gains OCR text evidence, text-removed bases, and checked image layers, and now runs on any vision host with an `image_gen.py` reference-image backend. Narration adds an OpenAI Realtime provider, `image_gen.py` can produce animated GIFs on OpenAI `gpt-image-2.6`, and a round of conversion and round-trip fixes stops sources from being overwritten or silently altered.
> **Image to PPTX**
> - New `scripts/image_ocr.py`: `scan` OCRs normalized page images into reviewable text blocks (line boxes, estimated font size, sampled ink color), and the text layer becomes native text over a text-removed base. Removal results are composited back onto source pixels, and merged bases are checked for text left inside removal boxes (37efd014, e55a56ff, 574265a0, d1619e4f).
> - New `scripts/image_layers.py`: `check` verifies an extracted layer is registered against the page, `diff-matte` derives a layer from the page's own pixels, `mono-matte` cuts a single-color graphic (such as a white logo) cleanly from a key plate, and merges are layer-aware and honour occlusion (bbc84447, 3c5cd655, 4a68cdda, 79d7cf57).
> - The profile is no longer tied to one host: any vision host with a reference-image path works, either host-native editing or `image_gen.py --reference-image` (OpenAI, Gemini). Every page follows one assembly path; text removal defaults to `-b openai` and registered layers to `-b gemini`, with at most two residue retries before a page is marked for manual work (9577d604, 09547b1a, 7387d7b9, 6b0a2a5a, 8e809511).
> **AI image generation**
> …

### [v6.8.0](https://github.com/hugohe3/ppt-master/releases/tag/v6.8.0)
<sub>2026-10-30 · 24d ago</sub>

> The OpenAI image backend now defaults to `gpt-image-2.5-sunburst`, and image generation accepts any W:H aspect ratio. This release also brings a round of Edit Native, template-import, and source-conversion fixes that stop content from being silently dropped, plus PowerPoint-exact animation timing.
> **AI image generation**
> - The OpenAI backend now defaults to `gpt-image-2.5-sunburst`. Measured on the official endpoint at 1024×1024 medium, it used about a quarter of the output tokens of `gpt-image-2` (~$0.013 vs ~$0.053) and returned in about half the time. It also returns real RGBA for `OPENAI_BACKGROUND=transparent`. `OPENAI_MODEL` still overrides it (fc7aa7c5, 27be992f, af5029c7).
> - `aspect_ratio` accepts any positive W:H, decimals included (e.g. `1.85:1`). Unsupported ratios no longer fail a request: each backend picks the nearest size its model allows, reports the adaptation, and placement crops to the requested shape (b1b7f1b2, be8a19da, e61c34ed).
> - Rate limits are handled properly. `Retry-After` is honored by every backend and by manifest requeues. Waits are capped so that a huge header value can no longer crash the run or block it for a day, and a run that stops with items still pending exits non-zero (c02689f4, 230afab1, 4c3961a8, 625e05a9).
> - `--filename` values containing dots (`gpt-image-2.5-sunburst_hero`) are no longer truncated at the last dot, which made each such run silently overwrite the previous file (c02689f4).
> …

### [v6.7.3](https://github.com/hugohe3/ppt-master/releases/tag/v6.7.3)
<sub>2026-10-22 · 1mo ago</sub>

> Patch release: Edit Native and native-object fixes that stop a round trip from failing or silently replacing content, plus a readable fallback for native formulas outside PowerPoint.
> **Edit Native PPTX**
> - An explicit Morph pair whose endpoint sits on an otherwise unchanged page no longer crashes with `KeyError`. The page keeps its source bytes, and only the shape name the pair needs is patched (604ecdec).
> - Moving an imported object that kept its source text body (for example Office Math that could not be rebuilt as a formula) restores that text body at the new position. Before, any move rebuilt the formulas as plain text. Edits that do change the text still rebuild it, and now warn when native math would become plain text (2e1658cc).
> - Imported charts and block formulas rebuilt during a round trip keep their source shape id. Before, export stopped with "Edited slide removed source animation target(s)" (0db9d903, cd445683).
> **Native charts and formulas**
> …

### [v6.7.2](https://github.com/hugohe3/ppt-master/releases/tag/v6.7.2)
<sub>2026-10-17 · 1mo ago</sub>

> Patch release: fixes from an audit of the issue history. Most of them stop a tool from losing, overwriting or rewriting content while it reports success.
> **Installation and startup**
> - **Skill-only installations create projects in your working folder again** (703aa72f, #144). Since v6.3.0, `project_manager.py init` placed projects relative to the installed skill. For an `npx skills` or plugin installation, that meant `.agents/projects/` or the plugin cache, where an update can replace them. Inside a repository checkout nothing changes.
> - On Windows, a `python3` that never starts (the WindowsApps stub exits 9009 with no output) is no longer treated as an integrity-guard failure; the agent retries with `python` first (e1b58732, follow-up on #142).
> **Source conversion and import**
> - **PDF**: removed four table rewrites that were written against one sample paper. They re-derived variable categories from hard-coded symbols, replaced headers, dropped rows and invented a correlation column. Extracted cells are now kept as extracted (3aa2ec62).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(servers): narrow Windows breakaway fallback and document foregrou…](https://github.com/hugohe3/ppt-master/commit/63a03673d5c3c928e7f52983a2c8ec65bac30002) | hugohe3 |
| 2026-11-19 | [chore(release): bump version to 6.10.0](https://github.com/hugohe3/ppt-master/commit/d8f704bc8c1552d53a8769b55d1eecd22c782042) | hugohe3 |
| 2026-11-19 | [Merge pull request #355 from DoctrineAlanK/fix/roundtrip-a14-math-nam…](https://github.com/hugohe3/ppt-master/commit/df936341d5376504261de314ca7eaf9dadb0f990) | hugohe3 |
| 2026-11-19 | [Merge pull request #354 from kevindesuyo/fix/outline-icon-filled-details](https://github.com/hugohe3/ppt-master/commit/3efb59b7ec07954998f978a822b5253aacdbec63) | hugohe3 |
| 2026-11-19 | [Merge pull request #353 from kevindesuyo/fix/html-latin1-label-as-cp1252](https://github.com/hugohe3/ppt-master/commit/17cae0e8947fb5efd0ba37655ede54c17a4f77fc) | hugohe3 |
| 2026-11-19 | [Merge pull request #352 from kevindesuyo/fix/notes-split-atx-heading](https://github.com/hugohe3/ppt-master/commit/d643e597fe89944199422c5c2192b63193d7dd73) | hugohe3 |
| 2026-11-19 | [fix(edit-native): keep a14 math namespaces when roundtrip merging slides](https://github.com/hugohe3/ppt-master/commit/0500701516303f1b1d3c2fd0567616e7d2ae50fd) | DoctrineAlanK |
| 2026-11-19 | [fix(icons): keep the filled details of outline icons filled](https://github.com/hugohe3/ppt-master/commit/ea6b25da14986edbfebefc99013c362849952ad2) | kevindesuyo |
| 2026-11-19 | [fix(convert): read an iso-8859-1 HTML label as windows-1252](https://github.com/hugohe3/ppt-master/commit/98d47ea280ba4e28785a8471f72e36304a6b907b) | kevindesuyo |
| 2026-11-19 | [fix(notes-split): only real Markdown headings start a new page](https://github.com/hugohe3/ppt-master/commit/1244d8142b95676e51e676bb1fdcb041216cb104) | kevindesuyo |

[See all commits ↗](https://github.com/hugohe3/ppt-master/commits)

## ⬇️ Get it

```bash
git clone https://github.com/hugohe3/ppt-master.git
```
