# Repo Documentation Governance

A [Musher](https://hub.musher.dev) bundle that audits and scaffolds repository documentation. Ships four multi-file skills and a specialist agent — designed to demonstrate how Musher distributes versioned agent behavior for the Claude Agent SDK.

- **Domain:** repo-documentation
- **Purpose:** governance
- **Risk Level:** low
- **Technologies:** Claude Agent SDK
- **Aliases:** repo-docs, documentation-audit

## Quick Start

Publish to your own account or pack locally:

```sh
cd bundle

# Option A: Publish to Musher Hub
musher bundle publish

# Option B: Local pack (no account needed)
musher bundle pack
```

Then install and use the skills:

```
Audit this repo's documentation health
```

```
Scaffold missing community-health files
```

## What's Inside

### Skills

| Skill | Files | Description |
|-------|-------|-------------|
| `auditing-repo-documentation` | SKILL.md, scoring-rubric.md | Score documentation health with weighted rubric |
| `scaffolding-repo-documentation` | SKILL.md, docs-checklist.md, github-community-profile.md | Create missing docs based on audit results |
| `writing-readme` | SKILL.md, templates/README.template.md | Generate or improve README.md |
| `writing-security-policy` | SKILL.md, templates/SECURITY.template.md | Generate SECURITY.md with disclosure policy |

### Agents

| Agent | Description |
|-------|-------------|
| `repo_docs_auditor` | Orchestrator that audits, scaffolds, and reports in a single run |

### Tools

None

## Why Multi-File Skills?

Each skill ships companion files (rubrics, templates, checklists) alongside SKILL.md. This demonstrates Musher's distribution value: you are not just shipping a prompt, you are shipping **reusable expertise with supporting data** — versioned, pinned, and discoverable by the SDK.

