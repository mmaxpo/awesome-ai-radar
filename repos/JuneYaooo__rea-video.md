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
| ⭐ **Stars** | 11.6k |
| 🍴 **Forks** | 1.7k |
| 🐞 **Open issues + PRs** | [8](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 72.8 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 9d ago</sub>

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
| 2026-11-21 | [Handle image paths and Windows setup](https://github.com/JuneYaooo/rea-video/commit/4d98dd8dd1838edfa58037cf4df9d1cccc245da7) | JuneYaooo |
| 2026-11-21 | [Report a missing ffmpeg when probe runs, not a missing file](https://github.com/JuneYaooo/rea-video/commit/73541597454c29281103e03029ba7bdb439875b7) | xdAsaah |
| 2026-11-21 | [Tell Windows users how to install ffmpeg and Python, and how to link …](https://github.com/JuneYaooo/rea-video/commit/1526ca3b3c9c166f16a6425f34667981d7041725) | xdAsaah |
| 2026-11-21 | [Find browsers in the 64-bit and per-user Windows install locations](https://github.com/JuneYaooo/rea-video/commit/6eb1e1779e57426a3ccf3b2e4cd8d992ce8180b5) | xdAsaah |
| 2026-11-20 | [Find magic reveals and highlight moments](https://github.com/JuneYaooo/rea-video/commit/131d1527557d2cccacb64059d47560964235acd7) | JuneYaooo |
| 2026-11-20 | [Fix SyntaxError on Python <=3.11: apostrophe inside single-quoted f-s…](https://github.com/JuneYaooo/rea-video/commit/82d5463890cbeb1b8442072b8e4665e7efdd76a2) | Godward-Bound |
| 2026-11-19 | [Keep frame select expressions shallow](https://github.com/JuneYaooo/rea-video/commit/cf12cc73353635dc859cd7fb8a0c471c03ab150d) | JuneYaooo |
| 2026-11-19 | [Update 3D-Speaker CAM++ checksum after sherpa-onnx re-export](https://github.com/JuneYaooo/rea-video/commit/cd2ca431bdf236d6123f320170bd0d762c2e384d) | BitmanAlan |
| 2026-11-19 | [Update ChatCut entry](https://github.com/JuneYaooo/rea-video/commit/ac470773188574833b839be17abee6162201ddf9) | JuneYaooo |
| 2026-11-19 | [Label sponsored tool in skill replies](https://github.com/JuneYaooo/rea-video/commit/7b411d5f18f5ba051465270ac0d7aad49e486d72) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
