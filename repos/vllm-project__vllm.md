# vllm-project/vllm

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/vllm-project/vllm)

> A high-throughput and memory-efficient inference and serving engine for LLMs

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | TCOS |
| **Why it's worth a look** | High-throughput LLM serving engine |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 97.3k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [10.9k](https://github.com/vllm-project/vllm/issues) |
| 💻 **Languages** | Python 86% · Rust 7% · Cuda 4% · C++ 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `gpt` `llm` `pytorch` `model-serving` `transformer` `llm-serving` `inference` `llama` `amd` `cuda` `tpu` `deepseek` `qwen` `blackwell` `deepseek-v3` `gpt-oss` `kimi` `moe` `openai` `qwen3` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-02-09 |
| 📦 **Latest release** | [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 378.6 MB |
| 🌐 **Website** | https://vllm.ai |

## 📦 Recent releases

### [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)
<sub>2026-11-16 · 5d ago</sub>

> **v0.34.0**
> **1,061 commits from 412 contributors (120 new).** Thank you!
> **TL;DR**
> - **10 new models** (Mistral Large 4, MiniMax-M3.1-Flash, Nemotron-3.5-Transcribe, and more!)
> - **Extensible KV cache is on by default:** vLLM sizes the KV cache from memory actually free after warmup, so most models get a bigger cache and more throughput - in most cases you should now **remove `gpu_memory_utilization`** from your configs.
> - **Model Runner V1 is gone.** Model Runner V2 is now the only GPU runner.
> …

### [v0.33.0rc3](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) — v0.33.0
<sub>2026-11-02 · 20d ago</sub>

> **v0.33.0**
> **Highlights**
> This release features 927 commits from 389 contributors (122 new)!
> * **New models**: Reflection Beam-1.0 (501B MoE, 23B active) with its DFlash2 drafter (#62074), Yandex AliceAI-Foundation-80B-A3B (#57963), Recursive Flint (40B MoE, 2.5B active) (#62938), Muse Spark Open (#61879), Step-5 Preview (#61727, #63147), NVIDIA Alpamayo 2 Super (#62957), Nemotron-Labs Dory1.0-4B (#60149), Nemotron Parse 3.5 (#61651), MiniCPM-OCR 1.0 (#63095), Domyn Edge (#62544) and the ColUltraVBERT visual document retriever (#62237).
> * **PyTorch 2.14**: vLLM is upgraded to PyTorch 2.14.0, with torchvision 0.29.0 and Triton 3.8.0 (#52183).
> * **CUDA 12.9 dropped**: release wheels and images are CUDA 13.0 only. The CUDA 12.9 wheels and the `-cu129` / `-cu129-ubuntu2404` images are no longer published (#62575); use the default CUDA 13.0 artifacts instead.
> …

### [v0.32.0](https://github.com/vllm-project/vllm/releases/tag/v0.32.0)
<sub>2026-10-18 · 1mo ago</sub>

> **v0.32.0**
> **Highlights**
> This release features 814 commits from 363 contributors (121 new)!
> * **Structured decisions and generic parsers**: the new `POST /v1/systemone` endpoint answers `choice`, `noul` and `score` questions over a structured state (#59299), is served by default (#60677, #60696), and also runs on `Cloudflare/clef-omni` (#61064), `LiquidAI/d1-3B` (#60676) and DiffusionGemma (#60466). The new `hf` tool and reasoning parser (`--tool-call-parser hf`, `--reasoning-parser hf`) reads the checkpoint's `response_template`, so models that ship it need no model-specific parser (#58604, #58602), in both the Python and Rust frontends (#59005).
> * **Low-precision KV cache everywhere**: NVFP4 KV cache now runs on SM8x and SM12x (#46963), SM90 (#60620) and with XQA decode on SM12x (#60452), and on MiniMax-M3 sparse attention on SM100 (#59300); GLM-5.x defaults to an FP8 KV cache on SM100, halving KV memory per rank with 2.3-5.5% more throughput at a 7-11% TTFT cost in the PR's benchmark (#60140, #60281); `fp8_ds_mla` on SM90 gives GLM-5.3-Flash up to 31% more output throughput (#59246); ROCm gains the 4-bit `ultraquant_4bit` KV cache with about 2x the density of FP8 (#57057).
> * **Model Runner V2**: a GPU n-gram speculator with variable-length drafts (#40704), Elastic EP (#53934), pipeline parallelism with prefill context parallelism for MLA models (#59139), a stock torch.compile mode (#59079), and MRV2 is now the default on ROCm with the model-specific MRV1 exceptions removed (#56360).
> …

### [v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0)
<sub>2026-10-05 · 1mo ago</sub>

> **v0.31.0**
> **Highlights**
> This release features 717 commits from 307 contributors (96 new)!
> * **DeepSeek-V4.1-Flash performance**: FlashMLA mega attention with the V4.1 NVFP4 compressed KV cache is now the SM100 default (#56935); DeepGEMM sparse MQA logits for the indexer (#56254) and Mega-Gate fusing the gate GEMM with expert selection (#56266); decoder boundaries fuse the TP all-reduce, mHC input preparation (#57643) and the MoE finalize (#58586); a fused small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103 (#58634); the MXFP8 `wo_b` GEMM fused with the sequence-parallel reduce-scatter (#57428); Engram `wkv` sharded across TP ranks (#58678) and Engram host tables shared across co-located DP replicas by default (#57651); encoder CUDA graphs for the vision tower (#56625); and SWA bounded replay that keeps the sliding-window KV out of prefix caching (#56227).
> * **Fast restart**: the new `vllm preload` CLI launches the weight-cache daemon that keeps post-quantized weights resident in GPU memory across engine restarts (#56680), now with data parallelism (#57386), MTP draft models (#57312), a `/health` endpoint (#58552) and a readiness wait (#58370). Experimental initialized-engine snapshots (`vllm snapshot create/restore`) use CRIU to restore a fully initialized TP1 engine (#51360).
> * **Model Runner V2 and speculative decoding**: draft-model speculative decoding (#43091) and custom logits processors (#56497) on Model Runner V2; the new LiLiCorr drafter (#57934); async scheduling for DFlash (#58065) with the context K/V precompute captured in the draft CUDA graph (#57632); DSpark adaptive verification for Gemma4 (#57263) and variable-length decode for Kimi-K3 (#52988); a DCP target with a non-DCP DSpark draft (#56723); and MoE memory now counted during MRV2 profiling, avoiding OOMs on WideEP deployments (#57270, #58411).
> …

### [v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0)
<sub>2026-09-22 · 2mo ago</sub>

> **v0.30.0**
> **Highlights**
> This release features 762 commits from 315 contributors (104 new)!
> * **New models**: DeepSeek-V4.1-Flash (#56214, #56228, #56208) with the whole KV stored in MXFP8 through the FlashMLA V4.1 record on SM100 (#56893), DeepGEMM Mega-mHC (#56962), and async Engram prefetch with Engram DP sharding (#56512); DeepSeek-V4-Flash-Vision-Exp (#54566), also on ROCm (#55107) and with LoRA (#55897); GLM-5.3-Flash (#53906) with EPLB (#55119); K2-Horizon (#55063); Cohere Compass (#54774); Bailing V3 VL (#55921); Nanbeige4.2 via the Transformers backend (#56071); and a DeepSeek-V4 CPU backend with AVX512/AMX sparse MLA, indexer, mHC and compressor kernels (#55355).
> * **Fast Start**: a persistent per-GPU weight-cache daemon holds post-quantized, TP-sharded weights in GPU memory so restarting engines map them over CUDA IPC with `--load-format ipc_cache` instead of reloading from disk (#54921), now covering FP4 checkpoints (#55465) and multi-node TP (#55468).
> * **Watermarking**: Gumbel-max watermarked generation and detection with a keyed PRF, per-request opt-out and an example detection endpoint (#54053); dual-key Gumbel-max makes it compatible with speculative decoding (#56122); the Rust frontend forwards the per-request controls (#56338).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [[Bugfix] Apply the video processor frame caps when loading videos (#6…](https://github.com/vllm-project/vllm/commit/b976fff86af82c559b19aa676f52ea193eb0c188) | paulpak58 |
| 2026-11-22 | [[Perf][KV Offload] Avoid waking idle FS workers on job completion (#6…](https://github.com/vllm-project/vllm/commit/17323e0b1ca54296cc3016b72d481ecffc17e69b) | waizuichougou |
| 2026-11-22 | [[Bugfix][KV Offload] Preserve reused ARC prefixes during running-requ…](https://github.com/vllm-project/vllm/commit/e29c741da8d11e2ae7ba381bb78b6f703812cae1) | waizuichougou |
| 2026-11-22 | [[Rust Frontend] Support allowed_tools tool_choice (#68408)](https://github.com/vllm-project/vllm/commit/443b51e52fad36bbbd7960fd272c8baf23f14dbb) | BugenZhao |
| 2026-11-22 | [[KV Offload] Add access_mode (read/write/readwrite) (#67961)](https://github.com/vllm-project/vllm/commit/9ae9c15c569176e52783dd2ef8f4fedf8aadc70a) | effi-ofer |
| 2026-11-22 | [[Bugfix][Multimodal] Pass image kwargs through the OpenCUA processor …](https://github.com/vllm-project/vllm/commit/cb19fedd85f55e4c09ce76ab95b3a70fe4b5872a) | subhashpolisetti |
| 2026-11-22 | [[Frontend] Classify errors in offline LLM APIs (#68667)](https://github.com/vllm-project/vllm/commit/d4cc8ec42efa7e1b41dfc5462d189004d5c5cb19) | Remarkable911 |
| 2026-11-22 | [[Bugfix][KV Offload] Store the chunks that fit when a request exceeds…](https://github.com/vllm-project/vllm/commit/e72fc9ae50c221180c4b8f4a94c5009714a4b199) | lnvitesace |
| 2026-11-22 | [[Bugfix][Multimodal] Accept torch.Tensor videos in vLLM's own HF proc…](https://github.com/vllm-project/vllm/commit/647a76866b4559a74e27d1c6b55fbffe85c07ce4) | yarikama |
| 2026-11-22 | [[Bugfix][Multimodal] Accept NumPy images and PIL frame videos in Muse…](https://github.com/vllm-project/vllm/commit/cb85c4e9efc27be9644bb90d8eed5fb521a77f44) | yarikama |

[See all commits ↗](https://github.com/vllm-project/vllm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vllm-project/vllm.git
```
