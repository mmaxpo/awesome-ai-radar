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
| ⭐ **Stars** | 97.4k |
| 🍴 **Forks** | 25.2k |
| 🐞 **Open issues + PRs** | [11.0k](https://github.com/vllm-project/vllm/issues) |
| 💻 **Languages** | Python 86% · Rust 7% · Cuda 4% · C++ 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `gpt` `llm` `pytorch` `model-serving` `transformer` `llm-serving` `inference` `llama` `amd` `cuda` `tpu` `deepseek` `qwen` `blackwell` `deepseek-v3` `gpt-oss` `kimi` `moe` `openai` `qwen3` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-02-09 |
| 📦 **Latest release** | [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 380.5 MB |
| 🌐 **Website** | https://vllm.ai |

## 📦 Recent releases

### [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)
<sub>2026-11-16 · 6d ago</sub>

> **v0.34.0**
> **1,061 commits from 412 contributors (120 new).** Thank you!
> **TL;DR**
> - **10 new models** (Mistral Large 4, MiniMax-M3.1-Flash, Nemotron-3.5-Transcribe, and more!)
> - **Extensible KV cache is on by default:** vLLM sizes the KV cache from memory actually free after warmup, so most models get a bigger cache and more throughput - in most cases you should now **remove `gpu_memory_utilization`** from your configs.
> - **Model Runner V1 is gone.** Model Runner V2 is now the only GPU runner.
> …

### [v0.33.0rc3](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) — v0.33.0
<sub>2026-11-02 · 21d ago</sub>

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
| 2026-11-23 | [[ROCm][Perf] Skip masked-out context tiles for sliding-window models …](https://github.com/vllm-project/vllm/commit/e83d82a46b50a27534584a8bf4c6dd2d2cb9eeb5) | phambinhfin |
| 2026-11-23 | [[Refactor][SleepMode] Expose CuMemBackend allocator hook (#69412)](https://github.com/vllm-project/vllm/commit/187c473dbe8aa2b3fc4213d5b79a70c588902ba5) | Ronald1995 |
| 2026-11-23 | [[Bugfix][KVConnector] Split MLA kernel rows larger than the NIXL bloc…](https://github.com/vllm-project/vllm/commit/75d8770263d6907de1f28a7fdaf485e20a039d6d) | NickLucche |
| 2026-11-23 | [[Bugfix][Model] Normalize the legacy Qwen3-ASR text config alias (#69…](https://github.com/vllm-project/vllm/commit/6aeedab553dd85d6bc3f9f4deb3bb264bce0cb7c) | pk954061458 |
| 2026-11-23 | [[Bugfix][Quantization] Keep checkpoint-excluded routed experts unquan…](https://github.com/vllm-project/vllm/commit/abad4cc48213a20bdc335379520fc66b26e6181d) | vllmellm |
| 2026-11-23 | [[Core][Model Loader] Add sleep/wake/reload lifecycle hooks to model l…](https://github.com/vllm-project/vllm/commit/afb35f85e7e25720a9acb656d0b20b20d33ffcd0) | romanbaron |
| 2026-11-23 | [[CI] Use test runner for sampling and LoRA tests (#68884)](https://github.com/vllm-project/vllm/commit/ee1d07c7b2c30dc0eb686bdb00a8ce94f4e4c071) | hlin99 |
| 2026-11-23 | [[Model] Migrate ERNIE 4.5 to Transformers backend (#69087)](https://github.com/vllm-project/vllm/commit/d9bfe86b9fe1156642ac45aadef965159dd1d7f1) | Remarkable911 |
| 2026-11-23 | [[Bugfix] Respect root_path in elastic EP scaling middleware (#69285)](https://github.com/vllm-project/vllm/commit/4a1620a09aba0cd771a186b81e973707c0ecbb07) | rishabhsai |
| 2026-11-23 | [[CI][Bugfix] Precompute Gemma3n sparsity quantiles before inference (…](https://github.com/vllm-project/vllm/commit/ab94934e6ca2db6e41e9e6d8eeefb740488ed0ee) | hlin99 |

[See all commits ↗](https://github.com/vllm-project/vllm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vllm-project/vllm.git
```
