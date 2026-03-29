---
name: write-commit-message
version: 1.0.0
user-invocable: true
description: Generate a Conventional Commits–compliant commit message from staged changes or a plain-language description. Use when you want a well-structured commit message, are unsure how to categorize a change, or want to ensure your commit history stays readable. Triggered by: write commit message, commit message, conventional commit, git commit, commit this, what should I commit.
argument-hint: "[description of the change]"
allowed-tools:
  - Bash
  - Read
---

# Write Commit Message

Generate a clear, Conventional Commits–compliant commit message.

## Conventional Commits Format

```
<type>(<optional scope>): <short description>

[optional body]

[optional footer(s)]
```

**Types:**

| Type | When to use |
|------|-------------|
| `feat` | A new feature or capability |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `style` | Formatting, whitespace (no logic change) |
| `refactor` | Code restructuring without feature/fix |
| `test` | Adding or updating tests |
| `chore` | Build tooling, dependencies, CI, config |
| `perf` | Performance improvements |
| `ci` | CI/CD pipeline changes |
| `revert` | Reverting a previous commit |

---

## Input

**Arguments:** `$ARGUMENTS`

- If arguments are provided, treat them as a plain-language description of the change.
- If arguments are empty, inspect staged changes.

---

## Phase 1: Gather Context

**If a description was provided in `$ARGUMENTS`:**
Use it directly to infer the type, scope, and short description. Skip to Phase 2.

**If no description was provided:**
Inspect the staged diff:

```bash
git diff --cached --stat
git diff --cached
```

If there are no staged changes, check if there are unstaged changes:

```bash
git diff --stat
```

If no changes at all:
> "No staged or unstaged changes found. Stage your changes with `git add` first, or provide a description as an argument."

Stop.

---

## Phase 2: Determine Type and Scope

Analyze the diff or description:

1. **Type**: Choose the most specific matching type from the table above. When in doubt between `feat` and `fix`, prefer the one that matches the user's intent.

2. **Scope** (optional): A short noun identifying the affected module, component, or domain. Examples: `auth`, `api`, `ui`, `db`, `cli`, `deps`. Omit if the change is broad or cross-cutting.

3. **Breaking change**: If the change breaks backward compatibility, add `!` after the type/scope (e.g., `feat(api)!:`) and include a `BREAKING CHANGE:` footer.

---

## Phase 3: Write the Subject Line

The subject line must:
- Start with `<type>(<scope>):` (scope is optional)
- Use **imperative mood**: "add", "fix", "update", "remove" — not "added", "fixes", "updating"
- Be **72 characters or fewer**
- Not end with a period
- Be specific enough to understand the change without reading the body

**Good examples:**
```
feat(auth): add OAuth2 login with Google and GitHub
fix(cache): prevent race condition on concurrent writes
chore(deps): bump axios from 1.6.0 to 1.7.2
docs(readme): add installation instructions for Windows
refactor(api): extract rate-limiting middleware into separate module
```

**Bad examples:**
```
fix stuff                          ← too vague
feat: Added new thing.             ← past tense, trailing period
feat(authentication-service): implement OAuth2 login flow with Google  ← too long
```

---

## Phase 4: Write the Body (if needed)

Add a body when any of these apply:
- The *why* behind the change is not obvious from the subject
- There are important implementation notes (e.g., "uses exponential backoff")
- The change has side effects developers should know about

Body rules:
- Separate from the subject with a blank line
- Wrap at 72 characters per line
- Use imperative mood
- Explain *what* and *why*, not *how* (the code shows the how)

---

## Phase 5: Write Footers (if needed)

Add footers for:
- **Breaking changes**: `BREAKING CHANGE: <description of what broke and migration path>`
- **Issue references**: `Closes #123` or `Fixes #456`
- **Co-authors**: `Co-authored-by: Name <email>`

---

## Phase 6: Output

Present the final commit message in a code block:

```
feat(auth): add OAuth2 login with Google and GitHub

Replaces the username/password-only flow with an OAuth2 provider
selection screen. Existing sessions remain valid; users who have
not yet linked a provider will be prompted on next login.

Closes #42
```

Then offer:
> Ready to commit? Run:
> ```bash
> git commit -m "feat(auth): add OAuth2 login with Google and GitHub"
> ```
> Or for a multi-line message:
> ```bash
> git commit
> ```
> (This opens your editor with the full message pre-filled by the harness.)

---

## Edge Cases

- **Multiple unrelated changes staged** → Warn: "Your staged changes touch unrelated areas. Consider splitting into separate commits for a cleaner history." Then generate the best single message anyway.
- **Only whitespace/formatting changes** → Use `style` type.
- **Dependency bump** → Use `chore(deps):` with the package name and version range in the subject.
- **Revert** → Use `revert:` and reference the original commit SHA in the body.
