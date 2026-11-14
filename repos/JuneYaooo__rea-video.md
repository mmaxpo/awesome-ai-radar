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
| ⭐ **Stars** | 8.4k |
| 🍴 **Forks** | 1.2k |
| 🐞 **Open issues + PRs** | [4](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 153.1 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 2d ago</sub>

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
| 2026-11-14 | [Point multi-episode dramas to rea-toon in FAQ](https://github.com/JuneYaooo/rea-video/commit/751596967f58b8949124d291e59bdc40fc04486e) | JuneYaooo |
| 2026-11-14 | [Keep local notes out of the repo](https://github.com/JuneYaooo/rea-video/commit/fe67e634f085c1a2360b610e1bf6154ab58bd6c9) | JuneYaooo |
| 2026-11-14 | [Keep tests local](https://github.com/JuneYaooo/rea-video/commit/a01deeef423f4dbe1e7bcc399d2a7d864c951a7d) | JuneYaooo |
| 2026-11-14 | [Drop old breakdown format handling](https://github.com/JuneYaooo/rea-video/commit/a9f3fe6a1c990010eca443644b19677ad4a9a97b) | JuneYaooo |
| 2026-11-14 | [Step-by-step remake guide by video kind](https://github.com/JuneYaooo/rea-video/commit/1f4817d64965fe91b48d5ac02c5e4735f1f0f3eb) | JuneYaooo |
| 2026-11-14 | [Merge pull request #45 from Choihello/feat/korean-ocr](https://github.com/JuneYaooo/rea-video/commit/d9659f6a8cd8056c1032dfaaab93421e08fe6714) | JuneYaooo |
| 2026-11-14 | [README: Star History](https://github.com/JuneYaooo/rea-video/commit/ce1c4c1ebf95172376742cb784d35f005a84f436) | JuneYaooo |
| 2026-11-14 | [Add --ocr-lang ko: Korean subtitle OCR](https://github.com/JuneYaooo/rea-video/commit/f95101621590684bded7b72d7895bc2925b91534) | Choihello |
| 2026-11-14 | [README: remove Star History for now](https://github.com/JuneYaooo/rea-video/commit/124343f8acd09f2ae2e0ea4612a8d7512de4988d) | JuneYaooo |
| 2026-11-14 | [Write the code remake's text from the breakdown](https://github.com/JuneYaooo/rea-video/commit/f5c8b450f9eefa9757462a1febe63eb5d52ccf4f) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
