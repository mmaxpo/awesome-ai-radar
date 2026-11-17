# wkentaro/labelme

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/wkentaro/labelme)

> Image annotation with Python. Supports polygon, rectangle, circle, line, point, and AI-assisted annotation.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Image annotation tool for training data |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 16.3k |
| 🍴 **Forks** | 3.7k |
| 🐞 **Open issues + PRs** | [80](https://github.com/wkentaro/labelme/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `image-annotation` `python` `computer-vision` `annotations` `deep-learning` `semantic-segmentation` `instance-segmentation` `video-annotation` `classification` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2016-05-09 |
| 📦 **Latest release** | [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 70.9 MB |
| 🌐 **Website** | https://labelme.io |

## 📦 Recent releases

### [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0)
<sub>2026-11-14 · 3d ago</sub>

> **Changed**
> - SAM 3 asks to be downloaded again, as 1.8 GB on a GPU or 3.7 GB on the CPU, and asks again for its CPU files when AI falls back to the CPU. Its files from earlier versions stay on disk. ([#3099](https://github.com/wkentaro/labelme/pull/3099))
> - AI no longer retries a request on the CPU when the GPU fails partway through; the next request loads the model again. The status bar no longer shows "Preparing image…". ([#3100](https://github.com/wkentaro/labelme/pull/3100))
> **Fixed**
> - The model menu shows the download size for the AI device: SAM 3 shows about 1.8 GB on a GPU instead of its CPU size. ([#3104](https://github.com/wkentaro/labelme/pull/3104))
> - Deleting an AI model no longer freezes the window while AI runs, and other loaded models stay loaded. ([#3105](https://github.com/wkentaro/labelme/pull/3105))
> …

### [v7.10.0](https://github.com/wkentaro/labelme/releases/tag/v7.10.0)
<sub>2026-11-13 · 4d ago</sub>

> **Added**
> - Allow drawing Polygon and LineStrip paths by dragging, simplifying strokes into fewer vertices while preserving click-to-add input. ([#2757](https://github.com/wkentaro/labelme/pull/2757))
> - Add 3-point circle mode (`circle_3p`) to draw circles by clicking three points on the circumference. ([#2788](https://github.com/wkentaro/labelme/pull/2788))
> - Open JPEG 2000 Images (.jp2, .jpx, .j2k, .j2c) through Pillow with OpenJPEG support, including folder scanning and drag-and-drop, while preserving decoded pixels and transparency in memory. ([#2833](https://github.com/wkentaro/labelme/pull/2833))
> - `labelme.log` records the platform, the installed AI runtime versions, and how long each AI model takes to load, encode an image and generate annotations, to help debug GPU problems. ([#2849](https://github.com/wkentaro/labelme/pull/2849))
> - A Compute device Setting runs AI on the CPU, and the status bar shows while AI is running and whether it runs on the CPU. ([#2861](https://github.com/wkentaro/labelme/pull/2861))
> …

### [v7.9.1](https://github.com/wkentaro/labelme/releases/tag/v7.9.1)
<sub>2026-10-25 · 23d ago</sub>

> **Fixed**
> - Fix a point dragged inside a box being lost on image switch, because the move was never saved or added to undo history. ([#2845](https://github.com/wkentaro/labelme/pull/2845))
> - Hovering where Shapes overlap now highlights the Shape a click selects, so a point drawn inside a box is highlighted and picked over the box. ([#2846](https://github.com/wkentaro/labelme/pull/2846))

### [v7.9.0](https://github.com/wkentaro/labelme/releases/tag/v7.9.0)
<sub>2026-10-20 · 28d ago</sub>

> **Added**
> - Allow double-clicking a shape on the canvas to open the label-edit dialog. ([#2744](https://github.com/wkentaro/labelme/pull/2744))
> - Lock shapes against editing with Lock Shapes / Unlock Shapes (`Ctrl+Shift+L`); the lock is saved per shape as `"locked": true` in the annotation file. ([#2755](https://github.com/wkentaro/labelme/pull/2755))
> - Add Fit to Selection (`Ctrl+Shift+F`) to the View menu and toolbar, a zoom mode that fits the view to the selected shapes, with padding, whenever the selection changes. ([#2758](https://github.com/wkentaro/labelme/pull/2758))
> - Labelme remembers the Annotation Folder for each opened folder across restarts, including one given with `--output`, which Labelme now creates at startup if it is missing. ([#2775](https://github.com/wkentaro/labelme/pull/2775))
> - The Image List has a footer that shows the Annotation Folder and how many images are annotated, for example "3 of 5 annotated · next to images", with Change Annotation Folder… and an option to go back to saving next to images. A remembered folder that is missing shows a warning there. ([#2776](https://github.com/wkentaro/labelme/pull/2776), [#2778](https://github.com/wkentaro/labelme/pull/2778), [#2808](https://github.com/wkentaro/labelme/pull/2808))
> …

### [v7.8.1](https://github.com/wkentaro/labelme/releases/tag/v7.8.1)
<sub>2026-10-07 · 1mo ago</sub>

> **Fixed**
> - Avoid image hashing when loading images while preserving AI embedding reuse when revisiting unchanged images. ([#2741](https://github.com/wkentaro/labelme/pull/2741))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Merge pull request #3112 from wkentaro/test/e2e-teardown-stops-workers](https://github.com/wkentaro/labelme/commit/615a6cac445a74fa3659d4a545916d80482d5ee6) | wkentaro |
| 2026-11-17 | [test: close each window for real when the main_win fixture tears down](https://github.com/wkentaro/labelme/commit/d09d700a8e238fc00ed485065a9e297d494d63a6) | wkentaro |
| 2026-11-17 | [Merge pull request #3110 from wkentaro/build/just-test-quiet-default](https://github.com/wkentaro/labelme/commit/30f21092901ef3e5b915f6cedded049da587c15b) | wkentaro |
| 2026-11-17 | [build: make just test quiet and serial for narrow runs](https://github.com/wkentaro/labelme/commit/01925c0398814948a1bb256bdf2b6122f04edc7b) | wkentaro |
| 2026-11-17 | [Merge pull request #3109 from wkentaro/fix/just-test-path](https://github.com/wkentaro/labelme/commit/f7a0735542a7c8b54b5be1a9b2917416b002eb19) | wkentaro |
| 2026-11-17 | [Merge pull request #3108 from wkentaro/test/private-server-own-thread](https://github.com/wkentaro/labelme/commit/92f1da2e7e5cad19acd3e8f8a603a508305d04c0) | wkentaro |
| 2026-11-17 | [docs: tell agents how to run tests](https://github.com/wkentaro/labelme/commit/6c5b10710e06d8120d313b774c59aeed3b711ef3) | wkentaro |
| 2026-11-17 | [fix: make `just test <path>` run only that path](https://github.com/wkentaro/labelme/commit/bb16efe408d407d240b97493d4e03e1ba5de6848) | wkentaro |
| 2026-11-17 | [test: join only the private-server test's own worker thread](https://github.com/wkentaro/labelme/commit/72f48b304e885c6838e5858114e006fad21273a4) | wkentaro |
| 2026-11-14 | [chore: prep 7.11.0 release](https://github.com/wkentaro/labelme/commit/79699f7dc32af2f8a4418f849a3ed78a4841b42f) | wkentaro |

[See all commits ↗](https://github.com/wkentaro/labelme/commits)

## ⬇️ Get it

```bash
git clone https://github.com/wkentaro/labelme.git
```
