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
| 🐞 **Open issues + PRs** | [85](https://github.com/wkentaro/labelme/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `image-annotation` `python` `computer-vision` `annotations` `deep-learning` `semantic-segmentation` `instance-segmentation` `video-annotation` `classification` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2016-05-09 |
| 📦 **Latest release** | [v7.11.1](https://github.com/wkentaro/labelme/releases/tag/v7.11.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 70.0 MB |
| 🌐 **Website** | https://labelme.io |

## 📦 Recent releases

### [v7.11.1](https://github.com/wkentaro/labelme/releases/tag/v7.11.1)
<sub>2026-11-25 · yesterday</sub>

> **Fixed**
> - AI-Segment and AI-Find All work again on images over 179 MP, which failed with "Image size exceeds limit" since 7.11.0. Labelme sends the AI server the image at the model's input size instead of in full, so SAM2 segments a 600 MP image in about a second. Labelme requires osam 0.12.1 or later. ([#3126](https://github.com/wkentaro/labelme/pull/3126))
> - Auto-save in a folder of thousands of Images no longer rescans every Image after each save, which paused the window for up to 0.3 s per save at 50k Images. The first save after opening a folder still indexes it once. ([#3129](https://github.com/wkentaro/labelme/pull/3129))
> - Browsing Images with a kept Brightness/Contrast no longer grows memory by the size of each Image it opens. ([#3130](https://github.com/wkentaro/labelme/pull/3130))
> - Merging Mask Shapes moved by half a pixel no longer shifts one of them a pixel away from the others. ([#3132](https://github.com/wkentaro/labelme/pull/3132))
> - The AI Models panel opens faster by sharing a single model catalog read with the toolbar. ([#3147](https://github.com/wkentaro/labelme/pull/3147))

### [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0)
<sub>2026-11-14 · 12d ago</sub>

> **Changed**
> - SAM 3 asks to be downloaded again, as 1.8 GB on a GPU or 3.7 GB on the CPU, and asks again for its CPU files when AI falls back to the CPU. Its files from earlier versions stay on disk. ([#3099](https://github.com/wkentaro/labelme/pull/3099))
> - AI no longer retries a request on the CPU when the GPU fails partway through; the next request loads the model again. The status bar no longer shows "Preparing image…". ([#3100](https://github.com/wkentaro/labelme/pull/3100))
> **Fixed**
> - The model menu shows the download size for the AI device: SAM 3 shows about 1.8 GB on a GPU instead of its CPU size. ([#3104](https://github.com/wkentaro/labelme/pull/3104))
> - Deleting an AI model no longer freezes the window while AI runs, and other loaded models stay loaded. ([#3105](https://github.com/wkentaro/labelme/pull/3105))
> …

### [v7.10.0](https://github.com/wkentaro/labelme/releases/tag/v7.10.0)
<sub>2026-11-13 · 13d ago</sub>

> **Added**
> - Allow drawing Polygon and LineStrip paths by dragging, simplifying strokes into fewer vertices while preserving click-to-add input. ([#2757](https://github.com/wkentaro/labelme/pull/2757))
> - Add 3-point circle mode (`circle_3p`) to draw circles by clicking three points on the circumference. ([#2788](https://github.com/wkentaro/labelme/pull/2788))
> - Open JPEG 2000 Images (.jp2, .jpx, .j2k, .j2c) through Pillow with OpenJPEG support, including folder scanning and drag-and-drop, while preserving decoded pixels and transparency in memory. ([#2833](https://github.com/wkentaro/labelme/pull/2833))
> - `labelme.log` records the platform, the installed AI runtime versions, and how long each AI model takes to load, encode an image and generate annotations, to help debug GPU problems. ([#2849](https://github.com/wkentaro/labelme/pull/2849))
> - A Compute device Setting runs AI on the CPU, and the status bar shows while AI is running and whether it runs on the CPU. ([#2861](https://github.com/wkentaro/labelme/pull/2861))
> …

### [v7.9.1](https://github.com/wkentaro/labelme/releases/tag/v7.9.1)
<sub>2026-10-25 · 1mo ago</sub>

> **Fixed**
> - Fix a point dragged inside a box being lost on image switch, because the move was never saved or added to undo history. ([#2845](https://github.com/wkentaro/labelme/pull/2845))
> - Hovering where Shapes overlap now highlights the Shape a click selects, so a point drawn inside a box is highlighted and picked over the box. ([#2846](https://github.com/wkentaro/labelme/pull/2846))

### [v7.9.0](https://github.com/wkentaro/labelme/releases/tag/v7.9.0)
<sub>2026-10-20 · 1mo ago</sub>

> **Added**
> - Allow double-clicking a shape on the canvas to open the label-edit dialog. ([#2744](https://github.com/wkentaro/labelme/pull/2744))
> - Lock shapes against editing with Lock Shapes / Unlock Shapes (`Ctrl+Shift+L`); the lock is saved per shape as `"locked": true` in the annotation file. ([#2755](https://github.com/wkentaro/labelme/pull/2755))
> - Add Fit to Selection (`Ctrl+Shift+F`) to the View menu and toolbar, a zoom mode that fits the view to the selected shapes, with padding, whenever the selection changes. ([#2758](https://github.com/wkentaro/labelme/pull/2758))
> - Labelme remembers the Annotation Folder for each opened folder across restarts, including one given with `--output`, which Labelme now creates at startup if it is missing. ([#2775](https://github.com/wkentaro/labelme/pull/2775))
> - The Image List has a footer that shows the Annotation Folder and how many images are annotated, for example "3 of 5 annotated · next to images", with Change Annotation Folder… and an option to go back to saving next to images. A remembered folder that is missing shows a warning there. ([#2776](https://github.com/wkentaro/labelme/pull/2776), [#2778](https://github.com/wkentaro/labelme/pull/2778), [#2808](https://github.com/wkentaro/labelme/pull/2808))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Merge pull request #3158 from wkentaro/chore/mdformat-frontmatter](https://github.com/wkentaro/labelme/commit/edde3fc63e7c57b4c994c3b20bbfb1f5a5da84ef) | wkentaro |
| 2026-11-26 | [chore: add mdformat-frontmatter to the dev group](https://github.com/wkentaro/labelme/commit/1ce60d12b49d8f743c17f113a2bc49848b4c5091) | wkentaro |
| 2026-11-26 | [Merge pull request #3153 from wkentaro/fix/display-16bit-range](https://github.com/wkentaro/labelme/commit/16d025c8193fcd88349e8e0428590bb9d8b7218c) | wkentaro |
| 2026-11-26 | [Merge pull request #3137 from SajjadPSavoji/fix-3121-quitting-while-a…](https://github.com/wkentaro/labelme/commit/f195fdc28baad055e966ccd2e29ac56d6674e60f) | wkentaro |
| 2026-11-26 | [docs: add changelog fragment for #3153](https://github.com/wkentaro/labelme/commit/1f39baf3ee369f2b7f03cde08c2d5ea253c4a2d1) | wkentaro |
| 2026-11-26 | [fix: show 16-bit grayscale from its minimum to its maximum](https://github.com/wkentaro/labelme/commit/f40d2a79323ab9c862d5aa2fb21d56cb8240b8ba) | wkentaro |
| 2026-11-26 | [test: show 16-bit grayscale from black to white across its range](https://github.com/wkentaro/labelme/commit/b5d1ac151de5f4cd28a8af848afac760326d8d2a) | wkentaro |
| 2026-11-26 | [docs: add changelog fragment for #3152](https://github.com/wkentaro/labelme/commit/ac84444c49a201a66aecc0afcdd311a7cff5cd5e) | wkentaro |
| 2026-11-26 | [fix: adjust brightness and contrast from the image the canvas shows](https://github.com/wkentaro/labelme/commit/ec89081320b77061e577923f73d324f9cf00402b) | wkentaro |
| 2026-11-26 | [test: show a 16-bit image unchanged after neutral Brightness/Contrast](https://github.com/wkentaro/labelme/commit/dcce3631ae69320cf50bd0591ce0a7e351805f07) | wkentaro |

[See all commits ↗](https://github.com/wkentaro/labelme/commits)

## ⬇️ Get it

```bash
git clone https://github.com/wkentaro/labelme.git
```
