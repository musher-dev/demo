# Demo Starter

A demonstration bundle for the [Musher](https://hub.musher.dev) platform. Ships three practical assets — two skills and a specialist agent — that work across all supported CLI harnesses (Claude Code, Codex, OpenCode, Copilot, Gemini CLI).

## Quick Start

Install via the [Mush CLI](https://github.com/musher-dev/mush):

```sh
mush bundle install musher-dev/demo-starter
```

Then invoke from any compatible harness:

```
Summarize the changes in the last 5 commits
```

```
Write a conventional commit message for my staged changes
```

Or delegate to the specialist agent:

```
Use the code-reviewer agent to review my latest changes
```

## What's Inside

### Skills

| Skill | Description |
|-------|-------------|
| `summarize-changes` | Summarize git history, staged diffs, or PR changes into clear, human-readable summaries |
| `write-commit-message` | Generate Conventional Commits–compliant messages from staged diffs or a description of the change |

### Agents

| Agent | Description |
|-------|-------------|
| `code-reviewer` | A specialist read-only agent that reviews code for quality, correctness, and best-practice adherence with structured feedback |

## Usage Examples

**Summarize recent changes**
```
Summarize the changes since the last release
```

**Write a commit message**
```
Write a commit message for my staged changes
```

**Delegate a thorough code review**
```
Use the code-reviewer agent to review the authentication module
```

---

**Domain:** developer-workflows · **Technologies:** Harness-agnostic · **Aliases:** demo, starter, git-workflows
