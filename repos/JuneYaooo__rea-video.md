# JuneYaooo/rea-video

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/JuneYaooo/rea-video)

> Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open VIDEO.md format. 逆向一切视频，逐个镜头看是拍的、AI 生成的还是代码做的，再告诉你怎么复刻；拆解结果按 VIDEO.md 格式输出。

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | — |
| **Why it's worth a look** | Reverse-engineer any video shot by shot |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 12.6k |
| 🍴 **Forks** | 1.8k |
| 🐞 **Open issues + PRs** | [10](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 73.6 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 11d ago</sub>

> **视频拆解标准包 Reel，报告重写，音效单独分离**
> 这一版定下了视频拆解的标准包格式：拆片包（Reel）。拆一条视频现在得到两样东西：给人看的报告（HTML / PDF），和给模型、下游项目读的拆片包。格式介绍和规范见 [docs/reel.md](https://github.com/JuneYaooo/rea-video/blob/v0.1.0/docs/reel.md)。
> **拆片包 Reel**
> - 四层逐级展开：卡片 → 概览和地图 → 时间线（一行一镜）→ 单镜文件，最后才是完整数据。一条 3 分钟口播读到概览约 2k token，完整数据约 19 万 token。
> - 每个文件开头写着自己的 token 数；看到的和推断的分开写，时间线里推断的键名带 `~`。
> - 字段有 JSON Schema（`rea_video/reel.schema.json`）。`rea-video reel out/ref --check` 检查一个目录是否合格，`reel.read()` 读出结构化数据。
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Use Gemini directly and keep evals local](https://github.com/JuneYaooo/rea-video/commit/9572a00bbccf0baa272983893b5c0c3589875088) | JuneYaooo |
| 2026-11-23 | [Tighten model answers and remake frames](https://github.com/JuneYaooo/rea-video/commit/4a8dcded6a57ccbba07f3168b1bb2707bf60c376) | JuneYaooo |
| 2026-11-23 | [Keep face_area median at MIN_AREA and use linear projection for SFX s…](https://github.com/JuneYaooo/rea-video/commit/99033f7ec8e2ddd51da40259d99d679897860c95) | JuneYaooo |
| 2026-11-23 | [Fix review precedence, moments v3 edge cases, DIY remake fallback, an…](https://github.com/JuneYaooo/rea-video/commit/92b9df33140843ac4376afcd1c5f8432043d30be) | JuneYaooo |
| 2026-11-22 | [Align model limits with vendor docs](https://github.com/JuneYaooo/rea-video/commit/a124acd4a02b3a9b72b9e7dedca5d1bfcda2a7b8) | JuneYaooo |
| 2026-11-22 | [Point remakes to Capsule recipes first](https://github.com/JuneYaooo/rea-video/commit/574c47a2ce5dfc8b2197d64f7cfae02755736b78) | JuneYaooo |
| 2026-11-22 | [Flag reference frames that conflict with swaps](https://github.com/JuneYaooo/rea-video/commit/01258b9e85a270dc49d1725819ced6d60228ec7b) | JuneYaooo |
| 2026-11-22 | [Weigh image reviews and uncertain shots more carefully](https://github.com/JuneYaooo/rea-video/commit/9f1b075d6a7b1a6782feb5f4e8d3dd83a3dc5762) | JuneYaooo |
| 2026-11-22 | [Keep remake execution in one place](https://github.com/JuneYaooo/rea-video/commit/de506fd5f157315b4089629286af1ab96c01a072) | JuneYaooo |
| 2026-11-22 | [Make remake runs more reliable](https://github.com/JuneYaooo/rea-video/commit/90eae960d13643e24a0066d6f569df7f390f0567) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
