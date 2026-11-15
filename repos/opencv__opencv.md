# opencv/opencv

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/opencv/opencv)

> Open Source Computer Vision Library

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | The standard computer-vision library (pip install opencv-python) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 91.6k |
| 🍴 **Forks** | 57.1k |
| 🐞 **Open issues + PRs** | [2.9k](https://github.com/opencv/opencv/issues) |
| 💻 **Languages** | C++ 86% · Python 4% · C 3% · CMake 2% · Java 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `opencv` `c-plus-plus` `computer-vision` `deep-learning` `image-processing` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2012-07-19 |
| 📦 **Latest release** | [5.1.0](https://github.com/opencv/opencv/releases/tag/5.1.0) — 2026-11-06 |
| 🌿 **Default branch** | `5.x` |
| 💾 **Size** | 558.7 MB |
| 🌐 **Website** | https://opencv.org |

## 📦 Recent releases

### [5.1.0](https://github.com/opencv/opencv/releases/tag/5.1.0) — OpenCV 5.1.0
<sub>2026-11-06 · 9d ago</sub>

> OpenCV 5.1.0 has been released.
> :hammer_and_wrench: Change log is [here](https://github.com/opencv/opencv/wiki/OpenCV-Change-Logs#version510).

### [4.14.0](https://github.com/opencv/opencv/releases/tag/4.14.0) — OpenCV 4.14.0
<sub>2026-07-19 · 3mo ago</sub>

> OpenCV 4.14.0 has been released.
> :hammer_and_wrench: Change log is [here](https://github.com/opencv/opencv/wiki/OpenCV-Change-Logs#version4140).
> **NOTE:** Windows-on-Arm binaries have been validated on Qualcomm Snapdragon devices. Devices with private L2 caches, PPL auto-partitioning may fail in some cases. For those, we recommend building with OpenMP and using it instead.

### [5.0.0](https://github.com/opencv/opencv/releases/tag/5.0.0) — OpenCV 5.0.0
<sub>2026-06-06 · 5mo ago</sub>

> OpenCV 5.0.0 released!
> OpenCV 5.0.0 overview: https://opencv.org/opencv-5
> OpenCV 4.x -> 5.x migration guide: https://github.com/opencv/opencv/wiki/OpenCV-4-to-5-migration
> **NOTE:** The original Android SDK  was built with old NDK and includes standard C++ library not properly aligned for devices with 16kb pages. Please use the package with "16kb-page-fix" suffix for Google Play releases.
> **NOTE:** Windows-on-Arm binaries have been validated on Qualcomm Snapdragon devices. Devices with private L2 caches, PPL auto-partitioning may fail in some cases. For those, we recommend building with OpenMP and using it instead.

### [4.13.0](https://github.com/opencv/opencv/releases/tag/4.13.0) — OpenCV 4.13.0
<sub>2025-12-31 · 10mo ago</sub>

> OpenCV 4.13.0 has been released.
> :hammer_and_wrench: Change log is [here](https://github.com/opencv/opencv/wiki/OpenCV-Change-Logs#version4130).

### [4.12.0](https://github.com/opencv/opencv/releases/tag/4.12.0) — OpenCV 4.12.0
<sub>2025-07-02 · 1y ago</sub>

> OpenCV 4.12.0 has been released.
> :hammer_and_wrench: Change log is [here](https://github.com/opencv/opencv/wiki/OpenCV-Change-Logs#version4120).

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Merge pull request #30774 from tanveer-arch/fix-applycolormap-1x256](https://github.com/opencv/opencv/commit/b3d14b1caf41abb74d101a898b1fcae841152a24) | abhishek-gola |
| 2026-11-15 | [dnn: compute LogSoftmax without taking the log of softmax (5.x) 🤖🤖🤖 (…](https://github.com/opencv/opencv/commit/d87ac83e055e7ccff8d803e3c40de3289905bb90) | usmanmateen |
| 2026-11-15 | [doc(core): fix LUT index formula for CV_8S and CV_16S inputs (#30793)](https://github.com/opencv/opencv/commit/cc26a67b62279ce137f327a9c6a6f826fef3928e) | sshivensolanki |
| 2026-11-15 | [samples: add error check for invalid frame count in application_trace…](https://github.com/opencv/opencv/commit/be7eede9c5abc22ec53cc02bef6e61ca53d0de25) | sultan-ai-and-ml |
| 2026-11-15 | [Merge pull request #30679 from amd/port_5.x_pyrDown](https://github.com/opencv/opencv/commit/b6185cb36571aada94dbffe6868542ef9e60a1af) | madanm3 |
| 2026-11-13 | [Fix dead links in Python tutorials (#30775)](https://github.com/opencv/opencv/commit/205613a29728c2217049bdddbbe98322b485b34e) | mgeethikasaisri09-eng |
| 2026-11-13 | [Merge pull request #30706 from sshivensolanki/core-locateroi-1d (#30706)](https://github.com/opencv/opencv/commit/efe44093c383b7996b27da98f595dddc18f05a89) | sshivensolanki |
| 2026-11-13 | [Merge pull request #30655 from sshivensolanki/core-add-sub-64-saturat…](https://github.com/opencv/opencv/commit/f62ce23b91a846e60103f222cab406e34638570e) | abhishek-gola |
| 2026-11-13 | [dnn: keep INT4/UINT4 QuantizeLinear off the AVX2 per-tensor fast path…](https://github.com/opencv/opencv/commit/998f72949d6bcfc5b1bf87ef57c464c5708803ed) | Kaustubh1235 |
| 2026-11-13 | [video: dis: vectorize Densification_ParBody with scalable intrinsics …](https://github.com/opencv/opencv/commit/07b31f1e2e8928d280fa59c99418e3b4ad24cfca) | velonica0 |

[See all commits ↗](https://github.com/opencv/opencv/commits)

## ⬇️ Get it

```bash
git clone https://github.com/opencv/opencv.git
```
