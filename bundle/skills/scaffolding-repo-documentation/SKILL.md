---
name: scaffolding-repo-documentation
version: 1.0.0
user-invocable: true
description: Create missing documentation files based on audit results or a direct request. Uses repository context to generate tailored content. Never overwrites existing files. Use when scaffolding docs, creating community health files, or filling documentation gaps after an audit. Triggered by: scaffold docs, create docs, missing documentation, generate community files, docs gaps.
argument-hint: "[path/to/repo] [--files FILE1,FILE2,...] [--all]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - Skill
---

# Scaffold Repository Documentation

Create missing community-health and onboarding documentation files, tailored to the repository's language, framework, and existing content.

## Input

**Arguments:** `$ARGUMENTS`

- **Path** — Repository root to scaffold into. Defaults to the current working directory.
- **`--files`** — Comma-separated list of specific files to create.
- **`--all`** — Create all missing files from the checklist.
- If neither flag is provided, create all files flagged as High or Medium priority.

## Phase 1 — Assess Current State

Check which documentation files already exist. Use the checklist in `references/docs-checklist.md` (bundled alongside this skill) as the canonical list.

If the `auditing-repo-documentation` skill was invoked earlier in this conversation, reuse its findings instead of re-scanning.

## Phase 2 — Gather Repository Context

Collect signals that inform generated content:

1. **Language and framework** — Check `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.
2. **Project name** — From the manifest, directory name, or first heading in an existing README.
3. **License** — From LICENSE file or package manifest.
4. **Existing README** — Extract useful context if present.
5. **GitHub expectations** — Reference `references/github-community-profile.md` (bundled alongside this skill).

## Phase 3 — Generate Missing Files

For each file to be created:

1. **Confirm it does not already exist.** Never overwrite.
2. **Generate content** tailored to the repository context from Phase 2.
3. **Delegate to specialist skills when available:**
   - For `README.md` → invoke the `writing-readme` skill
   - For `SECURITY.md` → invoke the `writing-security-policy` skill
4. **For other files**, generate directly using the guidance below.

### CONTRIBUTING.md
Sections: How to Contribute (fork/branch/PR workflow), Development Setup (language-appropriate commands), Code Style (reference linter config if present), Pull Request Process, Reporting Issues.

### CODE_OF_CONDUCT.md
Adopt the Contributor Covenant v2.1. Use `[INSERT CONTACT METHOD]` as a TODO placeholder for the enforcement contact.

### CHANGELOG.md
Skeleton following Keep a Changelog format with an `[Unreleased]` section.

### CODEOWNERS
Generate based on directory structure with placeholder team names (`@org/maintainers`).

### .github/PULL_REQUEST_TEMPLATE.md
Structured template: Summary, Type of Change (checkboxes), Testing, Checklist.

### .github/ISSUE_TEMPLATE/bug_report.md
YAML frontmatter + sections: Description, Steps to Reproduce, Expected/Actual Behavior, Environment.

### .github/ISSUE_TEMPLATE/feature_request.md
YAML frontmatter + sections: Problem Statement, Proposed Solution, Alternatives, Additional Context.

## Phase 4 — Output

Print a summary:

```
## Scaffolding Report

**Repository:** <name>

### Files Created
- ✅ CONTRIBUTING.md
- ✅ SECURITY.md (via writing-security-policy skill)

### Files Skipped (already exist)
- ⏭️ README.md
- ⏭️ LICENSE

### TODO Items
- CODE_OF_CONDUCT.md: Replace `[INSERT CONTACT METHOD]` with an enforcement email
- CODEOWNERS: Replace `@org/maintainers` with actual GitHub team handles
```

## Safety Rules

- **NEVER overwrite an existing file.** Skip and note in report.
- **NEVER generate LICENSE files.** License selection is a legal decision — flag it only.
- **ALWAYS use TODO markers** for content requiring human judgment.
- **Create parent directories** (e.g. `.github/ISSUE_TEMPLATE/`) as needed.
