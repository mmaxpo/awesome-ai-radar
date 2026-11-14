# Panniantong/Agent-Reach

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Panniantong/Agent-Reach)

> Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Gives agents access to information across the internet |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 111.7k |
| 🍴 **Forks** | 10.0k |
| 🐞 **Open issues + PRs** | [106](https://github.com/Panniantong/Agent-Reach/issues) |
| 💻 **Languages** | Python 98% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-infrastructure` `ai-agent` `ai-search` `automation` `bilibili` `claude-code` `cli` `cursor` `free-api` `llm-tools` `mcp` `python` `reddit-scraper` `twitter-scraper` `web-scraper` `xiaohongshu` `youtube-transcript` |
| 🕒 **Last activity** | 2026-11-08 (6d ago) |
| 📅 **Created** | 2026-02-24 |
| 📦 **Latest release** | [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1) — 2026-11-01 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3.3 MB |

## 📦 Recent releases

### [v1.6.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.1)
<sub>2026-11-01 · 13d ago</sub>

> 中文：
> - 全网搜索、Reddit、小红书、B站在 1.6.0 里会出现的几种"明明能查却报错"或"显示成功但内容是空的"，这版都修好了。
> - 电脑上别的软件占用了浏览器端口时，可以换一个端口，不用关掉那个软件。
> - 复制登录失败时会如实告诉你，不再假装成功。
> - Windows 上小红书带特殊符号的链接能正常打开了。
> English:
> …

### [v1.6.0](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.6.0)
<sub>2026-10-23 · 22d ago</sub>

> 中文：
> - 从旧版升级：把"帮我更新 Agent Reach"那句话发给你的 AI 就行。你的密钥和设置都保留，旧版程序会自动删掉。
> - 加一个平台只要说一句，需要的软件都会自动装好，不需要管理员密码；你只需要登录或者填一个 Key。
> - 小红书、推特这类要登录的平台，改用 Agent Reach 自己的专用浏览器，不弹窗、不占用你的浏览器；多个 AI 可以同时查。
> - RSS 订阅和 Exa 全网搜索合并进了"网页"。以后有新版本，AI 会用大白话告诉你改了什么，你同意了才更新。
> English:
> …

### [v1.5.0](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.5.0) — v1.5.0 — 能力层:多后端路由 + 真体检 + OpenCLI
<sub>2026-06-11 · 5mo ago</sub>

> **这一版是什么**
> **Agent Reach 从「工具集合」升级为「能力层」**:每个平台 = 首选 + 备选的有序后端列表,当下最稳的接入方式替你实测选好、装好、体检好——接入方式换代,你无感。本版全部选型基于 2026-06 真机实测(32 项端到端测试)。
> **平台路由变化**
> | 平台 | 现在的路 |
> |------|---------|
> | 小红书 | **OpenCLI**(桌面,复用浏览器登录态零配置)▸ xiaohongshu-mcp(服务器,扫码)▸ xhs-cli(存量备选,上游已停更) |
> …

### [v1.4.2](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.4.2) — v1.4.2 — 诚实瘦身：移除失修渠道，新增转写与 doctor --json
<sub>2026-06-10 · 5mo ago</sub>

> **渠道调整**
> **移除抖音、微博、微信公众号三个渠道。** 原因很直接——它们已经名不副实：
> - **抖音**：上游 douyin-mcp-server 已停止维护（archived），且需要手动起本地服务的 4 步配置，几乎没人能配通
> - **微博**：依赖一个久未维护的个人 fork，实际已不可用
> - **微信公众号**：全文阅读被反爬拦截越来越严重（#339），却还在宣传"零配置可用"
> 与其展示坏掉的承诺，不如诚实下架。等有可靠的上游方案时它们会回来（v1.4.0 移除 Discord/头条是同样的逻辑）。现在的口径：**13 个平台，6 个真零配置**。
> …

### [v1.4.1](https://github.com/Panniantong/Agent-Reach/releases/tag/v1.4.1) — v1.4.1 — 修复源码安装失败(wheel 重复打包)
<sub>2026-06-10 · 5mo ago</sub>

> **修复**
> **修复了源码安装失败的问题。** 近期从 GitHub 安装(`pip install .../archive/main.zip`、`pipx`、`uvx`)会因 wheel 重复打包直接构建失败:
> ```
> ValueError: A second file is being added to the wheel archive at the same path:
> `agent_reach/guides/setup-exa.md`
> ```
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-08 | [Merge pull request #934 from Panniantong/fix/reddit-linkedin-instagra…](https://github.com/Panniantong/Agent-Reach/commit/c70ae6da5d39bc90e09ad2ae0575ccc89f31e284) | Panniantong |
| 2026-11-08 | [fix(opencli): test OpenCLI 2.0.3 so LinkedIn jobs work on Chinese pag…](https://github.com/Panniantong/Agent-Reach/commit/6e9b8b3fb5b92318595d38f395b2e439903a06c3) | Panniantong |
| 2026-11-08 | [Merge pull request #925 from remote-controlled-man/codex/prflow-ffc95…](https://github.com/Panniantong/Agent-Reach/commit/a64a47e3aa236c8124c34949c16aa13c73343dba) | Panniantong |
| 2026-11-08 | [Merge pull request #851 from w21180239/feat/skill-unlink](https://github.com/Panniantong/Agent-Reach/commit/7c190890ee23f6ffb806f84bb1817792ace05569) | Panniantong |
| 2026-11-08 | [Merge pull request #779 from rahul05ranjan/fix/xueqiu-html-entities](https://github.com/Panniantong/Agent-Reach/commit/d653e8aedb26cf2f03778018f212bf7c69a16c0a) | Panniantong |
| 2026-11-08 | [Merge pull request #898 from quark404/fix/windows-hide-child-console](https://github.com/Panniantong/Agent-Reach/commit/41eba5797dc37e81c464de9dd79b93a5c3a641f2) | Panniantong |
| 2026-11-08 | [Merge remote-tracking branch 'origin/main' into sweep/b925](https://github.com/Panniantong/Agent-Reach/commit/b0c4ee273cb7cbdf4ec84aade76abb5432b3a3b0) | Panniantong |
| 2026-11-08 | [Merge remote-tracking branch 'origin/main' into sweep/b851](https://github.com/Panniantong/Agent-Reach/commit/f50e0054d3aed7823efebd8d0cdde0dc66db356c) | Panniantong |
| 2026-11-08 | [Merge remote-tracking branch 'origin/main' into sweep/pr779](https://github.com/Panniantong/Agent-Reach/commit/9f483e1598cae1f4a3d18650e42b304b23f15ac7) | Panniantong |
| 2026-11-08 | [Merge remote-tracking branch 'origin/main' into sweep/pr898](https://github.com/Panniantong/Agent-Reach/commit/c102528d844f5ec0852f1b8e93d1c6a4945d8312) | Panniantong |

[See all commits ↗](https://github.com/Panniantong/Agent-Reach/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Panniantong/Agent-Reach.git
```
