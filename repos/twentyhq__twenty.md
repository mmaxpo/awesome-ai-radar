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
| 🐞 **Open issues + PRs** | [122](https://github.com/twentyhq/twenty/issues) |
| 💻 **Languages** | TypeScript 82% · MDX 16% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `crm` `customer` `graphql` `marketing` `react` `sales` `typescript` `crm-system` `nestjs` `reactjs` `web` `monorepo` `open-source` `postgresql` `good-first-issue` `hacktoberfest` `javascript` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2022-12-01 |
| 📦 **Latest release** | [twenty/v2.63.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.63.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3195.2 MB |
| 🌐 **Website** | https://twenty.com |

## 📦 Recent releases

### [twenty/v2.63.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.63.0)
<sub>2026-11-24 · today</sub>

> Table columns get three new shapes. A filtered one-to-many column shows related records narrowed by filter, sort, and limit. Summary columns aggregate those records per row: count, sum, or average. Columns can be renamed, and filtered columns can show a single field of their records instead of chips.
> WhatsApp arrives as a connected app. Members link by QR code, pick which conversations to import, and see messages sync to People. The call recorder gains per-member preferences: record all meetings, only internal, only external, or none — set from a new Recording page in settings.
> Two breaking changes: the workflow API drops `visibility` and `updateCoreWorkflowVisibility` — use `isPrivate` on `createCoreWorkflow` and `updateCoreWorkflow` instead. Inbox presence tracking replaces `updateFocusedTab` with `updateTabPresence`.
> **⚠️ Breaking changes**
> - Workflow triggers no longer read legacy workspaceWorkflowVersionId or lastPublishedVersionId. Integrations referencing those fields must switch to core IDs. ([#30744](https://github.com/twentyhq/twenty/pull/30744)) by @thomtrp
> - Inbox members now show as online while they have a Twenty tab open. The updateFocusedTab mutation is replaced by updateTabPresence. ([#30952](https://github.com/twentyhq/twenty/pull/30952)) by @etiennejouan
> …

### [sdk/v2.63.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.63.0)
<sub>2026-11-24 · today</sub>

> One breaking change: `updateFocusedTab` is removed. Switch to `updateTabPresence({ tabId, status })` where status is `'FOCUSED'` or `'OPEN'`. `twenty app build` is also fixed: it no longer crashes when a source file imports a `twenty-ui` export at module level.
> `twenty-sdk` gains a new `twenty-sdk/email` entry point exporting `isWorkEmail`, `isWorkDomain`, `getDomainFromEmail`, and the full provider list. Apps can now share the server's email classifier instead of maintaining their own.
> `ViewType.INBOX` and a `presetFilter` field land on view types. Provider references in `defineConnectionProvider` manifests now use flat identifiers; the object form is deprecated. `IconMessageHeart` is newly exported from `twenty-ui/icon` and select field options gain an optional `description`.
> **⚠️ Breaking changes**
> - `updateFocusedTab` is removed; switch to `updateTabPresence({ tabId, status })` where status is `'FOCUSED'` or `'OPEN'` ([#30952](https://github.com/twentyhq/twenty/pull/30952)) by @etiennejouan
> **🌟 Highlights**
> …

### [sdk/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/sdk/v2.62.0)
<sub>2026-11-23 · 2d ago</sub>

> This release fixes a sidebar regression that left non-admin members without the Applications permission unable to see standard navigation items. Companies, People, Opportunities, Tasks, Notes, Dashboards, and folders all disappeared when the customizable sidebar flag was disabled.
> No SDK exports, types, or CLI commands changed. Package consumers do not need to update their code.
> **🌟 Highlights**
> - Sidebar navigation items (Companies, People, Opportunities, Tasks, Notes, Dashboards) are now visible to members without the Applications permission when the customizable sidebar flag is off. ([#31179](https://github.com/twentyhq/twenty/pull/31179))
> **🐛 Bug fixes**
> - Fixes a bug where sidebar items (Companies, People, Opportunities, Tasks, Notes, Dashboards) were hidden for members lacking the Applications permission when the customizable sidebar flag is off — no SDK changes required. ([#31179](https://github.com/twentyhq/twenty/pull/31179)) by @thomtrp
> …

### [twenty/v2.62.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.62.0)
<sub>2026-11-23 · 2d ago</sub>

> The `NOT_STARTED` workflow run status is removed in this release. The upgrade command converts any runs in that state to `ENQUEUED` automatically. Update any custom integrations, filters, or views that reference `NOT_STARTED` before upgrading.
> A regression from 2.61 is fixed for team members without the Applications permission. Those members were seeing an empty sidebar — Companies, People, Opportunities, Tasks, Notes, and Dashboards all gone. Navigation is restored for those roles.
> Emoji reactions now work in direct messages. Email thread panels no longer break when channel visibility is enabled. Internally, workflow privacy moves from a visibility enum to a boolean flag; the old column stays this release and is dropped in 2.63.
> **⚠️ Breaking changes**
> - The NOT_STARTED workflow run status is removed. The upgrade converts existing NOT_STARTED runs to ENQUEUED. Update any integrations, filters, or views that reference NOT_STARTED before upgrading. ([#31154](https://github.com/twentyhq/twenty/pull/31154)) by @charlesBochet
> **🌟 Highlights**
> …

### [twenty/v2.61.0](https://github.com/twentyhq/twenty/releases/tag/twenty/v2.61.0)
<sub>2026-11-22 · 2d ago</sub>

> **⚠️ Breaking changes**
> - [BREAKING_CHANGE] Show member health checks in Apps preferences ([#29242](https://github.com/twentyhq/twenty/pull/29242)) by @ehconitin
> - [BREAKING_CHANGE] Upsert row-level permission rules instead of a predicate tree ([#30252](https://github.com/twentyhq/twenty/pull/30252)) by @charlesBochet
> - Import recurring Google Calendar meetings only up to 90 days ahead ([#30335](https://github.com/twentyhq/twenty/pull/30335)) by @neo773
> - [BREAKING_CHANGE] Add a 2.60 command that drops the workspace workflowVersion object ([#30500](https://github.com/twentyhq/twenty/pull/30500)) by @thomtrp
> - [BREAKING_CHANGE] Add generic date functions to validation rules ([#30527](https://github.com/twentyhq/twenty/pull/30527)) by @FelixMalfait
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Generate SDK client for soft-deleted workspaces (#31453)](https://github.com/twentyhq/twenty/commit/a5e0443bc525754752ace0be0164ac0dafbb5977) | martmull |
| 2026-11-25 | [Add cron spreadMs, enqueueJobs limiter and job scheduledAt (#31383)](https://github.com/twentyhq/twenty/commit/736314729b98e27f7d667dfe5c50b5f42c78eb8a) | martmull |
| 2026-11-25 | [Enforce the privatable creator rule in the workspace migration builde…](https://github.com/twentyhq/twenty/commit/f5b37bd7798eb0eec581d35063b95c103b3b07ce) | Weiko |
| 2026-11-25 | [i18n - translations (#31454)](https://github.com/twentyhq/twenty/commit/577d2dfc69f5e151bc2eec09cc899728319eebc1) | twenty-pr[bot] |
| 2026-11-25 | [Address remaining review comments on the billing apps section (#31451)](https://github.com/twentyhq/twenty/commit/393ec0c330ec2b8ee2c5968ccc70a7d4bc3799a8) | martmull |
| 2026-11-25 | [Show the billing email in Billing settings and unify settings text li…](https://github.com/twentyhq/twenty/commit/93c4a7428b044c6fd2acbcc9052fa369347bd273) | Bonapara |
| 2026-11-25 | [i18n - translations (#31450)](https://github.com/twentyhq/twenty/commit/9df9d803e7c6d4c5a4be83258ecc87c6c940f3a8) | twenty-pr[bot] |
| 2026-11-25 | [Offer Add item only inside sidebar sections (#31448)](https://github.com/twentyhq/twenty/commit/15d9103759c30a8eedf4ce1540bad6bfefaab3c9) | thomtrp |
| 2026-11-25 | [Add apps section to billing settings page (#31435)](https://github.com/twentyhq/twenty/commit/6f1a32bb86093c366bf67279612a8cae334cab7f) | martmull |
| 2026-11-25 | [Hide the drop line where a sidebar drop would be refused (#31441)](https://github.com/twentyhq/twenty/commit/e1a00637df417c60f7c58bb88b53fb2fa35a2c4e) | thomtrp |

[See all commits ↗](https://github.com/twentyhq/twenty/commits)

## ⬇️ Get it

```bash
git clone https://github.com/twentyhq/twenty.git
```
