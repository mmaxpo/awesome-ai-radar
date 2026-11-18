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
| 🐞 **Open issues + PRs** | [76](https://github.com/wkentaro/labelme/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `image-annotation` `python` `computer-vision` `annotations` `deep-learning` `semantic-segmentation` `instance-segmentation` `video-annotation` `classification` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2016-05-09 |
| 📦 **Latest release** | [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 71.2 MB |
| 🌐 **Website** | https://labelme.io |

## 📦 Recent releases

### [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0)
<sub>2026-11-14 · 4d ago</sub>

> **Changed**
> - SAM 3 asks to be downloaded again, as 1.8 GB on a GPU or 3.7 GB on the CPU, and asks again for its CPU files when AI falls back to the CPU. Its files from earlier versions stay on disk. ([#3099](https://github.com/wkentaro/labelme/pull/3099))
> - AI no longer retries a request on the CPU when the GPU fails partway through; the next request loads the model again. The status bar no longer shows "Preparing image…". ([#3100](https://github.com/wkentaro/labelme/pull/3100))
> **Fixed**
> - The model menu shows the download size for the AI device: SAM 3 shows about 1.8 GB on a GPU instead of its CPU size. ([#3104](https://github.com/wkentaro/labelme/pull/3104))
> - Deleting an AI model no longer freezes the window while AI runs, and other loaded models stay loaded. ([#3105](https://github.com/wkentaro/labelme/pull/3105))
> …

### [v7.10.0](https://github.com/wkentaro/labelme/releases/tag/v7.10.0)
<sub>2026-11-13 · 5d ago</sub>

> **Added**
> - Allow drawing Polygon and LineStrip paths by dragging, simplifying strokes into fewer vertices while preserving click-to-add input. ([#2757](https://github.com/wkentaro/labelme/pull/2757))
> - Add 3-point circle mode (`circle_3p`) to draw circles by clicking three points on the circumference. ([#2788](https://github.com/wkentaro/labelme/pull/2788))
> - Open JPEG 2000 Images (.jp2, .jpx, .j2k, .j2c) through Pillow with OpenJPEG support, including folder scanning and drag-and-drop, while preserving decoded pixels and transparency in memory. ([#2833](https://github.com/wkentaro/labelme/pull/2833))
> - `labelme.log` records the platform, the installed AI runtime versions, and how long each AI model takes to load, encode an image and generate annotations, to help debug GPU problems. ([#2849](https://github.com/wkentaro/labelme/pull/2849))
> - A Compute device Setting runs AI on the CPU, and the status bar shows while AI is running and whether it runs on the CPU. ([#2861](https://github.com/wkentaro/labelme/pull/2861))
> …

### [v7.9.1](https://github.com/wkentaro/labelme/releases/tag/v7.9.1)
<sub>2026-10-25 · 24d ago</sub>

> **Fixed**
> - Fix a point dragged inside a box being lost on image switch, because the move was never saved or added to undo history. ([#2845](https://github.com/wkentaro/labelme/pull/2845))
> - Hovering where Shapes overlap now highlights the Shape a click selects, so a point drawn inside a box is highlighted and picked over the box. ([#2846](https://github.com/wkentaro/labelme/pull/2846))

### [v7.9.0](https://github.com/wkentaro/labelme/releases/tag/v7.9.0)
<sub>2026-10-20 · 29d ago</sub>

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
| 2026-11-17 | [Merge pull request #3124 from wkentaro/build/test-worksteal](https://github.com/wkentaro/labelme/commit/5cc8e9d801640f1c99a78122ca1336e0eeb700b8) | wkentaro |
| 2026-11-17 | [Merge pull request #3123 from wkentaro/test/fast-download-server-shut…](https://github.com/wkentaro/labelme/commit/76c66dc37628ddc5806bf6a2eb1f6522c521b4a7) | wkentaro |
| 2026-11-17 | [build: use xdist work stealing for parallel test runs](https://github.com/wkentaro/labelme/commit/523cf9d16767454d8177326f8b98e86a841cc2b3) | wkentaro |
| 2026-11-17 | [test: poll the download test servers every 10 ms](https://github.com/wkentaro/labelme/commit/85d41882bbfd157752478bb8b39a265a0a042a03) | wkentaro |
| 2026-11-17 | [Merge pull request #3114 from wkentaro/test/auto-save-read-after-idle](https://github.com/wkentaro/labelme/commit/d5e0d11f87290e28f5a7b073a8eaf4e33e7ea12b) | wkentaro |
| 2026-11-17 | [Merge pull request #3120 from wkentaro/test/label-file-roundtrip-prop…](https://github.com/wkentaro/labelme/commit/61b4ace061c0d27fdfb24d7138f9bf78a86d2f2b) | wkentaro |
| 2026-11-17 | [Merge pull request #3118 from wkentaro/test/drop-fixed-sleeps](https://github.com/wkentaro/labelme/commit/72ef97c1e4a02dd550b3dd26262462bff33d6da9) | wkentaro |
| 2026-11-17 | [test: add a round-trip property test for label files](https://github.com/wkentaro/labelme/commit/3ae36b32214371c6234d3dd51c3d0598bdc3032b) | wkentaro |
| 2026-11-17 | [test: drop fixed sleeps from GUI tests](https://github.com/wkentaro/labelme/commit/8b87de2668236166fcf7189e6fc20d0595150867) | wkentaro |
| 2026-11-17 | [test: move the cursor off screen before each test](https://github.com/wkentaro/labelme/commit/34d4cb1ac7980d773e2cf9c9b6a3e421d0b76763) | wkentaro |

[See all commits ↗](https://github.com/wkentaro/labelme/commits)

## ⬇️ Get it

```bash
git clone https://github.com/wkentaro/labelme.git
```
