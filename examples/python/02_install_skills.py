"""Example: Install skills from the demo-starter bundle into a Claude Code project."""

from pathlib import Path

import musher

# Pull the demo-starter bundle
bundle = musher.pull("musher-dev/demo-starter:1.0.0")

# Target directory for Claude Code skills
# Relative to your project root — Claude Code discovers skills from .claude/skills/
skills_dir = Path(".claude/skills")

# Install specific skills from the bundle.
# clean=True removes stale Musher-managed installs for this bundle from the
# target directory; it does NOT affect manually placed skills.
bundle.install_claude_skills(
    skills_dir,
    skills=["summarize-changes", "write-commit-message"],
    clean=True,
)

print(f"Installed skills to {skills_dir}/")
for skill in bundle.skills():
    installed_path = skills_dir / f"{skill.name}.md"
    status = "✓" if installed_path.exists() else "✗"
    print(f"  {status} {skill.name}")

print()
print("Skills are now available in Claude Code.")
print("Try asking: 'Summarize the changes since the last release'")
print("Or: 'Write a commit message for my staged changes'")
