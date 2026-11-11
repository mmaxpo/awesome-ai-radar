# casey/just

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/casey/just)

> 🤖 Just a command runner

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | Handy command runner: a simpler Makefile for project tasks |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 36.7k |
| 🍴 **Forks** | 871 |
| 🐞 **Open issues + PRs** | [172](https://github.com/casey/just/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | CC0-1.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2016-06-17 |
| 📦 **Latest release** | [1.59.0](https://github.com/casey/just/releases/tag/1.59.0) — 2026-10-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 17.7 MB |
| 🌐 **Website** | https://just.systems |

## 📦 Recent releases

### [1.59.0](https://github.com/casey/just/releases/tag/1.59.0)
<sub>2026-10-15 · 27d ago</sub>

> **Breaking**
> - Require unicode paths ([#3708](https://github.com/casey/just/pull/3708) by [casey](https://github.com/casey))
> **Added**
> - Allow `--working-directory` without `--justfile` ([#3720](https://github.com/casey/just/pull/3720) by [casey](https://github.com/casey))
> - Allow `--usage` with module path to show usage for all recipes in module ([#3718](https://github.com/casey/just/pull/3718) by [casey](https://github.com/casey))
> - Add `[cache(environment)]` to add and remove variables from cache key ([#3696](https://github.com/casey/just/pull/3696) by [casey](https://github.com/casey))
> …

### [1.58.0](https://github.com/casey/just/releases/tag/1.58.0)
<sub>2026-08-03 · 3mo ago</sub>

> **Changed**
> - Surround interoplation expressions with spaces when formatting ([#3685](https://github.com/casey/just/pull/3685) by [casey](https://github.com/casey))
> - Accept multiple `,`-separated values in `--justfile-name` ([#3676](https://github.com/casey/just/pull/3676) by [casey](https://github.com/casey))
> **Added**
> - Add format argument to `[timestamp]` attribute ([#3681](https://github.com/casey/just/pull/3681) by [casey](https://github.com/casey))
> - Add `[timestamp]` recipe attribute ([#3680](https://github.com/casey/just/pull/3680) by [casey](https://github.com/casey))
> …

### [1.57.0](https://github.com/casey/just/releases/tag/1.57.0)
<sub>2026-07-19 · 3mo ago</sub>

> **Changed**
> - Pass arguments to `cmd.exe` without escaping ([#3636](https://github.com/casey/just/pull/3636) by [casey](https://github.com/casey))
> - `split('')` splits into characters ([#3650](https://github.com/casey/just/pull/3650) by [casey](https://github.com/casey))
> - Accept markdown justfiles found by name ([#3648](https://github.com/casey/just/pull/3648) by [casey](https://github.com/casey))
> - Make `[env]` variables visible to `shell()` invocations ([#3631](https://github.com/casey/just/pull/3631) by [casey](https://github.com/casey))
> - Forbid duplicate groups ([#3626](https://github.com/casey/just/pull/3626) by [casey](https://github.com/casey))
> …

### [1.56.0](https://github.com/casey/just/releases/tag/1.56.0)
<sub>2026-07-10 · 4mo ago</sub>

> **Fixed**
> - Omit authorization header in install script if GITHUB_TOKEN is empty ([#3595](https://github.com/casey/just/pull/3595) by [casey](https://github.com/casey))
> - Evaluate assignments in dependency order ([#3591](https://github.com/casey/just/pull/3591) by [casey](https://github.com/casey))
> - Do not run `shell()` commands during dry run ([#3588](https://github.com/casey/just/pull/3588) by [casey](https://github.com/casey))
> - List aliases for recipes in other modules ([#3581](https://github.com/casey/just/pull/3581) by [casey](https://github.com/casey))
> - Don't unindent format strings twice ([#3579](https://github.com/casey/just/pull/3579) by [casey](https://github.com/casey))
> …

### [1.55.1](https://github.com/casey/just/releases/tag/1.55.1)
<sub>2026-06-30 · 4mo ago</sub>

> **Fixed**
> - Fix panic when empty path is passed to `--show` and `--usage` ([#3511](https://github.com/casey/just/pull/3511) by [casey](https://github.com/casey))
> **Misc**
> - Upgrade sha2 to 0.11.0 ([#3512](https://github.com/casey/just/pull/3512) by [casey](https://github.com/casey))
> - Remove `Test::test_round_trip()` ([#3509](https://github.com/casey/just/pull/3509) by [casey](https://github.com/casey))
> - Remove round-trip testing ([#3508](https://github.com/casey/just/pull/3508) by [casey](https://github.com/casey))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [Preserve trailing comments on attributes (#3776)](https://github.com/casey/just/commit/2f9dfaec10fb6125931e830a748a544f158dc206) | casey |
| 2026-11-11 | [Preserve trailing comments on recipes (#3775)](https://github.com/casey/just/commit/dc13f8b277f9e18bc75df0a20397c3c2c3e6e7e7) | casey |
| 2026-11-02 | [Various refactors (#3768)](https://github.com/casey/just/commit/7b7b51bec9359a5b4a76321018db65d07978fecc) | casey |
| 2026-11-02 | [Move caching into `Recipe::cache_status()` (#3767)](https://github.com/casey/just/commit/57979da6e3d64a127624bcef7e8bd117d3621e97) | casey |
| 2026-11-02 | [Store output paths on cache lock (#3766)](https://github.com/casey/just/commit/2bbf063fd856f3efab5ec4c081dccd4301f4940f) | casey |
| 2026-11-02 | [Serialize BLAKE3 hashes as hexadecimal (#3765)](https://github.com/casey/just/commit/a4d9c9afe797406dab271ff1f6041183d2d8dc14) | casey |
| 2026-11-02 | [Add more `filesystem` functions (#3764)](https://github.com/casey/just/commit/da59fed7d5db8c01055f32817ace383b6daf5379) | casey |
| 2026-11-02 | [Invalidate cache when outputs are modified (#3763)](https://github.com/casey/just/commit/25cfed9c145653f7cda2e177ce6717d7298c50b7) | casey |
| 2026-11-01 | [Add `set dry-run` (#3754)](https://github.com/casey/just/commit/a7f66ae51877287addb383690a5c58e90d82ddf9) | casey |
| 2026-10-27 | [Add example using `eager` keyword to readme (#3761)](https://github.com/casey/just/commit/c7317c85c21ebd83ea4bb8de26f8afec44c7e597) | casey |

[See all commits ↗](https://github.com/casey/just/commits)

## ⬇️ Get it

```bash
git clone https://github.com/casey/just.git
```
