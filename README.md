# Musher Demo

A showcase repository for the [Musher](https://hub.musher.dev) platform. It contains a ready-to-publish bundle with multi-file skills and an agent spec, plus SDK examples that demonstrate the full lifecycle: **author → publish → install → run with Claude Agent SDK**.

## Why This Example Exists

Instead of hard-coding long system prompts or manually copying `.claude/skills/` folders between projects, we:

1. **Author** a versioned Musher bundle with multi-file skills (rubrics, templates, checklists)
2. **Publish** it to the Musher Hub (or pack it locally)
3. **Install** the skills into the filesystem layout the Claude Agent SDK expects
4. **Run** the Agent SDK — Claude discovers and invokes the skills autonomously, constrained by hooks, permissions, and structured output

The demo uses a **repo documentation auditing** use case: the agent scans a fixture repository, scores its documentation health, and scaffolds missing files.

## What's Inside

```
demo/
├── bundle/                            Musher bundle source (skills + agents)
│   ├── musher.yaml                    Bundle manifest
│   ├── skills/
│   │   ├── auditing-repo-documentation/     Score documentation health (SKILL.md + rubric)
│   │   ├── scaffolding-repo-documentation/  Create missing docs (SKILL.md + checklist + reference)
│   │   ├── writing-readme/                  Generate README (SKILL.md + template)
│   │   └── writing-security-policy/         Generate SECURITY.md (SKILL.md + template)
│   └── agents/
│       └── repo_docs_auditor.md       Orchestrator agent composing all skills
└── examples/
    ├── python/
    │   ├── repo_docs_audit.py         Pull, install, and run Agent SDK in one script
    │   └── fixtures/under_documented_repo/  Intentionally under-documented fixture project
    └── typescript/                    TypeScript SDK (pull + install; Agent SDK demo pending)
```

## The Bundle

The `repo-documentation-governance` bundle ships four multi-file skills and one agent for documentation governance.

| Asset | Type | Files | What it does |
|-------|------|-------|--------------|
| `auditing-repo-documentation` | Skill | SKILL.md, scoring-rubric.md | Score docs health with weighted rubric |
| `scaffolding-repo-documentation` | Skill | SKILL.md, docs-checklist.md, github-community-profile.md | Create missing docs based on audit |
| `writing-readme` | Skill | SKILL.md, templates/README.template.md | Generate or improve README.md |
| `writing-security-policy` | Skill | SKILL.md, templates/SECURITY.template.md | Generate SECURITY.md with disclosure policy |
| `repo-docs-auditor` | Agent | repo_docs_auditor.md | Orchestrator that audits, scaffolds, and reports |

## Quick Start

### 1. Publish or pack the bundle

```bash
# Install the Musher CLI
curl -fsSL https://get.musher.dev | sh

cd bundle

# Option A: Publish to your Musher Hub account
musher bundle publish

# Option B: Pack locally (no account needed)
musher bundle pack
```

### 2. Run the demo (Python)

```bash
cd examples/python
pip install -r requirements.txt
export MUSHER_API_KEY="mush_..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Point at your published bundle (or use the default)
export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"

python repo_docs_audit.py
```

The script pulls the bundle, installs skills, and runs the Claude Agent SDK in one go.

### What to Look For

- Skills are loaded from `.claude/skills/` — including companion files (rubrics, templates)
- Claude invokes them autonomously through the `Skill` tool
- Hooks constrain where the agent can write (fixture repo only)
- The final result is JSON you could feed into CI, a dashboard, or another service

## Related Repositories

| Repo | Description |
|------|-------------|
| [musher-dev/musher-cli](https://github.com/musher-dev/musher-cli) | Musher CLI — install, run, author, and publish bundles |
| [musher-dev/python-sdk](https://github.com/musher-dev/python-sdk) | Python SDK for the Musher platform |
| [musher-dev/typescript-sdk](https://github.com/musher-dev/typescript-sdk) | TypeScript SDK for the Musher platform |
| [musher-dev/specs](https://github.com/musher-dev/specs) | Bundle definition schemas and specifications |
| [musher-dev/bundles](https://github.com/musher-dev/bundles) | Community bundle collection |

## Dev Container

This repo includes a dev container with Python, Node.js, and Claude CLI pre-installed. See [CONFIGURATION.md](CONFIGURATION.md) for details.
