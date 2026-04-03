---
name: writing-security-policy
version: 1.0.0
user-invocable: true
description: Generate a SECURITY.md with supported versions, vulnerability reporting instructions, and disclosure policy. Use when a repository needs a security policy, vulnerability reporting process, or disclosure guidelines. Triggered by: write security policy, generate security.md, vulnerability reporting, security disclosure, missing security policy.
argument-hint: "[path/to/repo]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
---

# Write Security Policy

Generate a comprehensive SECURITY.md tailored to the repository's release model and ecosystem.

## Input

**Arguments:** `$ARGUMENTS`

- If a path is provided, write SECURITY.md into that directory.
- If empty, use the current working directory.
- If SECURITY.md already exists, warn and stop. Do not overwrite security policies.

## Phase 1 — Gather Context

1. **Existing security files** — Check for `SECURITY*`, `.github/SECURITY*`.
2. **Versioning strategy** — Inspect git tags (if available) and package manifest versions.
3. **Language ecosystem** — Determines which advisory databases to reference.
4. **Security tooling** — Note any CodeQL, Snyk, or Trivy configurations.

If the directory is not a git repo, skip tag-based version detection and use the manifest version.

## Phase 2 — Generate SECURITY.md

Use the template in `templates/SECURITY.template.md` (bundled alongside this skill) as a structural guide.

### Section Guidance

- **Supported Versions** — Build a table from recent releases. Current major gets full support; previous major gets security fixes only.
- **Reporting a Vulnerability** — Private channel only (GitHub private reporting or email). Never suggest public issues. Include TODO placeholder for email.
- **Disclosure Policy** — Default to coordinated disclosure with 90-day timeline.
- **Security Contacts** — TODO placeholders for names and emails.

## Phase 3 — Write the File

Write `SECURITY.md` to the repository root. Do not write if the file already exists.

## Safety Rules

- **NEVER overwrite** an existing SECURITY.md.
- **NEVER include real email addresses** unless extracted from an existing file. Use TODO placeholders.
- **NEVER recommend public issue trackers** for vulnerability reporting.
- **ALWAYS include a response timeline.**
