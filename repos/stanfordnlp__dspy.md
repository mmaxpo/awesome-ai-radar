# stanfordnlp/dspy

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/stanfordnlp/dspy)

> DSPy: The framework for programming—not prompting—language models

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | ✍️ Prompting & LLM programming |
| **Project** | — |
| **Why it's worth a look** | Program and auto-optimize prompts instead of hand-writing them |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 39.0k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [777](https://github.com/stanfordnlp/dspy/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-01-09 |
| 📦 **Latest release** | [3.5.0](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 183.3 MB |
| 🌐 **Website** | https://dspy.ai |

## 📦 Recent releases

### [3.5.0](https://github.com/stanfordnlp/dspy/releases/tag/3.5.0)
<sub>2026-11-10 · today</sub>

> **DSPy 3.5: A Lighter, Faster Foundation**
> DSPy 3.5 brings a lighter LM layer, graduated core modules, and new History and image capabilities for RLM.
> **Upgrading from 3.4.1**
> **This release changes prompts, defaults and APIs.** Read the [upgrade guide](https://dspy.ai/current/community/upgrading-to-3-5/) for breaking changes, migration steps and compatibility limits, and re-evaluate optimized programs.
> **Highlights**
> **RLM, Flex and GEPA graduate**
> …

### [3.4.1](https://github.com/stanfordnlp/dspy/releases/tag/3.4.1)
<sub>2026-10-12 · 29d ago</sub>

> **DSPy 3.4.1**
> DSPy 3.4.1 makes GEPA's structured `InstructionProposer` the default instruction proposer and lets `dspy.RLM` build DSPy sub-agents from inside its REPL. It also adds Python 3.15 support, fixes a 3.4.0 import crash, and includes streaming, adapter, and interpreter fixes.
> ```bash
> pip install --upgrade "dspy==3.4.1"
> ```
> **Upgrade notices.** GEPA's default reflection request changes shape, so optimization results can differ from 3.4.0 even with the same seed. The reflection LM must now be a `dspy.LM` that can return JSON. Every RLM prompt now includes a sub-agent section, and `max_llm_calls` now also counts sub-agent LM calls. `dspy.ReActV2` signatures can no longer declare inputs named `history` or `tools`. Programs saved on 3.4.0 with a null `Score` level no longer load. See [API and Compatibility Changes](#api-and-compatibility-changes).
> …

### [3.4.0](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0)
<sub>2026-09-25 · 1mo ago</sub>

> **DSPy 3.4.0**
> DSPy 3.4 introduces **Jev integration through TypeSafe**, with three experimental decision types—`Noul`, `Choice`, and `Score`—that bring probability evidence into ordinary DSPy signatures. ReAnchor calibrates those decisions against your program's metric. This release also introduces native LM engines, a local CPython interpreter for trusted code, async ReActV2, and versioned documentation.
> ```bash
> pip install --upgrade "dspy==3.4.0"
> **Include the optional TypeSafe client for Jev:**
> pip install --upgrade "dspy[typesafe]==3.4.0"
> …

### [3.4.0b1](https://github.com/stanfordnlp/dspy/releases/tag/3.4.0b1) _(pre-release)_
<sub>2026-09-11 · 2mo ago</sub>

> **DSPy 3.4.0 Beta 1**
> DSPy 3.4.0b1 is the first beta of 3.4. It moves language-model execution to a shared engine interface, adds a local CPython interpreter for trusted code, and brings async execution to ReActV2. It also adds custom Flex code proposals in GEPA and fixes evaluation, streaming, and demonstration-sampling bugs.
> **This is a prerelease, not the stable 3.4.0 release.** APIs and behavior may change before stable. We especially welcome feedback on native versus LiteLLM compatibility, tool calling and streaming, custom LM migration, saved programs, and multi-answer latency and costs. Please include your engine selection and a minimal reproduction when reporting issues.
> Install this beta explicitly:
> ```bash
> pip install --upgrade "dspy==3.4.0b1"
> …

### [3.3.1](https://github.com/stanfordnlp/dspy/releases/tag/3.3.1)
<sub>2026-08-21 · 2mo ago</sub>

> **DSPy 3.3.1**
> DSPy 3.3.1 contains many interpreter fixes and improvements. It makes `PythonInterpreter`
> easier to install, substantially strengthens sandbox isolation and request
> handling, and adds end-to-end visibility into interpreter execution. The release
> also improves optimizer throughput, adapter correctness, and MCP compatibility.
> **Highlights**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [chore: refresh model metadata from LiteLLM 1.109.0 (#10871)](https://github.com/stanfordnlp/dspy/commit/398396012371a95471c8e7be24a70e6660e87aa4) | isaacbmiller |
| 2026-11-10 | [Update versions for 3.5.0 (#10865)](https://github.com/stanfordnlp/dspy/commit/5708342f3c88b78fc3566d8294af4b1a50154c19) | github-actions[bot] |
| 2026-11-10 | [fix(dspy): find dspy's distribution by the package it installs (#10864)](https://github.com/stanfordnlp/dspy/commit/4e9db7a83e71e4c36315a2402ae7ffd0c6493404) | isaacbmiller |
| 2026-11-10 | [fix(clients): exclude LiteLLM releases with eager MCP imports (#10863)](https://github.com/stanfordnlp/dspy/commit/4f2ecefc50a31d9e67b621f88c072cee17736753) | isaacbmiller |
| 2026-11-10 | [docs(dspy): add concise DSPy 3.5 upgrade guide (#10862)](https://github.com/stanfordnlp/dspy/commit/743b0ce16dae7be1e64858724bde95746dacc15b) | isaacbmiller |
| 2026-11-10 | [docs: make the RLM sandbox package example executable (#10860)](https://github.com/stanfordnlp/dspy/commit/471b3fb0e4efad45dbac980e42b1258f55a245cf) | isaacbmiller |
| 2026-11-10 | [Fix tool call IDs in serialized ReAct history (#10844)](https://github.com/stanfordnlp/dspy/commit/c472201fc7bd06fbcd712bf083d69908f6777080) | isaacbmiller |
| 2026-11-10 | [fix(tool): keep nested schema references scoped in native declarations (#10845)](https://github.com/stanfordnlp/dspy/commit/340deccd528805f01078113b9476e37072f75d0d) | isaacbmiller |
| 2026-11-10 | [fix(xml): honor positional tuple schemas (#10850)](https://github.com/stanfordnlp/dspy/commit/ede7a62d066c9eef68a82898f62d1dc3b314cd41) | isaacbmiller |
| 2026-11-10 | [fix(adapters): preserve nested XML enum and null guidance (#10859)](https://github.com/stanfordnlp/dspy/commit/07fa634dc06104b03787c728de49c668d75559e7) | isaacbmiller |

[See all commits ↗](https://github.com/stanfordnlp/dspy/commits)

## 👥 Top contributors

[okhat](https://github.com/okhat) (1129) · [arnavsinghvi11](https://github.com/arnavsinghvi11) (402) · [isaacbmiller](https://github.com/isaacbmiller) (401) · [chenmoneygithub](https://github.com/chenmoneygithub) (265) · [krypticmouse](https://github.com/krypticmouse) (201)

## ⬇️ Get it

```bash
git clone https://github.com/stanfordnlp/dspy.git
```
