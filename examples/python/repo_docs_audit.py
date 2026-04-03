"""Audit and scaffold repository documentation using a Musher bundle
and the Claude Agent SDK.

This script demonstrates the full Musher consumption flow:

1. Pull a versioned bundle from the Musher registry
2. Inspect its multi-file skills and agent specs
3. Install skills into .claude/skills/ for SDK discovery
4. Run the Claude Agent SDK — it discovers skills, applies hooks,
   and returns structured JSON output

Prerequisites:
    pip install -r requirements.txt
    export MUSHER_API_KEY="mush_..."
    export ANTHROPIC_API_KEY="sk-ant-..."

To use your own published bundle:
    export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Any

import musher
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    HookMatcher,
    ResultMessage,
    query,
)

THIS_DIR = Path(__file__).resolve().parent
SKILLS_DIR = THIS_DIR / ".claude" / "skills"
FIXTURE_DIR = THIS_DIR / "fixtures" / "under_documented_repo"
OUTPUT_DIR = THIS_DIR / "out"
TOOL_LOG = OUTPUT_DIR / "tool_calls.jsonl"

BUNDLE_REF = os.environ.get(
    "MUSHER_BUNDLE_REF", "musher-examples/repo-documentation-governance:1.0.0"
)

SKILL_NAMES = [
    "auditing-repo-documentation",
    "scaffolding-repo-documentation",
    "writing-readme",
    "writing-security-policy",
]

REPORT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "overall_score": {"type": "number"},
        "missing_files_before": {"type": "array", "items": {"type": "string"}},
        "files_created": {"type": "array", "items": {"type": "string"}},
        "high_priority_gaps": {"type": "array", "items": {"type": "string"}},
        "follow_up_recommendations": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": [
        "overall_score",
        "missing_files_before",
        "files_created",
        "high_priority_gaps",
        "follow_up_recommendations",
    ],
}


# ── Hooks ────────────────────────────────────────────────────────────────────


def _safe_resolve(path_str: str) -> Path:
    try:
        return Path(path_str).expanduser().resolve()
    except Exception:
        return Path(path_str)


async def guard_fixture_writes(
    input_data: dict[str, Any],
    tool_use_id: str,
    context: Any,
) -> dict[str, Any]:
    """Deny writes outside the fixture repo and protect .env files."""
    if input_data.get("hook_event_name") != "PreToolUse":
        return {}

    tool_name = input_data.get("tool_name", "")
    if tool_name not in {"Write", "Edit"}:
        return {}

    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    target = _safe_resolve(file_path)
    fixture_root = FIXTURE_DIR.resolve()

    if target.name == ".env":
        return {
            "hookSpecificOutput": {
                "hookEventName": input_data["hook_event_name"],
                "permissionDecision": "deny",
                "permissionDecisionReason": "Editing .env files is blocked.",
            }
        }

    if not str(target).startswith(str(fixture_root)):
        return {
            "systemMessage": "Only modify files inside the fixture repository.",
            "hookSpecificOutput": {
                "hookEventName": input_data["hook_event_name"],
                "permissionDecision": "deny",
                "permissionDecisionReason": "Writes are only allowed inside the fixture repository.",
            },
        }

    return {}


async def log_pretool(
    input_data: dict[str, Any],
    tool_use_id: str,
    context: Any,
) -> dict[str, Any]:
    """Append tool-call events to a local JSONL log."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "tool_use_id": tool_use_id,
        "hook_event_name": input_data.get("hook_event_name"),
        "tool_name": input_data.get("tool_name"),
        "tool_input": input_data.get("tool_input"),
    }
    with TOOL_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    return {}


# ── Step 1: Pull & Inspect ──────────────────────────────────────────────────


def pull_and_inspect() -> musher.Bundle:
    """Pull the bundle from the registry and print its contents."""
    print(f"Pulling bundle: {BUNDLE_REF}")
    bundle = musher.pull(BUNDLE_REF)
    print(f"  Version: {bundle.version}")
    print(f"  Files:   {len(list(bundle.files()))}")
    print()

    print("Skills:")
    for skill in bundle.skills():
        files = skill.files()
        print(f"  {skill.name} ({len(files)} file(s))")
        for fh in files:
            print(f"    {fh.logical_path}")
    print()

    print("Agent specs:")
    for agent in bundle.agent_specs():
        print(f"  {agent.name}")
    print()

    return bundle


# ── Step 2: Install Skills ──────────────────────────────────────────────────


def install_skills(bundle: musher.Bundle) -> None:
    """Install multi-file skills into .claude/skills/ for SDK discovery."""
    bundle.install_claude_skills(
        SKILLS_DIR,
        skills=SKILL_NAMES,
        clean=True,
    )

    print(f"Installed skills to {SKILLS_DIR}/")
    for name in SKILL_NAMES:
        skill_path = SKILLS_DIR / name
        if skill_path.exists():
            installed = [f for f in skill_path.rglob("*") if f.is_file()]
            print(f"  ✓ {name} ({len(installed)} file(s))")
            for f in installed:
                print(f"      {f.relative_to(skill_path)}")
        else:
            print(f"  ✗ {name} (not found)")
    print()


# ── Step 3: Run Agent SDK ───────────────────────────────────────────────────


async def run_agent() -> None:
    """Run the Claude Agent SDK against the fixture repo."""
    if not FIXTURE_DIR.exists():
        raise SystemExit(f"Fixture repo not found: {FIXTURE_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    prompt = f"""
Audit the repository at {FIXTURE_DIR} for missing community-health and onboarding
documentation.

Use installed Skills when relevant.

Constraints:
- Only inspect and modify files inside {FIXTURE_DIR}
- Do not touch secrets or .env files
- Focus on repository documentation and GitHub community-health files
- Create missing files when useful
- Return the final answer as structured JSON that matches the required schema
"""

    options = ClaudeAgentOptions(
        cwd=str(THIS_DIR),
        setting_sources=["project"],
        allowed_tools=["Skill", "Read", "Write", "Edit", "Glob", "Grep"],
        permission_mode="dontAsk",
        hooks={
            "PreToolUse": [
                HookMatcher(matcher="Write|Edit", hooks=[guard_fixture_writes]),
                HookMatcher(hooks=[log_pretool]),
            ]
        },
        output_format={"type": "json_schema", "schema": REPORT_SCHEMA},
    )

    report_path = OUTPUT_DIR / "repo_docs_report.json"

    print("Running Claude Agent SDK...")
    print(f"  Skills source: {SKILLS_DIR}")
    print(f"  Target repo:   {FIXTURE_DIR}")
    print()

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text") and block.text:
                    print(block.text)
                elif hasattr(block, "name"):
                    print(f"[tool] {block.name}")

        elif isinstance(message, ResultMessage):
            if message.subtype == "success" and message.result:
                try:
                    report = json.loads(message.result)
                except (json.JSONDecodeError, TypeError):
                    report = {"raw_result": message.result}

                report_path.write_text(
                    json.dumps(report, indent=2),
                    encoding="utf-8",
                )
                print("\n── Structured Report ────────────────────────────")
                print(json.dumps(report, indent=2))
                print(f"\nSaved to: {report_path}")
                print(f"Tool log: {TOOL_LOG}")
            else:
                print(f"Run finished with subtype={message.subtype}")
                if message.result:
                    print(message.result)


# ── Main ────────────────────────────────────────────────────────────────────


async def main() -> None:
    bundle = pull_and_inspect()
    install_skills(bundle)
    await run_agent()


if __name__ == "__main__":
    asyncio.run(main())
