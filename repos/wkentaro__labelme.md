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
| 🐞 **Open issues + PRs** | [78](https://github.com/wkentaro/labelme/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `image-annotation` `python` `computer-vision` `annotations` `deep-learning` `semantic-segmentation` `instance-segmentation` `video-annotation` `classification` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2016-05-09 |
| 📦 **Latest release** | [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 71.5 MB |
| 🌐 **Website** | https://labelme.io |

## 📦 Recent releases

### [v7.11.0](https://github.com/wkentaro/labelme/releases/tag/v7.11.0)
<sub>2026-11-14 · 5d ago</sub>

> **Changed**
> - SAM 3 asks to be downloaded again, as 1.8 GB on a GPU or 3.7 GB on the CPU, and asks again for its CPU files when AI falls back to the CPU. Its files from earlier versions stay on disk. ([#3099](https://github.com/wkentaro/labelme/pull/3099))
> - AI no longer retries a request on the CPU when the GPU fails partway through; the next request loads the model again. The status bar no longer shows "Preparing image…". ([#3100](https://github.com/wkentaro/labelme/pull/3100))
> **Fixed**
> - The model menu shows the download size for the AI device: SAM 3 shows about 1.8 GB on a GPU instead of its CPU size. ([#3104](https://github.com/wkentaro/labelme/pull/3104))
> - Deleting an AI model no longer freezes the window while AI runs, and other loaded models stay loaded. ([#3105](https://github.com/wkentaro/labelme/pull/3105))
> …

### [v7.10.0](https://github.com/wkentaro/labelme/releases/tag/v7.10.0)
<sub>2026-11-13 · 6d ago</sub>

> **Added**
> - Allow drawing Polygon and LineStrip paths by dragging, simplifying strokes into fewer vertices while preserving click-to-add input. ([#2757](https://github.com/wkentaro/labelme/pull/2757))
> - Add 3-point circle mode (`circle_3p`) to draw circles by clicking three points on the circumference. ([#2788](https://github.com/wkentaro/labelme/pull/2788))
> - Open JPEG 2000 Images (.jp2, .jpx, .j2k, .j2c) through Pillow with OpenJPEG support, including folder scanning and drag-and-drop, while preserving decoded pixels and transparency in memory. ([#2833](https://github.com/wkentaro/labelme/pull/2833))
> - `labelme.log` records the platform, the installed AI runtime versions, and how long each AI model takes to load, encode an image and generate annotations, to help debug GPU problems. ([#2849](https://github.com/wkentaro/labelme/pull/2849))
> - A Compute device Setting runs AI on the CPU, and the status bar shows while AI is running and whether it runs on the CPU. ([#2861](https://github.com/wkentaro/labelme/pull/2861))
> …

### [v7.9.1](https://github.com/wkentaro/labelme/releases/tag/v7.9.1)
<sub>2026-10-25 · 25d ago</sub>

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

### [v7.8.1](https://github.com/wkentaro/labelme/releases/tag/v7.8.1)
<sub>2026-10-07 · 1mo ago</sub>

> **Fixed**
> - Avoid image hashing when loading images while preserving AI embedding reuse when revisiting unchanged images. ([#2741](https://github.com/wkentaro/labelme/pull/2741))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Merge pull request #3129 from wkentaro/perf/image-list-checkmarks-per…](https://github.com/wkentaro/labelme/commit/7e840675431402a3f449b8efc5c090ac1f172017) | wkentaro |
| 2026-11-19 | [Merge pull request #3130 from wkentaro/fix/brightness-contrast-dialog…](https://github.com/wkentaro/labelme/commit/5cadd8a85cb296a342cef042141534cd0dddc44a) | wkentaro |
| 2026-11-19 | [docs: note the faster Image List saves in the changelog](https://github.com/wkentaro/labelme/commit/c64e79a8099a6afa5e69a254ae2036eed7922eeb) | wkentaro |
| 2026-11-19 | [perf: update Image List checkmarks without scanning every image](https://github.com/wkentaro/labelme/commit/48a7e2d5d3e0d233fd1fe1c28b613817f470cc3d) | wkentaro |
| 2026-11-19 | [fix: list an image dropped twice only once](https://github.com/wkentaro/labelme/commit/a8e5dead662aa114e08829bf6ac799942112254b) | wkentaro |
| 2026-11-19 | [docs: note the Brightness/Contrast memory fix in the changelog](https://github.com/wkentaro/labelme/commit/abab02a87ed009b389582689b3418f14f877b519) | wkentaro |
| 2026-11-19 | [fix: free the Brightness/Contrast dialog after each use](https://github.com/wkentaro/labelme/commit/4bdcef365de91861b057d2dba712eea00b863f6e) | wkentaro |
| 2026-11-19 | [refactor: adjust brightness and contrast without the dialog](https://github.com/wkentaro/labelme/commit/04cd87dc9d1447fc775d69bcbed7495ee989f71c) | wkentaro |
| 2026-11-19 | [Merge pull request #3126 from wkentaro/fix/ai-model-resolution](https://github.com/wkentaro/labelme/commit/7f16433758f3917dda259b1c5b6f0e3567344443) | wkentaro |
| 2026-11-19 | [docs: note the large-image AI fix in the changelog](https://github.com/wkentaro/labelme/commit/43688d3a25bd74c4b0f223724f6c20740fd7d0cc) | wkentaro |

[See all commits ↗](https://github.com/wkentaro/labelme/commits)

## ⬇️ Get it

```bash
git clone https://github.com/wkentaro/labelme.git
```
