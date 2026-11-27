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
| ⭐ **Stars** | 61.4k |
| 🍴 **Forks** | 7.8k |
| 🐞 **Open issues + PRs** | [514](https://github.com/jamiepine/voicebox/issues) |
| 💻 **Languages** | Python 48% · TypeScript 41% · Rust 9% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `voice-clone` `qwen3-tts` `voice-ai` `whisper` `qwen3-tts-ui` `cuda` `mlx` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-01-25 |
| 📦 **Latest release** | [v0.6.1](https://github.com/jamiepine/voicebox/releases/tag/v0.6.1) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 101.1 MB |
| 🌐 **Website** | https://voicebox.sh |

## 📦 Recent releases

### [v0.6.1](https://github.com/jamiepine/voicebox/releases/tag/v0.6.1) — voicebox v0.6.1
<sub>2026-11-27 · today</sub>

> A security and bug-fix release on top of 0.6.0. It raises the PyTorch floor for CVE-2026-24747, narrows the desktop app's shell and filesystem permissions, and fixes partial model downloads, a Windows CUDA DLL load failure in Chatterbox Turbo, and the dead end after denying microphone access.
> **Fixes**
> - **PyTorch 2.10 is now the minimum, closing CVE-2026-24747.** Before 2.10, a crafted checkpoint could run code during `torch.load` even with `weights_only=True`. `torch` and `torchaudio` now require 2.10 or newer on every platform with 2.10 wheels, and the Docker ROCm image and `just setup` on Linux AMD hosts now default to the PyTorch ROCm 7.2 wheels, because the ROCm 6.x indexes stop at 2.9.1 (set `ROCM_VERSION` / `VOICEBOX_ROCM_VERSION` to override). Two platforms cannot reach 2.10 yet and stay on their current torch: **Intel macOS** stays on 2.2.2, the last x86_64 macOS wheel PyTorch published, and **Windows ROCm** stays on AMD's 2.9.1+rocm7.2.1, the newest stable Windows ROCm wheel. On those two platforms, only load models from sources you trust. ([CVE-2026-24747](https://nvd.nist.gov/vuln/detail/CVE-2026-24747))
> - **The desktop app's shell and filesystem permissions are narrowed to what it uses.** The webview's shell `open` scope accepts only `http(s)://` and `mailto:` URLs instead of any string, the shell `execute`/`spawn` and blanket `fs` read/write grants are gone (exports write only to the file picked in the save dialog), and the capability no longer extends IPC to any page served from `http://localhost:*`. The Open folder buttons for generations, captures and models now call a new `reveal_app_folder` command that resolves the folder in Rust and checks it stays inside the app data directory or the configured models directory, instead of opening whatever path the server returned. (security hardening)
> - **A model is shown as downloaded only once every file it needs is on disk.** Voicebox writes an in-progress marker into the model's HuggingFace cache before a download starts and, once the model loads successfully from any path (generation, transcription and dictation, refinement and personalities, MCP, or the Models page), records the snapshot's file list in its place; `/models/status` and every engine's cache check now require all recorded files, and a marked model never runs in forced-offline mode. Previously any weights file was enough, so a download that failed after `model.safetensors` left the model marked *Downloaded* and every load failed with a misleading "couldn't connect to huggingface.co" error. Clicking Download again on such a model now fetches the missing files instead of being skipped, reloading it from disk if it is already in memory. Models downloaded by earlier versions keep working and get recorded on their next successful load. ([#1261](https://github.com/jamiepine/voicebox/issues/1261))
> - **Chatterbox Turbo loads on the Windows CUDA backend without a prior sample upload.** The frozen build now bundles the `onnx.libs` folder from onnx's Windows wheel through a new `pyi_hooks/hook-onnx.py`, so `onnx_cpp2py_export.pyd` finds its `msvcp140-<hash>.dll` via onnx's own `os.add_dll_directory` call instead of failing with "DLL load failed" unless pandas had already loaded an identical copy. ([#1264](https://github.com/jamiepine/voicebox/issues/1264))
> …

### [v0.6.0](https://github.com/jamiepine/voicebox/releases/tag/v0.6.0)
<sub>2026-11-21 · 6d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [ci(release): install --no-deps engines from backend/requirements-node…](https://github.com/jamiepine/voicebox/commit/a24f8ad99e024c6668bd74a536d5f5a97ed301a0) | jamiepine |
| 2026-11-27 | [Bump version: 0.6.0 → 0.7.0](https://github.com/jamiepine/voicebox/commit/fff3df3281447550c5a0e7f89b6c5b8491b390a1) | jamiepine |
| 2026-11-27 | [docs(changelog): draft the 0.7.0 release narrative](https://github.com/jamiepine/voicebox/commit/ed03198fdd9fdae7088f6860319f9b9be5acf2e0) | jamiepine |
| 2026-11-27 | [fix(profiles): close the sample temp file before deleting a rejected …](https://github.com/jamiepine/voicebox/commit/2e84d47e413559b7e652ac8bd1d3c0d3bded2a39) | jamiepine |
| 2026-11-27 | [fix(profiles): edit a designed voice's description in the profile form](https://github.com/jamiepine/voicebox/commit/fe1d078ddb5ed1553c34226c902150d0560d0892) | jamiepine |
| 2026-11-27 | [docs(changelog): attribute the designed-profile description fix](https://github.com/jamiepine/voicebox/commit/014be33ffe4aa37e515ee557cf388e1285f22e7a) | jamiepine |
| 2026-11-27 | [Fix: persist edits to designed voice descriptions](https://github.com/jamiepine/voicebox/commit/073c62545e756b8c32e7ba543f92f3320357c4e4) | zhangkom |
| 2026-11-27 | [docs(changelog): note the MCP shim UTF-8 fix](https://github.com/jamiepine/voicebox/commit/40b11e1a4c70d223b4ab2c341036fde39887ea9c) | jamiepine |
| 2026-11-27 | [fix(mcp): only reconfigure stdio streams that are text wrappers](https://github.com/jamiepine/voicebox/commit/197419e17f1f9d945705a8397f8ed1850598ce52) | jamiepine |
| 2026-11-27 | [fix(mcp): preserve UTF-8 on Windows stdio](https://github.com/jamiepine/voicebox/commit/52c9c59bd4ff8ccc8fbd673ebcb33f9fd8668e8a) | Ha1baraA11 |

[See all commits ↗](https://github.com/jamiepine/voicebox/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jamiepine/voicebox.git
```
