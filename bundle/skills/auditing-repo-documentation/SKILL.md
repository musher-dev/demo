---
name: auditing-repo-documentation
version: 1.0.0
user-invocable: true
description: Scan a repository and score its documentation health against community-health and onboarding best practices. Use when assessing documentation quality, checking repo health, or identifying missing docs. Triggered by: audit docs, documentation health, repo score, docs review, community health check.
argument-hint: "[path/to/repo]"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Glob
---

# Audit Repository Documentation

Scan a repository and produce a weighted documentation-health score with actionable gap analysis.

## Input

**Arguments:** `$ARGUMENTS`

- If a path is provided, audit that directory as the repository root.
- If empty, use the current working directory.

## Phase 1 — Discover Repository Context

Gather context that informs scoring and recommendations:

1. Detect the primary language and framework from manifest files (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.).
2. List existing documentation files at the repo root and under `.github/`.
3. Note any `docs/` directory or existing documentation infrastructure.

If the directory is not a git repository, skip git-specific checks and focus on file-presence auditing.

## Phase 2 — Score Each Documentation File

Use the scoring rubric in `references/scoring-rubric.md` (bundled alongside this skill). For each file listed in the rubric:

1. **Check existence** — Does the file exist at the expected path (including common variants)?
2. **Check content quality** — If it exists, read it and assess against the rubric's quality criteria.
3. **Assign a score** — 0 (missing), 1 (poor/stub), 2 (adequate), 3 (good).
4. **Apply the weight** — Multiply the score by the rubric weight for that file.

## Phase 3 — Calculate Overall Score

```
overall_score = sum(weighted_scores) / sum(max_possible_weighted_scores) * 100
```

Round to the nearest integer. Map to a grade:

| Score | Grade | Label |
|-------|-------|-------|
| 90–100 | A | Excellent |
| 75–89  | B | Good |
| 50–74  | C | Needs Improvement |
| 25–49  | D | Poor |
| 0–24   | F | Critical |

## Phase 4 — Prioritize Gaps

Sort missing or inadequate files by:

1. **Severity** — High (weight ≥ 5), Medium (weight 3), Low (weight ≤ 2)
2. **Impact** — Files that block contributors rank above internal-only docs

For each gap, provide:

- File name and expected path
- Why it matters (one sentence)
- Suggested next step (e.g. "Use the `scaffolding-repo-documentation` skill to create this file")

## Phase 5 — Output

Present the assessment:

```
## Documentation Health Report

**Repository:** <repo name or path>
**Overall Score:** <score>/100 (<grade>)
**Primary Language:** <detected language>

### Per-File Scores

| File | Status | Score | Weight | Weighted |
|------|--------|-------|--------|----------|
| README.md | ✅ Good | 3/3 | ×5 | 15/15 |
| CONTRIBUTING.md | ❌ Missing | 0/3 | ×3 | 0/9 |
| ... | ... | ... | ... | ... |

### High Priority Gaps
1. **CONTRIBUTING.md** (weight: 3) — No contributor guide.
   → Use the `scaffolding-repo-documentation` skill to create this file.

### Summary
<2–3 sentence summary of the repo's documentation posture and the most impactful next steps.>
```

## Edge Cases

- **Empty README** — A README with only a heading or fewer than 50 characters scores 1, not 2.
- **Non-GitHub hosting** — If `.github/` does not exist, skip GitHub-specific files but note them.
- **Monorepo** — Score only the root-level docs. Note that sub-packages may need their own READMEs.
