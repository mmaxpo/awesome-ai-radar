# ranxianglei/billion-context

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ranxianglei/billion-context)

> A context-compression plugin for month-long single sessions (billions of tokens)  and small context windows (a 100K context is enough), billion-context is all you need .

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Context-compression plugin for long coding-agent sessions |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 8.4k |
| 🍴 **Forks** | 681 |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/ranxianglei/billion-context/issues) |
| 💻 **Languages** | TypeScript 98% · JavaScript 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-08-06 |
| 📦 **Latest release** | [v0.1.216](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.216) — 2026-11-17 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 92.8 MB |

## 📦 Recent releases

### [v0.1.216](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.216)
<sub>2026-11-17 · 8d ago</sub>

> **What's Changed**
> * [PR] gate: two fixes — evidence file is now readable after the run completes + one retry added for the small-window round in  | gate 两个修复:跑完后证据文件能读了 + R 车道小窗口轮次加一次重试 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6808
> * [PR] Gate performance overhaul: P/R lanes parallelized, wall clock 45 min → ~18 min | gate 性能改造:P/R 车道并行,墙钟 45min→~18min by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6810
> * [PR] chore(branch): land 20 single-purpose fixes as one history-preserving batch (wave 10) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6765
> * [PR] fix: pass Claude Code's MCP config as --mcp-config=<file> so it cannot eat the prompt by @MohammadErfan-Jabbari in https://github.com/ranxianglei/billion-context/pull/6524
> * [PR] fix: retry context overflow with measured output headroom by @zouzh22 in https://github.com/ranxianglei/billion-context/pull/6529
> …

### [v0.1.215](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.215)
<sub>2026-11-15 · 10d ago</sub>

> **What's Changed**
> * [PR] gate: fix upstream recorder leak causing real model gate deadlock (pipe inheritance) | gate: 修上游 recorder 泄漏导致真模型门禁卡死（管道继承） by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6671
> * [PR] chore(branch): land 40 single-purpose fixes as one history-preserving batch (wave 5) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/6677
> * [PR] fix: map search evidence offsets back to original Unicode text by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6494
> * [PR] fix: interpret cache-diff byte offsets in original text coordinates by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6496
> * [PR] fix: preserve null response bodies in the inline HTTP engine by @Afloat16 in https://github.com/ranxianglei/billion-context/pull/6502
> …

### [v0.1.214](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.214)
<sub>2026-11-14 · 11d ago</sub>

> **What's Changed**
> * [PR] docs: clarify that top-level modelContextLimit / ACP_MODEL_CONTEXT_LIMIT are a last-resort window fallback (#5908) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5909
> * [PR] docs: How-it-works SVG diagrams (en/zh) replacing the ASCII box by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5916
> * [PR] Review follow-ups: 429 throttle saturation/scope guardrails, media-refs carry-forward filter, oversize-refusal messages that say what to do, doc typo by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5905
> * [PR] docs: Minor Documentation Fixes, Part 4 — 6 pure documentation/disclosure fixes bundled for review | docs: 文档小修合集第四辑 —— 6 件纯文档/披露类小修合并送审 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5918
> * [PR] fix(dsh): dsh lane minor fixes batch #5 — activation & other tool registration + liveness log wording | fix(dsh): dsh 车道小修合集第五辑 —— 激活等工具注册 + 存活日志措辞 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5921
> …

### [v0.1.213](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.213)
<sub>2026-11-07 · 17d ago</sub>

> **What's Changed**
> * [PR] fix: revert self-contradictory inclusive billing stamp to split (#5515) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5518
> * [PR] docs(website): add blog post 'What to Do When the Model Keeps Treating Old Compressed Content as New User Instructions?' | docs(website): add blog post '模型总是把压缩老内容当成用户新指令咋办?' (EN+ZH) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5549
> * [PR] fix: read Responses additional_tools preamble in tool reachability observation by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5528
> * [PR] fix: replay unsigned thinking when the upstream does not sign it (#5495) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5496
> * [PR] fix(copy): false-advertising sweep of ACP tool surfaces (host-side) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5556
> …

### [v0.1.212](https://github.com/ranxianglei/billion-context/releases/tag/v0.1.212)
<sub>2026-11-02 · 23d ago</sub>

> **What's Changed**
> * [PR] (ai: anthropic/claude-opus-4-6) fix(release): nuclear box = deps download + build + publish, zero checks; add local zero-install publish script by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5436
> * [PR] Manually remove the fucking AI restrictions | 手动取消傻逼ai限制 by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5444
> * [PR] Restore the old CI release manual. | 恢复老的ci release manal by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5446
> * [PR] Restore the emergency channel (raw_publish/skip_ci_gate) + fix the four feature regressions introduced by this revert (A | 恢复紧急通道(raw_publish/skip_ci_gate)+修掉这次回退带回来的四处功能损失(A–E) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5447
> * [PR] fix(release): land the raw-publish bump as a commit before tagging/syncing (empty sync PR 422 + stale-version tag) by @ranxianglei in https://github.com/ranxianglei/billion-context/pull/5457
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Merge pull request #7691 from ranxianglei/ci-full-eg-2026-11-25](https://github.com/ranxianglei/billion-context/commit/ced22b1d2b0576ac3c6f8169f2ecbe9f3d8f3a45) | ranxianglei |
| 2026-11-25 | [fix(ci-full): close the two red gates from 6842c71](https://github.com/ranxianglei/billion-context/commit/62f7b082660dfab45b20186d28a70c7ad196a133) | ranxianglei |
| 2026-11-25 | [feat(egress): renumber — the op log's log_seq IS the kernel citation …](https://github.com/ranxianglei/billion-context/commit/6842c7131b7d92dda86050e64680d1e65fab6647) | ranxianglei |
| 2026-11-25 | [docs(egress): lock the renumber design — log_seq IS the citation number](https://github.com/ranxianglei/billion-context/commit/31dc28085b533f83aa3c24a3f0f08910b9dbda7b) | ranxianglei |
| 2026-11-25 | [Merge pull request #6993 from ranxianglei/fix-4913-degenerate-turn-te…](https://github.com/ranxianglei/billion-context/commit/9c8307c804c2f08908bfabd9e3711e818d160b1c) | ranxianglei |
| 2026-11-25 | [test(ci-full): scope the real pi/dsh e2e lanes off the egress plane](https://github.com/ranxianglei/billion-context/commit/5c73de39b3774d3cce44dcee9271b737d213b32c) | ranxianglei |
| 2026-11-25 | [test(ci-full): scope legacy-wire suites off the egress plane](https://github.com/ranxianglei/billion-context/commit/eccdddc3755b9c652bc2178cfc7203187440af07) | ranxianglei |
| 2026-11-25 | [rollout: egress family defaults to 100 — ci:full verification branch …](https://github.com/ranxianglei/billion-context/commit/8341b976593724111db32236e8298f16dcc8d50c) | ranxianglei |
| 2026-11-25 | [Merge pull request #7664 from ranxianglei/egress-fork-wiring](https://github.com/ranxianglei/billion-context/commit/64b578b1e651bcd33dfa4913ef1e24e31fc57d43) | ranxianglei |
| 2026-11-25 | [fix(plugin): the fork source link must not leak a damaged flow as FOR…](https://github.com/ranxianglei/billion-context/commit/6618014d2c545e7c9c39949f86b34b3c63ef0972) | ranxianglei |

[See all commits ↗](https://github.com/ranxianglei/billion-context/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ranxianglei/billion-context.git
```
