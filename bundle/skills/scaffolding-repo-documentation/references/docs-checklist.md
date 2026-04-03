# Documentation Checklist

Canonical list of repository documentation files. Used by the `scaffolding-repo-documentation` skill to determine what to check and create.

## High Priority

| File | Path | Auto-Create | Notes |
|------|------|-------------|-------|
| README.md | `README.md` | Yes (via `writing-readme` skill) | Delegates to specialist skill |
| LICENSE | `LICENSE` | **No** | Legal decision; flag only |
| CONTRIBUTING.md | `CONTRIBUTING.md` | Yes | Tailored to detected language |
| SECURITY.md | `SECURITY.md` | Yes (via `writing-security-policy` skill) | Delegates to specialist skill |

## Medium Priority

| File | Path | Auto-Create | Notes |
|------|------|-------------|-------|
| CODE_OF_CONDUCT.md | `CODE_OF_CONDUCT.md` | Yes | Contributor Covenant v2.1 |
| CHANGELOG.md | `CHANGELOG.md` | Yes | Keep a Changelog skeleton |
| CODEOWNERS | `CODEOWNERS` or `.github/CODEOWNERS` | Yes | Placeholder teams |
| PR Template | `.github/PULL_REQUEST_TEMPLATE.md` | Yes | Structured checklist |

## Low Priority

| File | Path | Auto-Create | Notes |
|------|------|-------------|-------|
| Bug Report Template | `.github/ISSUE_TEMPLATE/bug_report.md` | Yes | With YAML frontmatter |
| Feature Request Template | `.github/ISSUE_TEMPLATE/feature_request.md` | Yes | With YAML frontmatter |
| Funding Config | `.github/FUNDING.yml` | **No** | Requires account-specific info |

## Detection Rules

When checking for existence, also check common variants:

- `README.md`, `readme.md`, `README.rst`, `README.txt`
- `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`
- `CHANGELOG.md`, `CHANGES.md`, `HISTORY.md`
- `CODEOWNERS`, `.github/CODEOWNERS`, `docs/CODEOWNERS`
