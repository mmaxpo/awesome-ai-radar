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
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [148](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [sdk/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.59.0) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3042.8 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [sdk/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.59.0)
<sub>2026-11-16 · 5d ago</sub>

> **✨ New features**
> - feat(cli): pull public application assets ([#30275](https://github.com/twentyhq/twenty/pull/30275)) by @Weiko
> - feat(cli): export workspace records to CSV ([#30279](https://github.com/twentyhq/twenty/pull/30279)) by @Weiko
> - feat(cli): preserve imported application sources in builds ([#30281](https://github.com/twentyhq/twenty/pull/30281)) by @Weiko
> - feat(cli): send proxy headers to servers behind authenticating proxies ([#30310](https://github.com/twentyhq/twenty/pull/30310)) by @FelixMalfait
> **💅 Improvements & UX**
> …

### [twenty/v2.59.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.59.0)
<sub>2026-11-16 · 5d ago</sub>

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
<sub>2026-11-09 · 12d ago</sub>

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
| 2026-11-22 | [i18n - translations (#31141)](https://github.com/twentyhq/twenty/commit/b83122a7cc112703807546f5b830b7e3ba862edb) | twenty-pr[bot] |
| 2026-11-22 | [Leave message attachments out of role wide access and individual role…](https://github.com/twentyhq/twenty/commit/9cee6f100e32b70e2aaf6189d7c809406da3b892) | charlesBochet |
| 2026-11-22 | [Name AI chat and inbox code after what it is (#31139)](https://github.com/twentyhq/twenty/commit/d4578e4a3492d0afa763d9b1214cbd29279ee850) | charlesBochet |
| 2026-11-22 | [Look up walled and one-to-many access group rules by value (#31135)](https://github.com/twentyhq/twenty/commit/fe2e676f952fd22e397856e868520733e66d6f97) | charlesBochet |
| 2026-11-22 | [Add a command revoking role wide access to channel objects where chan…](https://github.com/twentyhq/twenty/commit/fc01ecf6b928954c90395a74fc25d816b350c7da) | charlesBochet |
| 2026-11-22 | [Share duplicated AI chat and inbox logic in helpers (#31137)](https://github.com/twentyhq/twenty/commit/1975701b78c26a0b007cc1f2e46c5f9238f4159c) | charlesBochet |
| 2026-11-22 | [Mark unreadable columns that show the restricted placeholder instead …](https://github.com/twentyhq/twenty/commit/fa5e12dc79f474f4133fbdd6fa8517c8466bfd24) | charlesBochet |
| 2026-11-22 | [i18n - translations (#31138)](https://github.com/twentyhq/twenty/commit/94f8941f696fb1d9df9468ba372cc4640b830d01) | twenty-pr[bot] |
| 2026-11-22 | [Reach message and calendar records through channel visibility rules b…](https://github.com/twentyhq/twenty/commit/cc90c95e40e0e1deb7a3b20b6de7af7b0cbf45b8) | charlesBochet |
| 2026-11-22 | [Delete and trim low-value AI front-end tests (#31134)](https://github.com/twentyhq/twenty/commit/e08883f50f3ad29c65b7fac8592f78be99054204) | charlesBochet |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```
