# GitHub Community Health Profile

Reference for GitHub's recommended community health files. Used by the `scaffolding-repo-documentation` skill to align with GitHub's standards.

## What GitHub Checks

GitHub's community profile (visible at `https://github.com/<owner>/<repo>/community`) evaluates:

| File | Required for Profile | Notes |
|------|---------------------|-------|
| README.md | Yes | Must be non-empty |
| CODE_OF_CONDUCT.md | Yes | Can also be in `.github/` or `docs/` |
| CONTRIBUTING.md | Yes | Can also be in `.github/` or `docs/` |
| LICENSE | Yes | Detected by licensee gem |
| SECURITY.md | Yes | Can also be in `.github/` or `docs/` |
| .github/ISSUE_TEMPLATE/ | Yes | Or `.github/ISSUE_TEMPLATE.md` |
| .github/PULL_REQUEST_TEMPLATE.md | Yes | Or in `docs/` |

## Organization Defaults

Organizations can place default community health files in a `.github` repository. These apply to all repos that lack their own copy. When scaffolding, note this possibility so teams know they may not need per-repo copies.

## File Location Precedence

GitHub looks for community health files in this order:

1. Repository root
2. `.github/` directory
3. `docs/` directory

Prefer the repository root for discoverability, except:

- Issue templates → `.github/ISSUE_TEMPLATE/` (required location)
- PR template → `.github/PULL_REQUEST_TEMPLATE.md` (conventional location)
- CODEOWNERS → `.github/CODEOWNERS` or repository root (both work)
