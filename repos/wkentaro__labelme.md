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
| 🐞 **Open issues + PRs** | [95](https://github.com/wkentaro/labelme/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `image-annotation` `python` `computer-vision` `annotations` `deep-learning` `semantic-segmentation` `instance-segmentation` `video-annotation` `classification` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2016-05-09 |
| 📦 **Latest release** | [v7.11.1](https://github.com/wkentaro/labelme/releases/tag/v7.11.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 70.3 MB |
| 🌐 **Website** | https://labelme.io |

## 📦 Recent releases

### [v7.11.1](https://github.com/wkentaro/labelme/releases/tag/v7.11.1)
<sub>2026-11-25 · 2d ago</sub>

> **Fixed**
> - AI-Segment and AI-Find All work again on images over 179 MP, which failed with "Image size exceeds limit" since 7.11.0. Labelme sends the AI server the image at the model's input size instead of in full, so SAM2 segments a 600 MP image in about a second. Labelme requires osam 0.12.1 or later. ([#3126](https://github.com/wkentaro/labelme/pull/3126))
> - Auto-save in a folder of thousands of Images no longer rescans every Image after each save, which paused the window for up to 0.3 s per save at 50k Images. The first save after opening a folder still indexes it once. ([#3129](https://github.com/wkentaro/labelme/pull/3129))
> - Browsing Images with a kept Brightness/Contrast no longer grows memory by the size of each Image it opens. ([#3130](https://github.com/wkentaro/labelme/pull/3130))
> - Merging Mask Shapes moved by half a pixel no longer shifts one of them a pixel away from the others. ([#3132](https://github.com/wkentaro/labelme/pull/3132))
> - The AI Models panel opens faster by sharing a single model catalog read with the toolbar. ([#3147](https://github.com/wkentaro/labelme/pull/3147))

### [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0)
<sub>2026-11-14 · 13d ago</sub>

> **Changed**
> - SAM 3 asks to be downloaded again, as 1.8 GB on a GPU or 3.7 GB on the CPU, and asks again for its CPU files when AI falls back to the CPU. Its files from earlier versions stay on disk. ([#3099](https://github.com/wkentaro/labelme/pull/3099))
> - AI no longer retries a request on the CPU when the GPU fails partway through; the next request loads the model again. The status bar no longer shows "Preparing image…". ([#3100](https://github.com/wkentaro/labelme/pull/3100))
> **Fixed**
> - The model menu shows the download size for the AI device: SAM 3 shows about 1.8 GB on a GPU instead of its CPU size. ([#3104](https://github.com/wkentaro/labelme/pull/3104))
> - Deleting an AI model no longer freezes the window while AI runs, and other loaded models stay loaded. ([#3105](https://github.com/wkentaro/labelme/pull/3105))
> …

### [v7.10.0](https://github.com/wkentaro/labelme/releases/tag/v7.10.0)
<sub>2026-11-13 · 14d ago</sub>

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
| 2026-11-27 | [Merge pull request #3168 from wkentaro/fix/tiff-16bit-display](https://github.com/wkentaro/labelme/commit/722c4d43335777a12ee16d13468db5c1f88ace4c) | wkentaro |
| 2026-11-27 | [Merge pull request #3164 from wkentaro/docs/verify-labelme-features](https://github.com/wkentaro/labelme/commit/6f1c36b032c70e03a5d786a82dd30121781467c1) | wkentaro |
| 2026-11-27 | [chore: add the changelog entry for #3168](https://github.com/wkentaro/labelme/commit/643166e144f675527a4c4dfd21334d844363a7f4) | wkentaro |
| 2026-11-27 | [fix: keep 16-bit grayscale TIFF pixels at 16 bits](https://github.com/wkentaro/labelme/commit/159bdd8fc1f1bcc94c22ad250c71a8fba39f32ab) | wkentaro |
| 2026-11-27 | [test: show a 16-bit TIFF at the gray level a PNG shows](https://github.com/wkentaro/labelme/commit/7a140a149385d02040174fa3dfd544adb14e3004) | wkentaro |
| 2026-11-27 | [chore: add the changelog entry for #3174](https://github.com/wkentaro/labelme/commit/d72e6075cda0f11e752e0b76da40629003f2e0b2) | wkentaro |
| 2026-11-27 | [fix: honor MINISWHITE in _imread_tiff](https://github.com/wkentaro/labelme/commit/c04160011ed286a27a42d823ec659495842192de) | wkentaro |
| 2026-11-27 | [test: read a MINISWHITE TIFF as the same MINISBLACK TIFF](https://github.com/wkentaro/labelme/commit/f68c2bb71545a8231d2a3ae528f591daf9f8b915) | wkentaro |
| 2026-11-27 | [docs: note that Open File is ambiguous on the welcome screen too](https://github.com/wkentaro/labelme/commit/61bcc8064a77ad732c8990a59c9e071cc0a9bd8e) | wkentaro |
| 2026-11-27 | [docs: check the shapes a quit-save keeps, then reopen them](https://github.com/wkentaro/labelme/commit/1fd44ae3da684234b2d5c7f1f95a38dda0465a2f) | wkentaro |

[See all commits ↗](https://github.com/wkentaro/labelme/commits)

## ⬇️ Get it

```bash
git clone https://github.com/wkentaro/labelme.git
```
