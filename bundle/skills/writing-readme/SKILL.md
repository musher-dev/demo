---
name: writing-readme
version: 1.0.0
user-invocable: true
description: Generate or improve a README.md tailored to the repository's language, framework, and purpose. Use when creating a new README, improving an existing one, or a repo lacks onboarding documentation. Triggered by: write readme, generate readme, improve readme, missing readme, onboarding docs.
argument-hint: "[path/to/repo] [--improve]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
---

# Write README

Generate a comprehensive README.md or improve an existing one using repository context.

## Input

**Arguments:** `$ARGUMENTS`

- **Path** — Repository root. Defaults to current working directory.
- **`--improve`** — Improve an existing README rather than replacing it.
- Without `--improve`, if README.md already exists, warn before overwriting.

## Phase 1 — Analyze the Repository

Read the repository to gather information for each section:

1. **Project identity** — Name, description, version from manifest files.
2. **Build and test tooling** — Makefile, CI workflows, Dockerfile, etc.
3. **Package manager** — Detect from lockfiles (package-lock.json, uv.lock, Cargo.lock, etc.).
4. **Configuration** — `.env.example`, linter configs, editor settings.

If an existing README is present and `--improve` was passed, read it to identify which sections exist and which are thin or missing.

## Phase 2 — Generate the README

Use the template in `templates/README.template.md` (bundled alongside this skill) as a structural guide. Fill each section with real content from the repository analysis.

### Section Guidance

- **Title and Description** — Use the project name from the manifest. Write a 1–2 sentence description.
- **Badges** — Only include badges for tools actually present (CI, license, package version).
- **Installation** — Provide the exact install command for the detected package manager.
- **Usage** — Extract from scripts in the manifest or Makefile targets. Show at least one concrete example.
- **Configuration** — Include if `.env.example` or config files exist.
- **Development** — Setup steps, test command, lint command.
- **Contributing** — Link to `CONTRIBUTING.md` if it exists.
- **License** — Reference the LICENSE file and state the license type.

## Phase 3 — Write or Improve

**New README:** Write the complete file.

**Improve mode (`--improve`):**
- Identify missing sections by comparing against the template.
- Append or insert missing sections in the correct order.
- Expand thin sections (< 2 sentences) with detected context.
- Do not remove or rewrite existing adequate sections.

## Quality Standards

- **Be concrete** — Every install command and path should reflect the actual repository.
- **Do not fabricate** — Use `<!-- TODO: ... -->` for anything you cannot determine.
- **Keep it scannable** — Use headings, code blocks, and lists.
- **No placeholders** — Use real project names when available.
