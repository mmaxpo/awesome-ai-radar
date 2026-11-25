# huggingface/smolagents

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/huggingface/smolagents)

> 🤗 smolagents: a barebones library for agents that think in code.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Hugging Face's small, code-first agent library: agents write and run Python instead of JSON tool calls. |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 30.5k |
| 🍴 **Forks** | 3.2k |
| 🐞 **Open issues + PRs** | [602](https://github.com/huggingface/smolagents/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2024-12-05 |
| 📦 **Latest release** | [v1.26.0](https://github.com/huggingface/smolagents/releases/tag/v1.26.0) — 2026-05-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 7.3 MB |
| 🌐 **Website** | https://huggingface.co/docs/smolagents |

## 📦 Recent releases

### [v1.26.0](https://github.com/huggingface/smolagents/releases/tag/v1.26.0)
<sub>2026-05-29 · 6mo ago</sub>

> **What's Changed**
> * Bump dev version: v1.26.0.dev0 by @albertvillanova in https://github.com/huggingface/smolagents/pull/2273
> * Add new possible error message to test of LiteLLM providers w/o key by @albertvillanova in https://github.com/huggingface/smolagents/pull/2275
> * Fix typo cleanups across docs, examples, and tests by @luojiyin1987 in https://github.com/huggingface/smolagents/pull/2208
> * fix: correct f-string escaping in ToolSerializer.dumps error message by @Ricardo-M-L in https://github.com/huggingface/smolagents/pull/2134
> * Revert fix: correct f-string escaping by @albertvillanova in https://github.com/huggingface/smolagents/pull/2291
> …

### [v1.25.0](https://github.com/huggingface/smolagents/releases/tag/v1.25.0)
<sub>2026-05-14 · 6mo ago</sub>

> **What's Changed**
> * Bump dev version: v1.25.0.dev0 by @albertvillanova in https://github.com/huggingface/smolagents/pull/1939
> * Fix import of TokenUsage by @albertvillanova in https://github.com/huggingface/smolagents/pull/1943
> * Add MLflow integration doc by @B-Step62 in https://github.com/huggingface/smolagents/pull/1884
> * Refactor agent/model deserialization: Replace importlib with registry pattern by @albertvillanova in https://github.com/huggingface/smolagents/pull/1944
> * Update _function_type_hints_utils.py: CohereForAI -> CohereLabs by @Michellehbn in https://github.com/huggingface/smolagents/pull/1946
> …

### [v1.24.0](https://github.com/huggingface/smolagents/releases/tag/v1.24.0)
<sub>2026-01-16 · 10mo ago</sub>

> **What's Changed**
> * Bump version to 1.24 by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1871
> * Fix: Add backward compatibility for deprecated HfApiModel by @MohammadKassas143 in https://github.com/huggingface/smolagents/pull/1863
> * Fix typo in secure_code_execution.md by @jonathanagustin in https://github.com/huggingface/smolagents/pull/1892
> * Update no-stop-sequence model list to support gpt-5.2* by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1895
> * Fix run_gaia.py token_counts when managed agent is called more than once by @suryabdev in https://github.com/huggingface/smolagents/pull/1878
> …

### [v1.23.0](https://github.com/huggingface/smolagents/releases/tag/v1.23.0)
<sub>2025-11-17 · 1y ago</sub>

> **Improvements ✨**
> * Update final answer checks to accept the agent instance by @Zoe14 in https://github.com/huggingface/smolagents/pull/1648
> * Dialog mode CLI by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1540
> * Add Blaxel support for remote code execution by @Joffref in https://github.com/huggingface/smolagents/pull/1791
> * Proposition: Add exponential backoff with jitter for retries by @suryabdev in https://github.com/huggingface/smolagents/pull/1829
> * Cut generation at stop sequence post generation by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1802
> …

### [v1.22.0](https://github.com/huggingface/smolagents/releases/tag/v1.22.0)
<sub>2025-09-25 · 1y ago</sub>

> **What's Changed**
> * Bump dev version: v1.22.0.dev0 by @albertvillanova in https://github.com/huggingface/smolagents/pull/1657
> * refactor(PythonExecutor): inherit from ABC and declare abstract methods by @HairlessVillager in https://github.com/huggingface/smolagents/pull/1654
> * Fix error for GPT-5 not supporting the `stop` parameter by @Xmader in https://github.com/huggingface/smolagents/pull/1662
> * Enable return_full_result directly in run method by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1658
> * Make RunResult json serializable by @aymeric-roucher in https://github.com/huggingface/smolagents/pull/1659
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [remove redundant UTF-8 reload tests (#3301)](https://github.com/huggingface/smolagents/commit/505b76b28d5cab580d7a4e0eaf4e8f142819e6a9) | julien-cto |
| 2026-11-25 | [fix(save-load): decode saved agents and tools as UTF-8 on reload (#3211)](https://github.com/huggingface/smolagents/commit/a8e75ce57f258368d527d20d9d42656ae090c974) | lester076 |
| 2026-11-24 | [trigger CI (#3280)](https://github.com/huggingface/smolagents/commit/d0ec5966bd0bc723988a62f91ae81ffacdddd2fe) | julien-cto |
| 2026-11-24 | [fix: send a base_url model with the call instead of to the client (#3…](https://github.com/huggingface/smolagents/commit/f1065af15485b5bd4aaa8ca663345bf267448a75) | Luckyou-d |
| 2026-11-24 | [fix(models): guard against None usage in non-streaming model generate…](https://github.com/huggingface/smolagents/commit/151ac6bb4e42ae4935f9fde4160f29e4fa1c2dde) | somuai |
| 2026-11-23 | [fix(models): send stop_sequences as inferenceConfig.stopSequences in …](https://github.com/huggingface/smolagents/commit/5107d3aec21d26ed808aabd95d93a63d4244226f) | Tirthnp |
| 2026-11-20 | [Monitor: include PlanningStep tokens in monitor totals (Fixes #3187) …](https://github.com/huggingface/smolagents/commit/99721bdc3b6f502108751a93c5d7f08b1a04ce76) | hr1juldey |
| 2026-11-18 | [Support starred and iterable unpacking in assignments (#2556)](https://github.com/huggingface/smolagents/commit/2689e450364d451a0afa0a5e883d12a031c125dd) | himanshu748 |
| 2026-11-18 | [add LlamaCppModel for Llama App (#3201)](https://github.com/huggingface/smolagents/commit/fcdf5f13563408569fff6172ee770a82a4fae710) | julien-cto |
| 2026-11-18 | [remove non-English source docs (#3208)](https://github.com/huggingface/smolagents/commit/0747ebee579039c5764de73f0949627dab64cc37) | julien-cto |

[See all commits ↗](https://github.com/huggingface/smolagents/commits)

## ⬇️ Get it

```bash
git clone https://github.com/huggingface/smolagents.git
```
