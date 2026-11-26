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
| ⭐ **Stars** | 157.4k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [765](https://github.com/farion1231/cc-switch/issues) |
| 💻 **Languages** | Rust 63% · TypeScript 36% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-tools` `claude-code` `desktop-app` `open-source` `rust` `tauri` `codex` `mcp` `provider-management` `wsl-support` `opencode` `skills` `skills-management` `hermes` `grok` `grokbuild` `pi` `deepseek-harness` `kimi-code` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-08-04 |
| 📦 **Latest release** | [v4.0.42](https://github.com/farion1231/cc-switch/releases/tag/v4.0.42) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 120.1 MB |
| 🌐 **Website** | https://ccswitch.io |

## 📦 Recent releases

### [v4.0.42](https://github.com/farion1231/cc-switch/releases/tag/v4.0.42) — CC Switch v4.0.42
<sub>2026-11-25 · yesterday</sub>

> **CC Switch v4.0.42**
> 本版本让 **GitHub Copilot** 供应商支持 Copilot 的 **Auto 自动选模型**：在 Claude、Codex 或 Claude Desktop 的模型列表里选「GitHub Copilot 自动选择」，每次对话由 Copilot 决定用哪个模型，Copilot Free 账号也能用。
> 本版本还修复了 4.0.41 引入的问题：所有应用的供应商卡片都显示「agy 在用」，副标题也被换成 Antigravity 账号邮箱。另外，Antigravity 官方卡换号时，系统钥匙串第一次读回失败不会再把已经换好的账号绑定撤销。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.42-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.42-ja.md)**
> ---
> **新增**
> …

### [v4.0.41](https://github.com/farion1231/cc-switch/releases/tag/v4.0.41) — CC Switch v4.0.41
<sub>2026-11-25 · yesterday</sub>

> **CC Switch v4.0.41**
> 本版本新增 **CodeBuddy** 支持（腾讯的 CLI 和桌面版共用一套配置）：可以管理自定义模型、MCP、Skills、提示词、会话和用量，在授权中心收集多个官方账号，查看套餐、积分和到期时间并随时切换。**Copilot CLI** 的供应商可以一键同步到 VS Code 的 Copilot 插件；**Grok 官方卡**显示订阅等级。
> 本版本还让 Claude 原生转发复用上游连接，主窗口和托盘面板启动时加载的代码更少，后台请求和供应商连通性检查失败时会说明原因，并加固了数据库文件权限、备份文件名、CONNECT 代理和深链接的安全检查。另外修复了 Codex 路由到 Opus / Sonnet 5.5 时工具调用后报「requires adaptive thinking」；Gemini Native 工具调用历史较长时报 400；旧请求的故障转移结果覆盖手动选的路由；Antigravity 卡片绑定的账号和授权中心不同步；Codex 分叉会话的用量一直不入账；Pi 插件被当成 pnpm 处理；Windows 上 Hermes 显示两处安装；macOS 更新后 Dock 栏多出一个图标等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.41-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.41-ja.md)**
> ---
> **新增**
> …

### [v4.0.40](https://github.com/farion1231/cc-switch/releases/tag/v4.0.40) — CC Switch v4.0.40
<sub>2026-11-23 · 3d ago</sub>

> **CC Switch v4.0.40**
> 本版本让 **Grok Build 的官方卡可以绑定授权中心里的 xAI 账号**，像 Claude、Codex 官方卡一样在多个 Grok 账号之间切换。**插件页**支持 Antigravity CLI；**用量统计**的供应商和模型列表加了缓存命中率；**小米 MiMo** 内置余额和 Token Plan 额度查询；授权中心的账号卡片跟随侧栏应用的顺序和隐藏设置。
> 本版本还加固了深链接导入 MCP、用量脚本、SQL 导入和非本机监听地址的安全检查，并提升了数据库、本地路由、用量同步、会话搜索和「应用」页的速度。另外修复了 Kimi Code Desktop 主 agent 的用量没统计；Antigravity 输出速度从 4.0.38 起虚高；T3 Code 和单独运行的 ACP 里的 Antigravity 会话看不到；Mistral 官方 API 开思考后回复为空；Kimi 原生 Responses 在并行看图工具调用后一直报 400；WorkBuddy 企业账号积分显示为已用完；托盘里看不到 xAI 额度、官方账号显示成网站域名；Skills 页的「发现」里出现重复的技能；「应用」页要等版本检查完才显示安装状态等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.40-ja.md)**
> ---
> **新增**
> …

### [v4.0.39](https://github.com/farion1231/cc-switch/releases/tag/v4.0.39) — CC Switch v4.0.39
<sub>2026-11-22 · 4d ago</sub>

> **CC Switch v4.0.39**
> 本版本以修复为主。**API Key 输入框**加了复制按钮；**备份**可以设置总大小上限，超过时从最旧的开始删；Claude Code 经 Codex OAuth 使用 **GPT-6.2 Sol / Astra** 时，系统提示的缓存命中率大幅提高。
> 另外修复了 Claude Code 和 Claude Desktop 的原生供应商卡住不出字时，要等最长 600 秒才故障转移；很长的流式响应让用量和日志收集占用的内存一直增长；一键导入链接合并配置失败后仍弹出确认框；只装了 Codex 桌面版时，插件页显示「未安装 Codex」；插件页给没装的应用建了空配置文件夹；OpenCode Go 的 DeepSeek V4.1 Flash 缺少 `max` 思考档位；快速点击时弹出层和下拉菜单闪烁等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.39-ja.md)**
> ---
> **新增**
> …

### [v4.0.38](https://github.com/farion1231/cc-switch/releases/tag/v4.0.38) — CC Switch v4.0.38
<sub>2026-11-21 · 5d ago</sub>

> **CC Switch v4.0.38**
> 本版本以修复为主。一键导入链接现在可以导入 **WorkBuddy** 供应商；Linux 上也能在授权中心切换 **Antigravity** 账号；Antigravity 的会话列表不再混进空会话和内部子会话，会话阅读器能看到思考、工具调用和结果。
> 另外修复了 DeepSeek Harness 的配置文件经过某些 YAML 工具后，所有第三方供应商都消失；从访达打开 CC Switch 时，「应用」页把能正常用的 npm 安装标成「无法运行」；技能仓库不是 GitHub / GitLab / Gitea 时只提示「0 个技能」而不报错；Codex 给模型选的思考等级有时没生效；Codex 经路由的几处格式转换错误；用量重复计算；会话正文搜索失败时显示「没有会话包含这个词」；主界面变成一条白条或被 macOS 菜单栏遮住；Linux AppImage 里点链接没反应等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-ja.md)**
> ---
> **新增**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [docs(release): add v4.0.43 release notes](https://github.com/farion1231/cc-switch/commit/754fed72d428c66c1e6ed45f38601ac25ded90c6) | farion1231 |
| 2026-11-26 | [chore(release): v4.0.43](https://github.com/farion1231/cc-switch/commit/40a61aec2b4173e73481f882493afef6a34a0080) | farion1231 |
| 2026-11-26 | [docs(manual): cover the tray Antigravity accounts, manual-only quota …](https://github.com/farion1231/cc-switch/commit/612212dd2b980210791263e9de4b9d4a1691ceda) | farion1231 |
| 2026-11-26 | [fix(apps): follow the installed OpenCode release line in the Apps page](https://github.com/farion1231/cc-switch/commit/3c49b5cdc55d18bf15a8f3412e186873286415de) | farion1231 |
| 2026-11-26 | [fix(codex): explain how the desktop app shows Fast on third-party cards](https://github.com/farion1231/cc-switch/commit/c8903de77ccb28569f4c2651b335d365f7010eef) | farion1231 |
| 2026-11-26 | [fix(codex): lock the official Fast tier switch on cards without a mod…](https://github.com/farion1231/cc-switch/commit/66817dc2588c6ac74c72fb579182fae04a0ca5d5) | farion1231 |
| 2026-11-26 | [fix(proxy): keep converted Chat reasoning item ids out of OpenAI's lo…](https://github.com/farion1231/cc-switch/commit/148c1005be89ea12ace8a7ef8e82c2e45c0e749d) | farion1231 |
| 2026-11-26 | [feat(tray): switch Antigravity official accounts from the tray](https://github.com/farion1231/cc-switch/commit/4a9f88546cd335ca7f857da72eb234453120ee22) | farion1231 |
| 2026-11-26 | [fix(tray): keep the macOS menu bar icon position across quits and res…](https://github.com/farion1231/cc-switch/commit/2a0f43331b1358b88c37f761fef3f437738673d5) | farion1231 |
| 2026-11-26 | [fix(usage): time Claude session replies from the request that produce…](https://github.com/farion1231/cc-switch/commit/9967927cb8ecb47c4c22a44d50e30c1113ee8c90) | farion1231 |

[See all commits ↗](https://github.com/farion1231/cc-switch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/farion1231/cc-switch.git
```
