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
| ⭐ **Stars** | 156.2k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [799](https://github.com/farion1231/cc-switch/issues) |
| 💻 **Languages** | Rust 63% · TypeScript 36% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-tools` `claude-code` `desktop-app` `open-source` `rust` `tauri` `codex` `mcp` `provider-management` `wsl-support` `opencode` `skills` `skills-management` `hermes` `grok` `grokbuild` `pi` `deepseek-harness` `kimi-code` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-08-04 |
| 📦 **Latest release** | [v4.0.38](https://github.com/farion1231/cc-switch/releases/tag/v4.0.38) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 116.8 MB |
| 🌐 **Website** | https://ccswitch.io |

## 📦 Recent releases

### [v4.0.38](https://github.com/farion1231/cc-switch/releases/tag/v4.0.38) — CC Switch v4.0.38
<sub>2026-11-21 · today</sub>

> **CC Switch v4.0.38**
> 本版本以修复为主。一键导入链接现在可以导入 **WorkBuddy** 供应商；Linux 上也能在授权中心切换 **Antigravity** 账号；Antigravity 的会话列表不再混进空会话和内部子会话，会话阅读器能看到思考、工具调用和结果。
> 另外修复了 DeepSeek Harness 的配置文件经过某些 YAML 工具后，所有第三方供应商都消失；从访达打开 CC Switch 时，「应用」页把能正常用的 npm 安装标成「无法运行」；技能仓库不是 GitHub / GitLab / Gitea 时只提示「0 个技能」而不报错；Codex 给模型选的思考等级有时没生效；Codex 经路由的几处格式转换错误；用量重复计算；会话正文搜索失败时显示「没有会话包含这个词」；主界面变成一条白条或被 macOS 菜单栏遮住；Linux AppImage 里点链接没反应等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.38-ja.md)**
> ---
> **新增**
> …

### [v4.0.37](https://github.com/farion1231/cc-switch/releases/tag/v4.0.37) — CC Switch v4.0.37
<sub>2026-11-20 · yesterday</sub>

> **CC Switch v4.0.37**
> 本版本以修复为主。读不出来的供应商和 MCP 条目（比如由更新版本写入、经 WebDAV / S3 同步过来的）不再被当成空配置、下次保存时被默认值覆盖，而是单独列出来，可以删除；Pi 新增 **Mistral AI** 预设；韩语界面翻译整体改进。
> 另外修复了本地路由监听地址填 IPv6 时启动不了；「应用到 Claude Code 插件」会把损坏的 `~/.claude/config.json` 整个清空；网速慢时大的技能仓库下载到一半被中断；从访达打开 CC Switch 时 Codex 模型目录探测找不到 Node；工具调用参数里 `_` 开头的字段被删掉后才发给上游；移出又加回故障转移队列的供应商仍被跳过；插件页点「重试」看起来没反应等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.37-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.37-ja.md)**
> ---
> **新增**
> …

### [v4.0.36](https://github.com/farion1231/cc-switch/releases/tag/v4.0.36) — CC Switch v4.0.36
<sub>2026-11-19 · 2d ago</sub>

> **CC Switch v4.0.36**
> 本版本新增**插件**页面，可以在 CC Switch 里安装、启用、更新、卸载 Claude Code、Codex、Grok Build、MiniMax Code、OpenClaw、Pi 的插件，并管理 Claude Code、Codex、Grok Build 的插件市场。技能仓库现在可以用**访问令牌读取私有仓库**；经本地路由的供应商可以设置**费用倍率**；会话管理里能看到 Claude Code 桌面版的**章节**。
> 另外修复了 Codex 开了官方额度保护后自动审批也被拦下；Codex 聚合模式下新发布的官方模型要很久才出现；OpenCode 升级到 2.x 后 1.x 会话的用量不再统计；用量页自定义日期一输入年份就变成 1905；Antigravity 多个模型显示未定价等问题。用量统计里价格相同的推理档位现在合并成一行。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.36-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.36-ja.md)**
> ---
> **新增**
> …

### [v4.0.35](https://github.com/farion1231/cc-switch/releases/tag/v4.0.35) — CC Switch v4.0.35
<sub>2026-11-18 · 3d ago</sub>

> **CC Switch v4.0.35**
> 本版本让 Claude Code / Claude Desktop 里用 ChatGPT 账号的 Codex 卡片能用上 **GPT-6.2**，会话管理里可以看到 Codex `/goal` 的**完整目标**，请求详情里的请求 ID 可以**一键复制**。
> 另外修复了 Claude Code 的 auto 模式在关不掉思考的模型上被整体拦下；Codex 聚合模式和「打开终端」报 Responses-Lite 需要 `reasoning.context`；Codex 压缩上下文后第一条请求被拒；用量页自定义日期选到很早的年份时卡死；Skill 的托管副本不在了就卸载不掉等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.35-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.35-ja.md)**
> ---
> **新增**
> …

### [v4.0.34](https://github.com/farion1231/cc-switch/releases/tag/v4.0.34) — CC Switch v4.0.34
<sub>2026-11-17 · 4d ago</sub>

> **CC Switch v4.0.34**
> 本版本的技能仓库支持 **GitLab、Gitea 和 Forgejo**（包括自建实例和 Codeberg），不再只能添加 GitHub 上的仓库。会话管理里现在可以直接删除 **Antigravity CLI** 的会话；开启自动下载更新后，发现新版本会立刻开始下载。另外，WorkBuddy 手动添加的模型可以设置思考强度，S3 同步也可以像 WebDAV 一样清除本机保存的配置。
> 另外修复了 Gemini CLI 的供应商「获取模型列表」报 Key 无效或拿到空列表；Codex 里的 GitHub Copilot 模型被当成不支持图片；阿里云 OSS、腾讯云 COS、华为云 OBS 用不了 S3 同步；Skills 目录里有失效链接时整个云同步上传失败；路由模式下 Fable 5.2 被显示成 Fable 5；Copilot 上的 Gemini 模型缓存命中率低；Copilot 上勾了 1M 的 Fable 模型请求失败等问题。
> **[English →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.34-en.md) | [日本語版 →](https://github.com/farion1231/cc-switch/blob/main/docs/release-notes/v4.0.34-ja.md)**
> ---
> **新增**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [docs(release): add v4.0.38 release notes](https://github.com/farion1231/cc-switch/commit/2c084ec752a985fa77470facc14cad76ee67e8e1) | farion1231 |
| 2026-11-21 | [chore(release): v4.0.38](https://github.com/farion1231/cc-switch/commit/6006b663dfbae3a13a886e4c424e430cf20f25b7) | farion1231 |
| 2026-11-21 | [test(sessions): gate the Windows-only Oh My Pi test env helper](https://github.com/farion1231/cc-switch/commit/78d2daf76b2aeee4a54d5f09f0f0cf533cf5b8bc) | farion1231 |
| 2026-11-21 | [fix(skills): report a non-ZIP repo archive instead of "0 skills found"](https://github.com/farion1231/cc-switch/commit/a5fd82b6aa2c6ac369c07541a6a97ac2020ebf8a) | farion1231 |
| 2026-11-21 | [fix(tools): give the install enumeration probe the login-shell PATH](https://github.com/farion1231/cc-switch/commit/49e5d9a00fbd03a7bdfc21eb1b6624fee4a7e67e) | farion1231 |
| 2026-11-21 | [fix(dsh): normalize reasoningEfforts keys before writing cordis.patch…](https://github.com/farion1231/cc-switch/commit/18744a32da3654c51483047d25827004923c6971) | farion1231 |
| 2026-11-21 | [chore(ci): remove the unused Claude review workflow](https://github.com/farion1231/cc-switch/commit/a3a85a500e723c73ed03cfc1db18a42bb7befc52) | farion1231 |
| 2026-11-21 | [fix(agy): drop redundant Google prefix from Google AI plan names (#9834)](https://github.com/farion1231/cc-switch/commit/40f4bc900b411bfcfc3eb05e3c71e77ace51998e) | allenxu09 |
| 2026-11-21 | [fix(usage): show Codex cache writes in the usage summary and request …](https://github.com/farion1231/cc-switch/commit/1159383db14ed9d5b0559dc42b5da2d3abad21dd) | Chaoqi31 |
| 2026-11-21 | [fix(codex): honor reasoning overrides for official model names (#9017)](https://github.com/farion1231/cc-switch/commit/a18d91c56f1cc91a8560b512d86e8a5a32552246) | StrengW |

[See all commits ↗](https://github.com/farion1231/cc-switch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/farion1231/cc-switch.git
```
