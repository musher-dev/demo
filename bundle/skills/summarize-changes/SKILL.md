---
name: summarize-changes
version: 1.0.0
user-invocable: true
description: Summarize git history, staged diffs, or pull request changes into clear, human-readable summaries grouped by theme. Use when you need to understand what changed, generate a release summary, or explain recent work to stakeholders. Triggered by: summarize changes, what changed, summarize commits, summarize diff, change summary, release notes, what's new, summarize PR.
argument-hint: "[<commit-range>|<branch>|staged] [--format short|detailed|release]"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
---

# Summarize Changes

Produce a clear, human-readable summary of git changes grouped by theme (features, fixes, refactors, chores).

## Input

**Arguments:** `$ARGUMENTS`

Parse the arguments to determine scope and format:

- **Scope** (what to summarize):
  - A commit range like `HEAD~5..HEAD` or `v1.2.0..HEAD`
  - A branch name to compare against the current branch's base
  - The word `staged` to summarize only staged changes
  - Empty → default to all changes since the last tag, or the last 10 commits if no tags exist

- **Format** (`--format`):
  - `short` — one-line bullets per logical change
  - `detailed` — bullets with brief context for each change (default)
  - `release` — formatted as a release notes section with a header and categorized lists

---

## Phase 1: Discover What Changed

Run the appropriate git commands based on the scope:

**For a commit range or branch:**
```bash
git log <range> --oneline --no-merges
git diff <range> --stat
```

**For staged changes:**
```bash
git diff --cached --stat
git diff --cached
```

**For default (since last tag or last 10 commits):**
```bash
# Check if tags exist
git tag --sort=-version:refname | head -1

# If a tag exists, compare since that tag
git log <last-tag>..HEAD --oneline --no-merges
git diff <last-tag>..HEAD --stat

# If no tags, use last 10 commits
git log HEAD~10..HEAD --oneline --no-merges
git diff HEAD~10..HEAD --stat
```

---

## Phase 2: Analyze and Group

Read the commit messages and diff stats. Group changes into these categories (omit any empty category):

| Category | What belongs here |
|----------|------------------|
| ✨ Features | New functionality, additions, enhancements |
| 🐛 Bug Fixes | Defect corrections, error handling improvements |
| ♻️ Refactors | Code restructuring without behavior change |
| 📚 Documentation | README updates, inline comments, docs changes |
| 🧪 Tests | New or updated tests |
| 🔧 Chores | Dependency updates, CI config, build tooling |
| 🗑️ Removals | Deleted files, deprecated feature removal |

For each commit/change:
1. Determine the most appropriate category
2. Extract a concise description (drop implementation details, keep user-visible impact)
3. Note affected files or modules if relevant for `detailed` and `release` formats

---

## Phase 3: Generate the Summary

### Short format

```
✨ Features
- Added user authentication via OAuth2
- New dark mode toggle in settings

🐛 Bug Fixes
- Fixed race condition in cache invalidation

🔧 Chores
- Updated dependencies to latest versions
```

### Detailed format

```
✨ Features
- **OAuth2 authentication** — Users can now sign in with Google and GitHub (src/auth/)
- **Dark mode** — New theme toggle persisted to user preferences (src/ui/settings/)

🐛 Bug Fixes
- **Cache race condition** — Fixed concurrent write conflict in the Redis cache layer (src/cache/)

🔧 Chores
- Bumped all npm dependencies to latest patch versions
```

### Release format

```markdown
## What's Changed

### ✨ New Features
- Users can now sign in with Google and GitHub via OAuth2
- Dark mode is now available and persists across sessions

### 🐛 Bug Fixes
- Fixed a race condition in the Redis cache layer that could cause stale reads under high concurrency

### 🔧 Maintenance
- Updated all dependencies to latest patch versions
```

---

## Phase 4: Output

Print the formatted summary. If the scope was empty and you defaulted to a range, briefly note which range was used at the top:

> *Summarizing 10 commits (a1b2c3d → HEAD)*

End with a one-line count: `X files changed, Y insertions(+), Z deletions(-)` (from `git diff --stat`).

---

## Edge Cases

- **No changes found** → Print "No changes found in the specified scope." and stop.
- **Binary files only** → Note them as "Binary file changes" in the Chores section.
- **Merge commits** → Skip merge commits; summarize only the substantive commits.
- **Very large diffs (>500 files)** → Summarize by directory rather than by individual file.
