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
| ⭐ **Stars** | 144.9k |
| 🍴 **Forks** | 23.3k |
| 🐞 **Open issues + PRs** | [93](https://github.com/harry0703/MoneyPrinterTurbo/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `tiktok` `ai-video-generator` `content-creation` `ffmpeg` `instagram-reels` `llm` `short-video` `subtitles` `text-to-speech` `video-automation` `video-workflow` `workflow-automation` `youtube-shorts` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2024-03-11 |
| 📦 **Latest release** | [v1.3.10](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.10) — 2026-11-07 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 529.1 MB |

## 📦 Recent releases

### [v1.3.10](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.10)
<sub>2026-11-07 · 14d ago</sub>

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

### [v1.3.6](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.3.6)
<sub>2026-09-02 · 2mo ago</sub>

> [English](#en-v1.3.6) | [中文](#cn-v1.3.6)
> <h2 id="en-v1.3.6">Highlights</h2>
> - Added native Volcano Engine Ark Seedance video generation for generating source clips directly from script segments.
> - Added OFox multi-model text-to-video support, allowing Seedance, Wan, and other models to share one API key.
> - Added Metaso MiniMax H3 text-to-video support with `768P`/`2K` output, 4–15 second clips, and `9:16`, `16:9`, and `1:1` aspect ratios.
> - Added an OpenAI-compatible text-to-image material source for cloud relays and local gateways.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(audio): validate decoded packets (#1823)](https://github.com/harry0703/MoneyPrinterTurbo/commit/92f6258714010dfea6fc28cc37a0bbb4558096a5) | AyhamJo7 |
| 2026-11-20 | [perf(video): draw each composite layer only where it covers the frame](https://github.com/harry0703/MoneyPrinterTurbo/commit/ef3c333fd475595176fc90b67c78555bf4b739a2) | b84330808 |
| 2026-11-20 | [fix(i18n): translate remaining Spanish WebUI strings and unify termin…](https://github.com/harry0703/MoneyPrinterTurbo/commit/20a09b84af20e3135d15b1bb32b90b3ed3841ea3) | PedroFlores199 |
| 2026-11-20 | [fix(tts): migrate Gemini speech to Flash-Lite 3.8](https://github.com/harry0703/MoneyPrinterTurbo/commit/5309263739f0776e94ab5ccef26a5e30a65c2b1c) | JunaidAhamed-7777 |
| 2026-11-20 | [chore: update project resources](https://github.com/harry0703/MoneyPrinterTurbo/commit/aebf92bfa2e8346182a188773d377e8e4f426a44) | harry0703 |
| 2026-11-19 | [Expose rendered scene clips in video project results](https://github.com/harry0703/MoneyPrinterTurbo/commit/bdd8d328cc366fe70d9fa67ffd0443ba34b4a3e1) | meowtivator |
| 2026-11-19 | [feat(material): add Aigei stock video provider](https://github.com/harry0703/MoneyPrinterTurbo/commit/d4877bc5d481868fc38da357d446407bf5c7e229) | harry0703 |
| 2026-11-16 | [Fix typo in Edge TTS cue test fixture ('stil' -> 'still')](https://github.com/harry0703/MoneyPrinterTurbo/commit/92e0f9a55b91e353565015aab74b7c50cc28f148) | Dani-Google |
| 2026-11-16 | [fix(loomloom): trace the video artifact download request](https://github.com/harry0703/MoneyPrinterTurbo/commit/8dc9b41eb72aa5fbe835c4bac51f071dc6c0fe30) | RerankerGuo |
| 2026-11-16 | [test(material): cover malformed Pixabay files in the rendition size sort](https://github.com/harry0703/MoneyPrinterTurbo/commit/49b900780c2463573a7968e9217e86fbea990023) | rohanb123 |

[See all commits ↗](https://github.com/harry0703/MoneyPrinterTurbo/commits)

## ⬇️ Get it

```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```
