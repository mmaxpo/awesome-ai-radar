# FareedKhan-dev/kimi-k3-in-c

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/FareedKhan-dev/kimi-k3-in-c)

> A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Kimi K3 inference on a single CPU, written in C |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 12.5k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [6](https://github.com/FareedKhan-dev/kimi-k3-in-c/issues) |
| 💻 **Languages** | C 69% · Python 23% · Shell 4% · Makefile 3% · CMake 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `avx2` `c99` `cpu-inference` `deep-learning` `from-scratch` `inference-engine` `kimi-k3` `linear-attention` `llm` `llm-inference` `machine-learning` `memory-efficient` `mixture-of-experts` `moe` `mxfp4` `quantization` `simd` `systems-programming` `transformer` `zero-dependencies` |
| 🕒 **Last activity** | 2026-11-16 (5d ago) |
| 📅 **Created** | 2026-08-01 |
| 📦 **Latest release** | [v2.0.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v2.0.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 31.4 MB |
| 🌐 **Website** | https://medium.com/@fareedkhandev/building-kimi-k3-in-c-to-run-a-2-8t-model-on-consumer-hardware-a5792cbf3b59 |

## 📦 Recent releases

### [v2.0.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v2.0.0)
<sub>2026-11-15 · 5d ago</sub>

> Long prompts stop being a one-core job, and a large round of fixes, most of them from outside contributors, makes everything that loads, parses, measures or certifies refuse a wrong input instead of quietly using it. Output is unchanged wherever it was already defined: every oracle gate still matches the PyTorch reference exactly, at any thread count.
> **Compatibility notes, which are why this is 2.0.0:**
> - `--save-state` files are now version 3, with the header inside the checksum. A version 2 file is refused rather than read; regenerate it with `--gen 0 --incremental --save-state`.
> - MLA scratch grew: the score term of `k3_mla_scratch_cached()` is now H*T floats. Code that sizes scratch through the helpers is unaffected. `K3Cache` gained fields, so rebuild anything that embeds it.
> - Chat sampling with both `--top-k` and `--top-p` measures the nucleus after top-k, as the Hugging Face and vLLM samplers do, so a fixed-seed run using both flags samples differently.
> - Malformed numeric flags (`--gen 1junk`, an empty `--seed`, `--stop-id 4294967296`) exit 2 instead of being parsed leniently, and a prompt longer than 32,768 ids is refused instead of truncated.
> …

### [v1.1.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v1.1.0)
<sub>2026-10-02 · 1mo ago</sub>

> Chat, native Windows builds, an 8 GB class mode for the complete model, NEON kernels for ARM, and a round of hardening on everything that parses checkpoint files. Output is unchanged wherever it was already defined: every oracle gate still matches the PyTorch reference exactly.
> **One compatibility note:** `--save-state` files are now version 2, with a checksum. A version 1 file is refused rather than read; regenerate it with `--gen 0 --incremental --save-state`.
> **New**
> - `--chat`: the official K3 XTML chat format, with JSONL history, `--no-think`, `--thinking-effort`, and opt-in sampling through `--temperature`, `--top-p`, `--top-k` and `--seed`. Greedy by default. Later turns reuse the previous turn's state instead of re-prefilling the transcript, behind a bit-exact gate.
> - `--preset ultra`: the complete 93-layer model in an 8 GB class memory budget, verified with four full runs on a Jetson Orin Nano Super.
> - Native Windows builds through MSYS2 MinGW-w64, with every gate passing, and NEON kernels on arm64.
> …

### [v1.0.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v1.0.0)
<sub>2026-08-07 · 3mo ago</sub>

> Verified end to end on the full released 1.56 TB checkpoint, and made substantially faster, with byte-identical output preserved at every step. The first-run experience, broken on a clean clone, now works.
> **Faster (output unchanged)**
> - Fused matmul kernels (fp32, bf16, MXFP4): about 8x less per-token compute, scalar and AVX2 paths bitwise identical.
> - `--preset auto`: sizes the trunk and expert-cache budgets from the machine's own free RAM, trunk-first.
> - Chunk-union prefill: fetches each unique routed expert once per chunk, about half the expert bytes on a prompt, generated token bit-identical.
> - Conversation resume (`--save-state` / `--load-state`): a second turn resumes instead of re-reading the prompt, 3.9x faster.
> …

### [v0.1.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v0.1.0)
<sub>2026-08-02 · 3mo ago</sub>

> _No notes._

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [docs(readme): bring the README in line with 2.0.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/b26ee8231bfa4390545ef2aec3576fd834b92ba7) | FareedKhan-dev |
| 2026-11-15 | [docs(readme): add the 2.0.0 contributors to the wall](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/a228989932f4b1ab497f11a14f62f4a78d825573) | FareedKhan-dev |
| 2026-11-15 | [docs(changelog): record the full-model check on the released checkpoint](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/6cffb4113bd420627256471b4745cf8b51051e21) | FareedKhan-dev |
| 2026-11-15 | [release: v2.0.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/e16de10e63e74e7a4b39905f14b39cbae0d2c8c5) | FareedKhan-dev |
| 2026-11-15 | [docs(termux): drop the /tmp workaround and list the files parity needs](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/c5430ce3c81738a187f0070f5e3217a80792dee3) | FareedKhan-dev |
| 2026-11-15 | [docs: add Termux (Android ARM64) build guide (#109)](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/82e28f68f30fbdb5f682bff8cce23afa8ecef986) | mechmind-dwv |
| 2026-11-15 | [perf(mla): run the attention heads in parallel, bit-identical to the …](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/921f19f4ce50391d514783811bb528525b5c1ce6) | FareedKhan-dev |
| 2026-11-15 | [fix(tools): close the JSON files cmp_logits reads](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/a63a2b70af859079c3d10cf49f91a73a71797fa6) | FareedKhan-dev |
| 2026-11-15 | [ci: run the macOS job on macos-15](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/b60c29bbcf2b77a6d7de9455ea9bc9438d086d1d) | FareedKhan-dev |
| 2026-11-15 | [build: make tok passes an explicit TOK_FILES through](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/c48f8333314b8da89c7b74871419dedfb62262c4) | FareedKhan-dev |

[See all commits ↗](https://github.com/FareedKhan-dev/kimi-k3-in-c/commits)

## ⬇️ Get it

```bash
git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
```
