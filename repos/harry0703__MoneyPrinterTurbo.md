# harry0703/MoneyPrinterTurbo

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/harry0703/MoneyPrinterTurbo)

> 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | — |
| **Why it's worth a look** | Generates short-form videos with AI from a topic |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 145.6k |
| 🍴 **Forks** | 23.4k |
| 🐞 **Open issues + PRs** | [91](https://github.com/harry0703/MoneyPrinterTurbo/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `tiktok` `ai-video-generator` `content-creation` `ffmpeg` `instagram-reels` `llm` `short-video` `subtitles` `text-to-speech` `video-automation` `video-workflow` `workflow-automation` `youtube-shorts` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2024-03-11 |
| 📦 **Latest release** | [v1.3.11](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.11) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 529.6 MB |

## 📦 Recent releases

### [v1.3.11](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.11)
<sub>2026-11-23 · 2d ago</sub>

> [English](#en-v1.3.11) | [中文](#cn-v1.3.11)
> <h2 id="en-v1.3.11">Highlights</h2>
> - Added **[Aigei](https://www.aigei.com/?utm_source=github&utm_medium=sponsorship&utm_campaign=moneyprinterturbo)** as a stock video source.
> - Added **useapi.net** as a source for AI video and images.
> - Added **APINEBULA, APIXO Responses, AtmoRouter, and MartLLM** (formerly UberLLM) as LLM providers.
> - Improved **local rendering performance** by reducing per-frame compositing work for subtitles, letterboxing, and slide transitions.
> …

### [v1.3.10](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.10)
<sub>2026-11-07 · 18d ago</sub>

> [English](#en-v1.3.10) | [中文](#cn-v1.3.10)
> <h2 id="en-v1.3.10">Highlights</h2>
> - Added **OpenAI Codex subscription access** with device-code sign-in and dynamic model selection, plus a separate **ChatGPT Native OAuth** provider. Native OAuth availability depends on account eligibility; existing Codex sign-in remains independent.
> - Added **Codex image generation** as a material source. Text and image generation can share the application's Codex login, and generated images support the existing static and slow zoom effects.
> - Added **Infistar and Jalapeno Cloud** for LLM and video generation, alongside **Runcrate, CloudGPU, and cheapaimodel** LLM providers.
> - Improved **long-running video generation feedback** with generation stages, elapsed time, and polling status. Task tracking survives page refreshes and temporary query failures, with protection against duplicate submissions.
> …

### [v1.3.9](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.9)
<sub>2026-10-21 · 1mo ago</sub>

> [English](#en-v1.3.9) | [中文](#cn-v1.3.9)
> <h2 id="en-v1.3.9">Highlights</h2>
> - Added official **`mpt` pip packaging**. Start the WebUI with `mpt webui` or generate videos with `mpt cli`.
> - Added **static and slow zoom image effects** for local and AI-generated images. Slow zoom remains the default.
> - Added Kimi Code subscription access with browser authorization, alongside improvements to the sign-in dialog, status updates, and cancellation.
> - Added an optional **local SDXL image server** for the OpenAI-compatible image material workflow, with idle GPU offloading.
> …

### [v1.3.8](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.8)
<sub>2026-10-03 · 1mo ago</sub>

> [English](#en-v1.3.8) | [中文](#cn-v1.3.8)
> <h2 id="en-v1.3.8">Highlights</h2>
> - Added continuous progress reporting during stock footage downloads, clip processing, and final rendering, with task logs from background helper threads visible in the WebUI.
> - Added configurable stock material and clip rendering concurrency. Stock material concurrency applies to Pexels, Pixabay, and Coverr; both settings default to **1 (serial processing)**.
> - Added VoxCPM reference-audio voice cloning and optional delivery conditioning to carry over pacing and emotion, with local Whisper transcription for editable reference transcripts.
> - Added Fluxion AI, Cheaper Inference, Requesty, FutureInfra, Y-API, and iFlytek Spark (Astron MaaS) LLM providers.
> …

### [v1.3.7](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.7)
<sub>2026-09-13 · 2mo ago</sub>

> [English](#en-v1.3.7) | [中文](#cn-v1.3.7)
> <h2 id="en-v1.3.7">Highlights</h2>
> - Added word-by-word subtitles and a pop-up spring animation, with independent controls for display mode and animation in the WebUI.
> - Added preset background music selection with in-browser audio preview, so you can listen before generating a video.
> - Added native pauses to scripts with Azure TTS V1 (Edge TTS): use `[pause: 2s]` or `[停顿: 2s]` to insert silence while keeping narration and subtitles aligned.
> - Added Kokoro and VoxCPM TTS providers. Kokoro supports a self-hosted OpenAI-compatible service and automatically loads the server's voice list.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [feat(llm): add TeamoRouter provider](https://github.com/harry0703/MoneyPrinterTurbo/commit/2dc10e850d78c61264a64ea180def2b7f1f334d8) | 2867297362mjb-sketch |
| 2026-11-25 | [feat(desktop): add cross-platform desktop app](https://github.com/harry0703/MoneyPrinterTurbo/commit/3837b078227a59adc6483fbf409376bd616413aa) | harry0703 |
| 2026-11-24 | [fix(material): use Wan 3.0 by default (#1842)](https://github.com/harry0703/MoneyPrinterTurbo/commit/dabfd3f8548d30ed0eea8759decbdead9626e0e6) | chengzeyi |
| 2026-11-23 | [chore: release v1.3.11](https://github.com/harry0703/MoneyPrinterTurbo/commit/3482168e8958a73c48656634c750a5ce459224df) | harry0703 |
| 2026-11-23 | [fix(api): reject a null video_aspect before the task starts](https://github.com/harry0703/MoneyPrinterTurbo/commit/708ac4836c14f77196c5d1f23cc0885ac9014c04) | HEOJUNFO |
| 2026-11-23 | [fix(api): reject a blank video_script on /audio and /subtitle](https://github.com/harry0703/MoneyPrinterTurbo/commit/fc7f44d1ce24dd34c83f3b79aa74b5579e20c071) | HEOJUNFO |
| 2026-11-23 | [perf(video): fill the opaque composite background one row at a time](https://github.com/harry0703/MoneyPrinterTurbo/commit/1d7ec49adf62cf743f2aff35fe1188ae858a93eb) | b84330808 |
| 2026-11-23 | [Rename UberLLM to MartLLM](https://github.com/harry0703/MoneyPrinterTurbo/commit/d021ad119872ebaa718489b6cd261cdf2d318040) | al-global-tech |
| 2026-11-23 | [perf(project): verify cached render artifacts once](https://github.com/harry0703/MoneyPrinterTurbo/commit/96496d5642ce3c6b080d728d2c91e32f78faad5c) | nemo-crypto |
| 2026-11-23 | [fix(project): preserve display aspect ratio when cropping scenes](https://github.com/harry0703/MoneyPrinterTurbo/commit/0a18e462fba44d11f8af15e2017ba53066ef1168) | nemo-crypto |

[See all commits ↗](https://github.com/harry0703/MoneyPrinterTurbo/commits)

## ⬇️ Get it

```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```
