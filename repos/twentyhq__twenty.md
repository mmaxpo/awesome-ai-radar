# twentyhq/twenty

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/twentyhq/twenty)

> The open alternative to Salesforce, designed for AI.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Open-source Salesforce alternative built for AI |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 61.3k |
| 🍴 **Forks** | 10.1k |
| 🐞 **Open issues + PRs** | [183](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [sdk/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.59.0) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3023.0 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [sdk/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.59.0)
<sub>2026-11-16 · 4d ago</sub>

> **✨ New features**
> - feat(cli): pull public application assets ([#30275](https://github.com/twentyhq/twenty/pull/30275)) by @Weiko
> - feat(cli): export workspace records to CSV ([#30279](https://github.com/twentyhq/twenty/pull/30279)) by @Weiko
> - feat(cli): preserve imported application sources in builds ([#30281](https://github.com/twentyhq/twenty/pull/30281)) by @Weiko
> - feat(cli): send proxy headers to servers behind authenticating proxies ([#30310](https://github.com/twentyhq/twenty/pull/30310)) by @FelixMalfait
> **💅 Improvements & UX**
> …

### [twenty/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.59.0)
<sub>2026-11-16 · 4d ago</sub>

> **✨ New features**
> - feat(billing): record admin usage limit overrides as arrangements ([#29469](https://github.com/twentyhq/twenty/pull/29469)) by @etiennejouan
> - feat(inbox): preview chat images inline, browse them, and share attachments with Messages ([#30127](https://github.com/twentyhq/twenty/pull/30127)) by @etiennejouan
> - feat(teams): manually link Teams users to workspace members ([#30156](https://github.com/twentyhq/twenty/pull/30156)) by @abdulrahmancodes
> - feat(inbox): show direct messages in their own sidebar section ([#30232](https://github.com/twentyhq/twenty/pull/30232)) by @etiennejouan
> - feat(cli): pull public application assets ([#30275](https://github.com/twentyhq/twenty/pull/30275)) by @Weiko
> …

### [twenty/v2.58.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.58.0)
<sub>2026-11-13 · 8d ago</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Drop the legacy workspace workflow object ([#30036](https://github.com/twentyhq/twenty/pull/30036)) by @charlesBochet
> - [BREAKING_CHANGE] Read row level permission rules in the permission compiler ([#30132](https://github.com/twentyhq/twenty/pull/30132)) by @charlesBochet
> - [BREAKING_CHANGE] Mask record grants with limiting roles and drop legacy current user permissions ([#30145](https://github.com/twentyhq/twenty/pull/30145)) by @charlesBochet
> - chore(security): bump exa-js to 2.28.0 in the exa app ([#30188](https://github.com/twentyhq/twenty/pull/30188)) by @mabdullahabaid
> **✨ New features**
> …

### [sdk/v2.58.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.58.0)
<sub>2026-11-13 · 8d ago</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Drop the legacy workspace workflow object ([#30036](https://github.com/twentyhq/twenty/pull/30036)) by @charlesBochet
> - [BREAKING_CHANGE] Read row level permission rules in the permission compiler ([#30132](https://github.com/twentyhq/twenty/pull/30132)) by @charlesBochet
> - [BREAKING_CHANGE] Mask record grants with limiting roles and drop legacy current user permissions ([#30145](https://github.com/twentyhq/twenty/pull/30145)) by @charlesBochet
> **💅 Improvements & UX**
> - Agents design fixes ([#29288](https://github.com/twentyhq/twenty/pull/29288)) by @Bonapara
> …

### [twenty/v2.57.1](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.57.1)
<sub>2026-11-09 · 11d ago</sub>

> Claude thinking tokens were being billed at roughly 1.7 times the actual Anthropic cost. That is fixed in this release, and cache writes are now priced correctly too. If your workspace uses AI features, credit usage will drop from this version forward.
> Installed app and marketplace pages show their content again. You can see what data objects, automations, and interface pieces an app includes before or after installing it. SAML providers saved with PEM certificates now authenticate correctly.
> The Security and Privacy settings pages have been reorganized. Iframe origins and media access use table-style inputs with favicons, the AI card links to the agents and model tiers it affects, and the compliance section opens with a cleaner layout.
> **🌟 Highlights**
> - Claude thinking tokens were billed at about 1.7× the Anthropic rate — that is now corrected, and cache writes are priced correctly too. ([#29976](https://github.com/twentyhq/twenty/pull/29976))
> - Installed app and marketplace pages show the full content an app adds — data, automations, interface pieces — after being missing since earlier this year. ([#29707](https://github.com/twentyhq/twenty/pull/29707))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [Record the actual level on impersonation audit events (#31101)](https://github.com/twentyhq/twenty/commit/caf62b888a05fc3966931617f6455982d3214b51) | prastoin |
| 2026-11-21 | [i18n - translations (#31105)](https://github.com/twentyhq/twenty/commit/80f03c8df028186874802b42a3a5c3183e35a198) | twenty-pr[bot] |
| 2026-11-21 | [Key access groups by type and rule shape, shared across roles (#31097)](https://github.com/twentyhq/twenty/commit/bfba91f0eb9801dfb14d3325068234f4508ffb56) | charlesBochet |
| 2026-11-21 | [Group consecutive chat messages from the same sender (#31003)](https://github.com/twentyhq/twenty/commit/d6269f917847e7bfc21f58378080646b62d97039) | Bonapara |
| 2026-11-21 | [Refresh the tool index when it is read instead of from an effect (#31…](https://github.com/twentyhq/twenty/commit/31f5b11c396814aa181de22ebf353d9f783c5779) | charlesBochet |
| 2026-11-21 | [Inline the AI chat and inbox sync logic into their effects (#31102)](https://github.com/twentyhq/twenty/commit/be3a61212cb04a28ea1fbe02ee3965a5847773ee) | charlesBochet |
| 2026-11-21 | [Count connected members per app on the server and revoke in one state…](https://github.com/twentyhq/twenty/commit/d6c4ae9a7d86328445c2678888d58f918054d10e) | FelixMalfait |
| 2026-11-21 | [Remove the standard Helper agent (#31087)](https://github.com/twentyhq/twenty/commit/ee88618a008f351bde9cd75355ea6b969e2f239e) | FelixMalfait |
| 2026-11-21 | [i18n - translations (#31095)](https://github.com/twentyhq/twenty/commit/48a62c97f7bd52598229bd15ab4168decc7dcf73) | twenty-pr[bot] |
| 2026-11-21 | [Trim workspace and member names before saving them (#30984)](https://github.com/twentyhq/twenty/commit/b8a6050343cf941fc6a836c6ce736ae85c004825) | prastoin |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```
