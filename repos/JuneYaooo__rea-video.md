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
| ⭐ **Stars** | 9.5k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [6](https://github.com/JuneYaooo/rea-video/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering` `remotion` `reverse-engineering` `short-video` `shot-detection` `subtitles` `video-analysis` `video-breakdown` `video-editing` `video-generation` `vlm` `videomd` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-10-29 |
| 📦 **Latest release** | [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 153.6 MB |
| 🌐 **Website** | https://www.reavideo.ai/ |

## 📦 Recent releases

### [v0.1.0](https://github.com/JuneYaooo/rea-video/releases/tag/v0.1.0)
<sub>2026-11-11 · 4d ago</sub>

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
| 2026-11-16 | [Keep calls whole when swapped subjects have no image](https://github.com/JuneYaooo/rea-video/commit/e83d5874beb6429d9488129c7f046755b60a5371) | JuneYaooo |
| 2026-11-16 | [Plan generation from the remake intent and the model's limits](https://github.com/JuneYaooo/rea-video/commit/b5cbfee5c1987e3441b5223cb94beee2c542ba6f) | JuneYaooo |
| 2026-11-16 | [Plan remakes per model and split the report into breakdown and remake](https://github.com/JuneYaooo/rea-video/commit/8db6cdf96d0c981d94daa22172c0f0c36187f159) | JuneYaooo |
| 2026-11-16 | [Add Turkish flow diagram](https://github.com/JuneYaooo/rea-video/commit/820d661e807034e0f0284262b4e93085cfd3da49) | JuneYaooo |
| 2026-11-16 | [docs: add Turkish README (#47)](https://github.com/JuneYaooo/rea-video/commit/b6f5c7a002616308c5181f04969cbef3d71517de) | lprvy |
| 2026-11-15 | [Tighten motion drive detection and caption erasing](https://github.com/JuneYaooo/rea-video/commit/ebe853e330d63719a1f91754f789647c515eac19) | JuneYaooo |
| 2026-11-15 | [Motion drive for dance and action shots](https://github.com/JuneYaooo/rea-video/commit/5b09832ab64c334045b99aaaeb8207e86da765e8) | JuneYaooo |
| 2026-11-14 | [Point multi-episode dramas to rea-toon in FAQ](https://github.com/JuneYaooo/rea-video/commit/751596967f58b8949124d291e59bdc40fc04486e) | JuneYaooo |
| 2026-11-14 | [Keep local notes out of the repo](https://github.com/JuneYaooo/rea-video/commit/fe67e634f085c1a2360b610e1bf6154ab58bd6c9) | JuneYaooo |
| 2026-11-14 | [Keep tests local](https://github.com/JuneYaooo/rea-video/commit/a01deeef423f4dbe1e7bcc399d2a7d864c951a7d) | JuneYaooo |

[See all commits ↗](https://github.com/JuneYaooo/rea-video/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JuneYaooo/rea-video.git
```
