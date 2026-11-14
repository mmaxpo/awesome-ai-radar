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

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 12.1k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [33](https://github.com/FareedKhan-dev/kimi-k3-in-c/issues) |
| 💻 **Languages** | C 71% · Python 20% · Shell 5% · Makefile 2% · CMake 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `avx2` `c99` `cpu-inference` `deep-learning` `from-scratch` `inference-engine` `kimi-k3` `linear-attention` `llm` `llm-inference` `machine-learning` `memory-efficient` `mixture-of-experts` `moe` `mxfp4` `quantization` `simd` `systems-programming` `transformer` `zero-dependencies` |
| 🕒 **Last activity** | 2026-10-02 (1mo ago) |
| 📅 **Created** | 2026-08-01 |
| 📦 **Latest release** | [v1.1.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/releases/tag/v1.1.0) — 2026-10-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 31.0 MB |
| 🌐 **Website** | https://medium.com/@fareedkhandev/building-kimi-k3-in-c-to-run-a-2-8t-model-on-consumer-hardware-a5792cbf3b59 |

## 📦 Recent releases

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
| 2026-10-02 | [docs(readme): move the contributor wall to the top](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/81bb6c23ccee2154bc35cad922588ab66494a9a9) | FareedKhan-dev |
| 2026-10-02 | [fix(trunk): charge a prefetched layer to the bind that reaches it](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/7721a1b1661f8a153634e27a7b0ba0327ef37d08) | FareedKhan-dev |
| 2026-10-02 | [docs: show contributors and star history in the README](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/fd8bf5219fae5de680dceafef09560057ecec6b2) | FareedKhan-dev |
| 2026-10-02 | [docs(contributors): credit Deobot2 for the trunk pinning work](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/358dfcca0e78c82e42dc6d7c4c5cb775aecd856f) | FareedKhan-dev |
| 2026-10-02 | [release: v1.1.0](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/1025d9e4990b211ec501b9bc17e9fdc43dcb4c14) | FareedKhan-dev |
| 2026-10-02 | [docs: say how much free memory a preset needs, not only its peak RSS](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/e5dc42f44413a56b696f46f1909b6ab6d348f2d0) | FareedKhan-dev |
| 2026-10-02 | [docs: catch the README up with the CLI, and record this round](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/1ae4d62c21814342b49c48e42bbc825f1865e3a8) | FareedKhan-dev |
| 2026-10-02 | [feat(scripts): fetch only the shards a --layers N run needs](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/0838cb4cc45f836adaf45ba1efeae8586baf2f7e) | FareedKhan-dev |
| 2026-10-02 | [perf(cache): split each expert read into 1 MiB chunks](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/916c0e716693ede4f84739b866ef266eea9b3dd1) | FareedKhan-dev |
| 2026-10-02 | [fix(cli): let --preset auto start on large machines, and add --threads](https://github.com/FareedKhan-dev/kimi-k3-in-c/commit/64bf532edb9db39820faf853e01d07f94b1edeec) | FareedKhan-dev |

[See all commits ↗](https://github.com/FareedKhan-dev/kimi-k3-in-c/commits)

## ⬇️ Get it

```bash
git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
```
