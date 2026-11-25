# jamiepine/voicebox

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/jamiepine/voicebox)

> The open-source AI voice studio. Clone, dictate, create.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖼 Image & video generation |
| **Project** | Klipova |
| **Why it's worth a look** | Open-source AI voice studio: clone, dictate, create |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 61.3k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [564](https://github.com/jamiepine/voicebox/issues) |
| 💻 **Languages** | Python 46% · TypeScript 42% · Rust 9% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `voice-clone` `qwen3-tts` `voice-ai` `whisper` `qwen3-tts-ui` `cuda` `mlx` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-01-25 |
| 📦 **Latest release** | [v0.6.0](https://github.com/jamiepine/voicebox/releases/tag/v0.6.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 100.5 MB |
| 🌐 **Website** | https://voicebox.sh |

## 📦 Recent releases

### [v0.6.0](https://github.com/jamiepine/voicebox/releases/tag/v0.6.0)
<sub>2026-11-21 · 4d ago</sub>

> **The stability release.** 0.5 made Voicebox a dictation and agent-voice studio; 0.6 makes it hold up. Sixty-plus contributor pull requests landed since 0.5 and most of them fix something that used to go wrong in daily use: MLX crashed with `There is no Stream(gpu, 1) in current thread` when a model was loaded on one thread and used on another, memory grew with every generation and never came back on unload, a fully-cached model retried HuggingFace five times per file before it would load offline, the Docker image could not write its own data volume, dictation refused to arm without an LLM it was never going to call, and the backend test suite would not even collect. All of that is fixed. The headline features ride on top: native AMD ROCm on Windows and in Docker, five new interface languages, and Chatterbox multilingual running on Apple Silicon through MLX.
> One change is breaking for existing MCP configs: the four MCP tools are renamed from dotted to underscore names (`voicebox.speak` → `voicebox_speak`, and so on) because Claude Desktop rejects dots in tool names. See the MCP section below.
> **Stability and reliability**
> - **Every MLX op runs on one worker thread.** MLX's Metal stream registry is thread-local and `asyncio.to_thread` hands successive calls to different pool threads, so loading a model on one thread and generating on another raised `There is no Stream(gpu, 1) in current thread` and killed the request. All MLX load, generate, transcribe and Qwen3 LLM calls (TTS, STT, personality compose and rewrite, dictation refinement) now go through a single-worker executor, reload and inference are folded into one submission so an unload cannot land between them, and `unload_model()` stays off the worker so `/models/unload` cannot stall the event loop behind an in-flight generation. Reproduced and verified on an M2 Ultra; a regression test locks the single-thread guarantee without needing `mlx` installed. — @Rdbi-The-Ai, @shsunmoonlee, @davidstrouk ([#1154](https://github.com/jamiepine/voicebox/pull/1154), from [#989](https://github.com/jamiepine/voicebox/pull/989), [#909](https://github.com/jamiepine/voicebox/pull/909), [#789](https://github.com/jamiepine/voicebox/pull/789); fixes [#699](https://github.com/jamiepine/voicebox/issues/699))
> - **MLX models release their memory on unload.** Unloading an MLX model dropped the Python reference but left the Metal allocator holding the weights, so switching models on Apple Silicon only ever grew. Unload now clears the prompt cache and the allocator, and a failing op's traceback can no longer pin the model binding alive. — @byevanli ([#1161](https://github.com/jamiepine/voicebox/pull/1161), from [#1074](https://github.com/jamiepine/voicebox/pull/1074))
> - **No more memory growth across generations.** Consecutive TTS generations accumulated tensors and cache that were never freed. Post-generation cleanup now runs after every generation, including `/generate/stream`, and is best-effort so a cleanup failure cannot fail the request that just succeeded. — @devangkantharia ([#1149](https://github.com/jamiepine/voicebox/pull/1149), from [#1032](https://github.com/jamiepine/voicebox/pull/1032); fixes [#923](https://github.com/jamiepine/voicebox/issues/923))
> …

### [v0.5.0](https://github.com/jamiepine/voicebox/releases/tag/v0.5.0)
<sub>2026-04-25 · 7mo ago</sub>

> **The Capture release.**
> Voicebox stops being just a voice-cloning studio and becomes a full AI voice studio. Hold a key anywhere on your machine, speak, release — the transcript lands in the focused text field. Flip the primitive around and any MCP-aware agent — Claude Code, Cursor, Spacebot — speaks back through an on-screen pill in one of your cloned voices. A local LLM sits between the two, so transcripts come out clean and voice profiles can carry a personality that reshapes what the agent says before it gets spoken.
> <img width="1354" height="990" alt="Screenshot 2026-04-22 at 2 37 10 PM" src="https://github.com/user-attachments/assets/853c730f-64f3-4573-bcd8-1000bdb8e11f" />
> **Dictation — speak anywhere, paste anywhere**
> - **Global hotkey capture.** Hold a customizable chord anywhere on your machine (defaults: right-Cmd + right-Option on macOS, right-Ctrl + right-Shift on Windows), speak, release. A floating on-screen pill walks through recording → transcribing → refining → done with a live elapsed timer. The transcript lands as clean text.
> - **Push-to-talk and toggle modes, each with its own chord.** The default toggle chord adds Space to the push-to-talk chord. Holding PTT and tapping Space mid-hold upgrades a hold into a hands-free session without a gap in the recording.
> …

### [v0.4.5](https://github.com/jamiepine/voicebox/releases/tag/v0.4.5)
<sub>2026-04-22 · 7mo ago</sub>

> Second hotfix for the "offline mode is enabled" crash on model load. 0.4.4 reverted the inference-path offline guards but kept the same trap on the load path, so users who updated to 0.4.4 kept hitting the exact error the release was supposed to fix ([#526](https://github.com/jamiepine/voicebox/issues/526)). This release removes the load-path guards and patches the transformers tokenizer load to be robust to HuggingFace metadata failures at the source, so the class of bug can't recur.
> **Reliability**
> - **Load no longer fails with "offline mode is enabled"** ([#530](https://github.com/jamiepine/voicebox/pull/530), fixes [#526](https://github.com/jamiepine/voicebox/issues/526)). transformers 4.57.x added an unconditional `huggingface_hub.model_info()` call inside `AutoTokenizer.from_pretrained` (via `_patch_mistral_regex`) that runs for every non-local repo load, regardless of cache state or whether the target model is actually a Mistral variant. The load-time `HF_HUB_OFFLINE` guard from 0.4.2 turned that into a hard crash for cached online users the moment 0.4.4 removed the inference-path guard that had been masking the problem. Fix wraps `_patch_mistral_regex` so any exception from the HF metadata check is caught and the tokenizer is returned unchanged — matching the success-path behavior for non-Mistral repos. The wrapper installs at `backend.backends` import time so it covers Qwen Base, Qwen CustomVoice, TADA, and every other transformers-backed engine on Windows, Linux, and CUDA alike. The load-time `force_offline_if_cached` guards were removed — with the wrapper in place they provide zero value and only risk re-introducing the same failure mode.
> - **No more 30s pause when generating without a network.** The HuggingFace metadata timeout called out as a known caveat in 0.4.4 is covered by the same patch; offline users no longer wait for the check to time out before load completes.

### [v0.4.4](https://github.com/jamiepine/voicebox/releases/tag/v0.4.4)
<sub>2026-04-21 · 7mo ago</sub>

> Hotfix for a regression in 0.4.3 where generation and transcription could fail outright with "offline mode is enabled" even when the user was online.
> **Reliability**
> - **Inference no longer fails with "offline mode is enabled" while online** ([#524](https://github.com/jamiepine/voicebox/pull/524), reverts the inference-path guards from [#503](https://github.com/jamiepine/voicebox/pull/503)). 0.4.3 wrapped every inference body (`generate`, `transcribe`, `create_voice_clone_prompt`) with a process-wide `HF_HUB_OFFLINE` flip to stop lazy HuggingFace lookups from hanging when the network drops mid-inference ([#462](https://github.com/jamiepine/voicebox/issues/462)). That flag also blocks legitimate metadata calls (e.g. `HfApi().model_info` for revision resolution) so online users started seeing generation fail outright. Inference now runs with the process's default HF state. Load-time offline guards — which weren't the source of the regression — stay in place.
> **Known caveat**: users generating without an internet connection may see brief pauses during inference while HuggingFace metadata lookups time out (typically ~30s, after which the library recovers). A proper offline-mode toggle is planned for 0.4.5.

### [v0.4.3](https://github.com/jamiepine/voicebox/releases/tag/v0.4.3) — voicebox v0.4.3
<sub>2026-04-21 · 7mo ago</sub>

> A patch focused on two user-impacting reliability fixes: macOS DMG notarization (unblocks `brew install voicebox` on macOS 15 Sequoia and fixes spurious "app isn't signed" Gatekeeper dialogs on older Intel Macs) and Kokoro Japanese voice initialization on fresh installs.
> **macOS**
> - **DMGs are now notarized and stapled** ([#523](https://github.com/jamiepine/voicebox/pull/523)). Tauri's bundler notarizes the `.app` inside the DMG but ships the DMG wrapper itself unnotarized. Gatekeeper rejects that on macOS 15 Sequoia (confirmed by Homebrew Cask CI failing on both arm and intel Sequoia runners) and causes the "the app is not signed" dialog on older Intel Macs when Apple's notarization servers are slow or unreachable ([#509](https://github.com/jamiepine/voicebox/issues/509)). The release workflow now submits each DMG to `notarytool`, staples the ticket, verifies with `spctl`, and overwrites the draft-release asset `tauri-action` uploaded. Adds ~5-10 min per macOS job.
> **Backend**
> - **Kokoro Japanese voices no longer crash on fresh installs** ([#521](https://github.com/jamiepine/voicebox/pull/521), fixes [#514](https://github.com/jamiepine/voicebox/issues/514)). `misaki[ja]` pulls in `fugashi`, which needs a MeCab dictionary on disk. The `unidic` package that was being installed ships no data and expects a ~526MB runtime download that `just setup` doesn't run (and which wouldn't survive PyInstaller anyway). Swapped to `unidic-lite`, which bundles a MeCab-compatible dict inside the wheel (~50MB). Collected in `build_binary.py` so frozen builds pick up `unidic_lite/dicdir/`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Track every model load so a successful load always clears the downloa…](https://github.com/jamiepine/voicebox/commit/8dc2a5bfe0f783edd53f8a346a22dcad9c1fb793) | jamiepine |
| 2026-11-24 | [Only prefer the repo data root when the app did not spawn the backend](https://github.com/jamiepine/voicebox/commit/6898ccb89b5ccf1b38e7a4606595850985c5fa55) | jamiepine |
| 2026-11-24 | [Resolve app folders against the dev backend's data root in debug builds](https://github.com/jamiepine/voicebox/commit/1c5243b50b772f2a44723bc634277d024488afca) | jamiepine |
| 2026-11-24 | [Narrow Tauri shell and fs permissions and open app folders from Rust](https://github.com/jamiepine/voicebox/commit/8abf8255c891a59c62be3b2d48d2b06c369e6147) | jamiepine |
| 2026-11-24 | [Make TADA residency size-aware and retry only clean OSError load fail…](https://github.com/jamiepine/voicebox/commit/b227910978ee2aaf6926b13ac4b7870db9b9b962) | jamiepine |
| 2026-11-24 | [Skip snapshot verification for a model that is already resident](https://github.com/jamiepine/voicebox/commit/8ce92fdb1ee3b25967951e3ee0b2a845bed496cd) | jamiepine |
| 2026-11-24 | [Retry an unverified model load online once before failing (#1261)](https://github.com/jamiepine/voicebox/commit/8b845f77533534e5ba2fb18909c79846f485f794) | jamiepine |
| 2026-11-24 | [Only report a model as downloaded once its snapshot is verified compl…](https://github.com/jamiepine/voicebox/commit/8815b9be08a184501a5c0cd5e428dd51b46d4721) | jamiepine |
| 2026-11-24 | [Bring the recovery dialog forward, or open OS settings when the main …](https://github.com/jamiepine/voicebox/commit/b5835f9d795cae615518c96a2a2f5065a195db10) | jamiepine |
| 2026-11-24 | [Recover from a denied microphone permission (#1267)](https://github.com/jamiepine/voicebox/commit/6d3b024e2884e3794b738296ffd29d9542f3abc1) | jamiepine |

[See all commits ↗](https://github.com/jamiepine/voicebox/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jamiepine/voicebox.git
```
