# farion1231/cc-switch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/farion1231/cc-switch)

> A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Desktop switcher for Claude Code, Codex, OpenCode providers & configs |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 157.6k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [767](https://github.com/farion1231/cc-switch/issues) |
| 💻 **Languages** | Rust 64% · TypeScript 36% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-tools` `claude-code` `desktop-app` `open-source` `rust` `tauri` `codex` `mcp` `provider-management` `wsl-support` `opencode` `skills` `skills-management` `hermes` `grok` `grokbuild` `pi` `deepseek-harness` `kimi-code` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2025-08-04 |
| 📦 **Latest release** | [v4.0.43](https://github.com/farion1231/cc-switch/releases/tag/v4.0.43) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 120.6 MB |
| 🌐 **Website** | https://ccswitch.io |

## 📦 Recent releases

### [v4.0.43](https://github.com/farion1231/cc-switch/releases/tag/v4.0.43) — CC Switch v4.0.43
<sub>2026-11-26 · today</sub>

> **CC Switch v4.0.43**
> 本版本为授权中心增加了「自动查询额度」开关：关掉后，官方账号的额度只在你点刷新时才查，适合经代理上网、不想在代理就绪前直连官方服务的情况。托盘里也能直接切换 Antigravity 官方账号，每个账号旁边显示剩余额度。「应用」页现在认得 OpenCode 2，能正确检查更新、升级和卸载；OpenCode 2.4 的会话也能显示助手回复了。用量统计的速度只算成功的请求，并剔除中转缓冲后一次性吐出的异常值。
> 修复包括：先用 Chat Completions 供应商、再在直连模式下切回官方 ChatGPT 时 Codex 会话无法继续，macOS 每次退出后菜单栏图标位置被重置，`~/.gemini/.env` 里带引号的值，带块注释的 OpenClaw 配置被写坏，删除环境变量后 shell 配置丢了末尾换行，以及 Pi 的插件识别和更新问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.43-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.43-ja.md)**
> ---
> **新增**
> …

### [v4.0.42](https://github.com/farion1231/cc-switch/releases/tag/v4.0.42) — CC Switch v4.0.42
<sub>2026-11-25 · 2d ago</sub>

> **CC Switch v4.0.42**
> 本版本让 **GitHub Copilot** 供应商支持 Copilot 的 **Auto 自动选模型**：在 Claude、Codex 或 Claude Desktop 的模型列表里选「GitHub Copilot 自动选择」，每次对话由 Copilot 决定用哪个模型，Copilot Free 账号也能用。
> 本版本还修复了 4.0.41 引入的问题：所有应用的供应商卡片都显示「agy 在用」，副标题也被换成 Antigravity 账号邮箱。另外，Antigravity 官方卡换号时，系统钥匙串第一次读回失败不会再把已经换好的账号绑定撤销。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.42-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.42-ja.md)**
> ---
> **新增**
> …

### [v4.0.41](https://github.com/farion1231/cc-switch/releases/tag/v4.0.41) — CC Switch v4.0.41
<sub>2026-11-25 · 2d ago</sub>

> **CC Switch v4.0.41**
> 本版本新增 **CodeBuddy** 支持（腾讯的 CLI 和桌面版共用一套配置）：可以管理自定义模型、MCP、Skills、提示词、会话和用量，在授权中心收集多个官方账号，查看套餐、积分和到期时间并随时切换。**Copilot CLI** 的供应商可以一键同步到 VS Code 的 Copilot 插件；**Grok 官方卡**显示订阅等级。
> 本版本还让 Claude 原生转发复用上游连接，主窗口和托盘面板启动时加载的代码更少，后台请求和供应商连通性检查失败时会说明原因，并加固了数据库文件权限、备份文件名、CONNECT 代理和深链接的安全检查。另外修复了 Codex 路由到 Opus / Sonnet 5.5 时工具调用后报「requires adaptive thinking」；Gemini Native 工具调用历史较长时报 400；旧请求的故障转移结果覆盖手动选的路由；Antigravity 卡片绑定的账号和授权中心不同步；Codex 分叉会话的用量一直不入账；Pi 插件被当成 pnpm 处理；Windows 上 Hermes 显示两处安装；macOS 更新后 Dock 栏多出一个图标等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.41-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.41-ja.md)**
> ---
> **新增**
> …

### [v4.0.40](https://github.com/farion1231/cc-switch/releases/tag/v4.0.40) — CC Switch v4.0.40
<sub>2026-11-23 · 4d ago</sub>

> **CC Switch v4.0.40**
> 本版本让 **Grok Build 的官方卡可以绑定授权中心里的 xAI 账号**，像 Claude、Codex 官方卡一样在多个 Grok 账号之间切换。**插件页**支持 Antigravity CLI；**用量统计**的供应商和模型列表加了缓存命中率；**小米 MiMo** 内置余额和 Token Plan 额度查询；授权中心的账号卡片跟随侧栏应用的顺序和隐藏设置。
> 本版本还加固了深链接导入 MCP、用量脚本、SQL 导入和非本机监听地址的安全检查，并提升了数据库、本地路由、用量同步、会话搜索和「应用」页的速度。另外修复了 Kimi Code Desktop 主 agent 的用量没统计；Antigravity 输出速度从 4.0.38 起虚高；T3 Code 和单独运行的 ACP 里的 Antigravity 会话看不到；Mistral 官方 API 开思考后回复为空；Kimi 原生 Responses 在并行看图工具调用后一直报 400；WorkBuddy 企业账号积分显示为已用完；托盘里看不到 xAI 额度、官方账号显示成网站域名；Skills 页的「发现」里出现重复的技能；「应用」页要等版本检查完才显示安装状态等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-ja.md)**
> ---
> **新增**
> …

### [v4.0.39](https://github.com/farion1231/cc-switch/releases/tag/v4.0.39) — CC Switch v4.0.39
<sub>2026-11-22 · 5d ago</sub>

> **CC Switch v4.0.39**
> 本版本以修复为主。**API Key 输入框**加了复制按钮；**备份**可以设置总大小上限，超过时从最旧的开始删；Claude Code 经 Codex OAuth 使用 **GPT-6.2 Sol / Astra** 时，系统提示的缓存命中率大幅提高。
> 另外修复了 Claude Code 和 Claude Desktop 的原生供应商卡住不出字时，要等最长 600 秒才故障转移；很长的流式响应让用量和日志收集占用的内存一直增长；一键导入链接合并配置失败后仍弹出确认框；只装了 Codex 桌面版时，插件页显示「未安装 Codex」；插件页给没装的应用建了空配置文件夹；OpenCode Go 的 DeepSeek V4.1 Flash 缺少 `max` 思考档位；快速点击时弹出层和下拉菜单闪烁等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-ja.md)**
> ---
> **新增**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [chore: credit fnyfree for the ZCode usage sync batching (#10053)](https://github.com/farion1231/cc-switch/commit/3cd481c0ba447cca53d3053d2d2c179e1bd18e7e) | farion1231 |
| 2026-11-27 | [perf(zcode): batch usage sync in one transaction and reuse sync curso…](https://github.com/farion1231/cc-switch/commit/0747c615df2a1dd89e93b62b9eb3abf953eb4654) | allenxu09 |
| 2026-11-27 | [fix(agy): hide console window when probing agy version on Windows (#1…](https://github.com/farion1231/cc-switch/commit/119534e7be4d7ba5541abf2b75bdfd17dbd5fce9) | fodangithub |
| 2026-11-27 | [fix(skill): name the actual app in protected Skill messages (#10044)](https://github.com/farion1231/cc-switch/commit/3a400d533c06d0de9f53e1104e810ab4c26d58a3) | JackieJK |
| 2026-11-27 | [fix(auth-center): keep xAI card visible for Grok Build and align card…](https://github.com/farion1231/cc-switch/commit/b46478483db670615dcf84c80a109e60d6383fea) | jimpablo |
| 2026-11-27 | [fix(codex): preserve stashed OAuth when clearing third-party residue …](https://github.com/farion1231/cc-switch/commit/60bb09b6a2f9f394e5def1cb0948fb7f7adafc7f) | D1screteWave |
| 2026-11-27 | [fix(agy): bound quota concurrency, early-return 403/429, skip extra k…](https://github.com/farion1231/cc-switch/commit/3abf262e529c95352bc8d933ed06a925d0d42b7a) | jimpablo |
| 2026-11-27 | [fix(proxy): cap the per-event buffer in SSE converters (#9938)](https://github.com/farion1231/cc-switch/commit/8b045ff71f8e135e608a8460ea4d0ffcd99fdfcc) | wlndysky |
| 2026-11-27 | [feat(presets): add TeleAI Xing4.1-Preview presets](https://github.com/farion1231/cc-switch/commit/1da9baf5e5fb0e116fff29b4d512f17a497332ce) | farion1231 |
| 2026-11-27 | [feat(presets): promote SudoCode to a full sponsor](https://github.com/farion1231/cc-switch/commit/c446b982906a084b61e84ca5cbc2a11a572b69b6) | farion1231 |

[See all commits ↗](https://github.com/farion1231/cc-switch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/farion1231/cc-switch.git
```
