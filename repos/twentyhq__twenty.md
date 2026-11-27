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
| ⭐ **Stars** | 61.5k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [140](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [sdk/v2.64.1](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.64.1) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3278.5 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [sdk/v2.64.1](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.64.1)
<sub>2026-11-27 · today</sub>

> Two breaking changes complete the view-privacy migration. The `visibility` field is removed from the view schema on a 2.64 server. Queries that select or send it will fail; switch to `isPrivate`. App manifests are affected too: `defineView()` no longer accepts `visibility`, and `ViewVisibility` is no longer exported from `twenty-sdk/define`.
> Views and their child entities are now hard-deleted. Any query filtering on `deletedAt` for view types needs to be removed.
> Installing `twenty-client-sdk` no longer pulls `@genql/runtime` or the 15+ packages it depended on. AI-generated record-page widgets can now read the viewed record via `useSelectedRecordIds()` and `useSelectedObjectMetadata()`.
> **⚠️ Breaking changes**
> - Views and their child entities are hard-deleted from this release; remove any `deletedAt` filters or field selections on `view`, `viewField`, `viewFilter`, `viewFilterGroup`, `viewGroup`, and `viewSort` types. ([#31323](https://github.com/twentyhq/twenty/pull/31323)) by @Weiko
> - `visibility` is removed from the view schema on a 2.64 server; any GraphQL, REST, or `twenty-client-sdk` query that selects `visibility` or sends it on create/update will fail — use `isPrivate` instead, including when `__scalar: true` is used. ([#31460](https://github.com/twentyhq/twenty/pull/31460)) by @Weiko
> …

### [twenty/v2.64.1](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.64.1)
<sub>2026-11-27 · today</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Stop reading deletedAt on views and their children ([#31323](https://github.com/twentyhq/twenty/pull/31323)) by @Weiko
> - Enforce the privatable creator rule in the workspace migration builder ([#31438](https://github.com/twentyhq/twenty/pull/31438)) by @Weiko
> - [BREAKING_CHANGE] Remove the deprecated view visibility API and relax its column ([#31460](https://github.com/twentyhq/twenty/pull/31460)) by @Weiko
> - [BREAKING_CHANGE] Remove view visibility from app manifests ([#31548](https://github.com/twentyhq/twenty/pull/31548)) by @Weiko
> **✨ New features**
> …

### [twenty/v2.63.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.63.0)
<sub>2026-11-24 · 2d ago</sub>

> Table columns get three new shapes. A filtered one-to-many column shows related records narrowed by filter, sort, and limit. Summary columns aggregate those records per row: count, sum, or average. Columns can be renamed, and filtered columns can show a single field of their records instead of chips.
> WhatsApp arrives as a connected app. Members link by QR code, pick which conversations to import, and see messages sync to People. The call recorder gains per-member preferences: record all meetings, only internal, only external, or none — set from a new Recording page in settings.
> Two breaking changes: the workflow API drops `visibility` and `updateCoreWorkflowVisibility` — use `isPrivate` on `createCoreWorkflow` and `updateCoreWorkflow` instead. Inbox presence tracking replaces `updateFocusedTab` with `updateTabPresence`.
> **⚠️ Breaking changes**
> - Workflow triggers no longer read legacy workspaceWorkflowVersionId or lastPublishedVersionId. Integrations referencing those fields must switch to core IDs. ([#30744](https://github.com/twentyhq/twenty/pull/30744)) by @thomtrp
> - Inbox members now show as online while they have a Twenty tab open. The updateFocusedTab mutation is replaced by updateTabPresence. ([#30952](https://github.com/twentyhq/twenty/pull/30952)) by @etiennejouan
> …

### [sdk/v2.63.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.63.0)
<sub>2026-11-24 · 2d ago</sub>

> One breaking change: `updateFocusedTab` is removed. Switch to `updateTabPresence({ tabId, status })` where status is `'FOCUSED'` or `'OPEN'`. `twenty app build` is also fixed: it no longer crashes when a source file imports a `twenty-ui` export at module level.
> `twenty-sdk` gains a new `twenty-sdk/email` entry point exporting `isWorkEmail`, `isWorkDomain`, `getDomainFromEmail`, and the full provider list. Apps can now share the server's email classifier instead of maintaining their own.
> `ViewType.INBOX` and a `presetFilter` field land on view types. Provider references in `defineConnectionProvider` manifests now use flat identifiers; the object form is deprecated. `IconMessageHeart` is newly exported from `twenty-ui/icon` and select field options gain an optional `description`.
> **⚠️ Breaking changes**
> - `updateFocusedTab` is removed; switch to `updateTabPresence({ tabId, status })` where status is `'FOCUSED'` or `'OPEN'` ([#30952](https://github.com/twentyhq/twenty/pull/30952)) by @etiennejouan
> **🌟 Highlights**
> …

### [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0)
<sub>2026-11-23 · 4d ago</sub>

> This release fixes a sidebar regression that left non-admin members without the Applications permission unable to see standard navigation items. Companies, People, Opportunities, Tasks, Notes, Dashboards, and folders all disappeared when the customizable sidebar flag was disabled.
> No SDK exports, types, or CLI commands changed. Package consumers do not need to update their code.
> **🌟 Highlights**
> - Sidebar navigation items (Companies, People, Opportunities, Tasks, Notes, Dashboards) are now visible to members without the Applications permission when the customizable sidebar flag is off. ([#31179](https://github.com/twentyhq/twenty/pull/31179))
> **🐛 Bug fixes**
> - Fixes a bug where sidebar items (Companies, People, Opportunities, Tasks, Notes, Dashboards) were hidden for members lacking the Applications permission when the customizable sidebar flag is off — no SDK changes required. ([#31179](https://github.com/twentyhq/twenty/pull/31179)) by @thomtrp
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [Add the filter builder screen parts for conditional availability (#31…](https://github.com/twentyhq/twenty/commit/6e0c006aff99b92709d898150cdb46d0326c206e) | neo773 |
| 2026-11-27 | [Resolve inbox object names from the workspace flag on the frontend (#…](https://github.com/twentyhq/twenty/commit/f4e30168801e32df80a183f64e464cb2208cad95) | bosiraphael |
| 2026-11-27 | [Move the twenty-standard role removal command to 2.66 (#31725)](https://github.com/twentyhq/twenty/commit/bb8d806ade6adfeaf21d44fede72e8a6c14dfc76) | prastoin |
| 2026-11-27 | [Block the workspace menu while editing the layout (#31710)](https://github.com/twentyhq/twenty/commit/3688859a7a86cb88fb1e4da7343bb2cbe599901c) | Bonapara |
| 2026-11-27 | [Shape table loading skeletons like their rows (#31714)](https://github.com/twentyhq/twenty/commit/f42d68ad4d484117e5cd0202102bf6b1de73601c) | FelixMalfait |
| 2026-11-27 | [i18n - translations (#31720)](https://github.com/twentyhq/twenty/commit/95d9c8cbc1a00a8b9810ea6ccff06498ef31df22) | twenty-pr[bot] |
| 2026-11-27 | [Group what a conditional evaluation rule can use by metadata name (#3…](https://github.com/twentyhq/twenty/commit/0224843d3b6f155d0b208aefb38b73d4104d5650) | neo773 |
| 2026-11-27 | [fix(cli): trust system certificate authorities (#31705)](https://github.com/twentyhq/twenty/commit/be7977ad6c46e058a74e130a7ef11498aa4f4a57) | FelixMalfait |
| 2026-11-27 | [Keep zod out of app bundles that use twenty-ui data-display (#31706)](https://github.com/twentyhq/twenty/commit/a7b5917a43594217dc20574e1ecada85617e3835) | ehconitin |
| 2026-11-27 | [Nullify twenty-standard app `requestRoleId` and remove its granted ro…](https://github.com/twentyhq/twenty/commit/196f73f67cb4897d3fa6cdda06b5bbd22ca504ed) | prastoin |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```
