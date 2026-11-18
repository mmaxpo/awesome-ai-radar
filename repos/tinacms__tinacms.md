# tinacms/tinacms

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/tinacms/tinacms)

> TinaCMS is the leading open-source headless CMS that supports Markdown and Visual Editing. Your content is stored in your own GitHub repo 🦙 ❤️

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Open-source headless CMS on top of Git |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 13.9k |
| 🍴 **Forks** | 773 |
| 🐞 **Open issues + PRs** | [499](https://github.com/tinacms/tinacms/issues) |
| 💻 **Languages** | TypeScript 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `cms` `nextjs` `react` `content-management-system` `tinacms` `markdown` `typescript` `tina` `forestry` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2019-07-23 |
| 📦 **Latest release** | [tinacms@3.15.2](https://github.com/tinacms/tinacms/releases/tag/tinacms%403.15.2) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 922.3 MB |
| 🌐 **Website** | https://tina.io |

## 📦 Recent releases

### [tinacms@3.15.2](https://github.com/tinacms/tinacms/releases/tag/tinacms%403.15.2)
<sub>2026-11-09 · 9d ago</sub>

> **Patch Changes**
> - [#7994](https://github.com/tinacms/tinacms/pull/7994) [`c91c528`](https://github.com/tinacms/tinacms/commit/c91c528f51171ee8a5955831738c2ece5ef8bed2) Thanks [@Tyagiquamar](https://github.com/Tyagiquamar)! - Focus the reference field combobox when visual editing selects it. The reference field ignored `experimental_focusIntent`, so clicking a reference in the preview opened the sidebar without focusing anything.

### [@tinacms/cli@4.0.5](https://github.com/tinacms/tinacms/releases/tag/%40tinacms/cli%404.0.5)
<sub>2026-11-09 · 9d ago</sub>

> **Patch Changes**
> - [#8019](https://github.com/tinacms/tinacms/pull/8019) [`a547b2f`](https://github.com/tinacms/tinacms/commit/a547b2f77b2b4807a4d4fb5feb1a9ecb73c046d1) Thanks [@joshbermanssw](https://github.com/joshbermanssw)! - Cap Rollup's `maxParallelFileOps` at 100 in the production admin build, so `tinacms build` no longer fails with `EMFILE: too many open files` on hosts with a 1024 open-file limit, such as Cloudflare Workers Builds.
> - [#7966](https://github.com/tinacms/tinacms/pull/7966) [`96196d6`](https://github.com/tinacms/tinacms/commit/96196d6056bb61571088a3ca63680b4c2e2d12e8) Thanks [@Spence1115](https://github.com/Spence1115)! - Move `@graphql-tools/load` to 8.1.21 and `@graphql-tools/graphql-file-loader` to 8.1.24, so the CLI no longer pulls in `@graphql-tools/utils` 9.2.1, which is affected by GHSA-7mx3-vvmw-hjmv (prototype pollution in `mergeDeep`).
> - Updated dependencies [[`c91c528`](https://github.com/tinacms/tinacms/commit/c91c528f51171ee8a5955831738c2ece5ef8bed2)]:
>   - tinacms@3.15.2

### [tinacms@3.15.1](https://github.com/tinacms/tinacms/releases/tag/tinacms%403.15.1)
<sub>2026-11-01 · 16d ago</sub>

> **Patch Changes**
> - [`124567b`](https://github.com/tinacms/tinacms/commit/124567b2e75e0f00b8d040d096532d8c6176f08f) Thanks [@Tyagiquamar](https://github.com/Tyagiquamar)! - Fix empty, index-less active field group when clicking a tinaField targeting an object list with fields.
> - [#7923](https://github.com/tinacms/tinacms/pull/7923) [`a3d56c0`](https://github.com/tinacms/tinacms/commit/a3d56c0272f967b3f7d5bef2143ca12a1b9b17ed) Thanks [@RaphaelFakhri](https://github.com/RaphaelFakhri)! - Validate `required` on string list fields that use `ui.component: 'tags'`. The tags field plugin had no `validate` function, so a required tags field showed no "Required" error and the document saved with no tags. The field now reports "Required" when it holds no tags.
> - Updated dependencies [[`80502f8`](https://github.com/tinacms/tinacms/commit/80502f86b0224fb67ec05f0644db71bf5d38fde4), [`19285c6`](https://github.com/tinacms/tinacms/commit/19285c6deeee52c380e8b2fdeafedc9530dc0618)]:
>   - @tinacms/mdx@2.4.2

### [@tinacms/mdx@2.4.2](https://github.com/tinacms/tinacms/releases/tag/%40tinacms/mdx%402.4.2)
<sub>2026-11-01 · 16d ago</sub>

> **Patch Changes**
> - [#7951](https://github.com/tinacms/tinacms/pull/7951) [`80502f8`](https://github.com/tinacms/tinacms/commit/80502f86b0224fb67ec05f0644db71bf5d38fde4) Thanks [@joshbermanssw](https://github.com/joshbermanssw)! - Fix saving a rich-text field that contains an empty bullet.
> - [#7958](https://github.com/tinacms/tinacms/pull/7958) [`19285c6`](https://github.com/tinacms/tinacms/commit/19285c6deeee52c380e8b2fdeafedc9530dc0618) Thanks [@wicksipedia](https://github.com/wicksipedia)! - Rich-text component values that contain a quote, backslash or newline now save and load back unchanged. Tina writes each value in a string, datetime, reference or image list as a JSON string literal. Values without those characters stay exactly as before.
>   Negative numbers and image lists on rich-text components now load back. Before, a negative number turned the block into invalid markdown, and an image list failed to load.
>   Number and boolean values must be real numbers or booleans. If one is not, the save fails with a message that names the field. If you clear a number field, Tina saves it as `null`. Tina drops a highlight colour that contains characters a CSS colour cannot have, and the text stays highlighted.

### [@tinacms/mdx@2.4.1](https://github.com/tinacms/tinacms/releases/tag/%40tinacms/mdx%402.4.1)
<sub>2026-10-27 · 22d ago</sub>

> **Patch Changes**
> - [#7319](https://github.com/tinacms/tinacms/pull/7319) [`40cf662`](https://github.com/tinacms/tinacms/commit/40cf6628da02f81bd0cb5994a3ed78b71cba699a) Thanks [@Osamaali313](https://github.com/Osamaali313)! - Fix a crash when parsing rich-text containing an `image` field with `list: true`. The image-list branch called `.split(',')` on the array returned by `extractScalar`, throwing `TypeError: values.split is not a function`; the error was wrapped as a parse failure, so the block became an `invalid_markdown` node (content dropped in the editor) or failed `tinacms build`. It now maps over the array like the other list field types.
> - [#7861](https://github.com/tinacms/tinacms/pull/7861) [`33bb5f3`](https://github.com/tinacms/tinacms/commit/33bb5f3a1e0c178fac0d9b8c8547fd0a2e4cee9d) Thanks [@Deea222](https://github.com/Deea222)! - A rich-text field holding two lists of the same kind in a row now reopens after it is saved. The MDX serializer separated such lists with an HTML comment (`<!---->`), which MDX does not allow, so the whole document fell back to raw text on the next load. It now switches the list marker instead: `*` then `-`, `1.` then `1)`. Files already saved with the comment are not rewritten; remove the `<!---->` line by hand once. Fixes #5238.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(tinacms): recover the login modal when the TinaCloud token exchan…](https://github.com/tinacms/tinacms/commit/f2142226dad67327afb991af8ee8c9e3cccb1817) | wicksipedia |
| 2026-11-16 | [feat(v4): browse a collection's documents in a table with folders and…](https://github.com/tinacms/tinacms/commit/87860ba11070b3ba004e14fc5d1c6e142f4290c8) | joshbermanssw |
| 2026-11-16 | [feat(v4): search through TinaCloud with tinaCloud({ search }) (#8057)](https://github.com/tinacms/tinacms/commit/e1f226455d573b4415062aba33bcd62379f95f1a) | joshbermanssw |
| 2026-11-16 | [fix(tinacms): recover when creating a branch fails in the branch swit…](https://github.com/tinacms/tinacms/commit/04635762a184ae3ae5242828145d24f19c873a45) | officialasishkumar |
| 2026-11-16 | [fix(cli): wait for the datalayer server to listen before connecting (…](https://github.com/tinacms/tinacms/commit/995d1dc9b5917ea763aa865f62d0e53e8ed4e5c7) | officialasishkumar |
| 2026-11-15 | [fix(graphql): index an unquoted date in a string field (#8023)](https://github.com/tinacms/tinacms/commit/f4e222ad0ef301ac83342e5096d7f53e701a3472) | officialasishkumar |
| 2026-11-15 | [fix(graphql): build index key range when eq filters cover leading fie…](https://github.com/tinacms/tinacms/commit/f5a5746094071ed46d6865fba9a92d05fc92b697) | PranjalGoyal06 |
| 2026-11-15 | [fix(tinacms): clear the preview URL poll on unmount (#8010)](https://github.com/tinacms/tinacms/commit/d58251fe0e641ecc28c7a444a0f934c3a1de4344) | sarahanntolsma-ff |
| 2026-11-15 | [fix(v4): keep the barebones config loader open so server hooks can sa…](https://github.com/tinacms/tinacms/commit/a43bc9011251db370c61ffa0fbd7479d5c37cd4c) | joshbermanssw |
| 2026-11-12 | [feat(v4): upload to Media with progress, cancel and retry (#8040)](https://github.com/tinacms/tinacms/commit/64e3517ec2959ca11484c35799c4f6eee2056acb) | joshbermanssw |

[See all commits ↗](https://github.com/tinacms/tinacms/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tinacms/tinacms.git
```
