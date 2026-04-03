"""Example: Pull the demo-starter bundle and inspect its contents."""

import musher

# Credentials are auto-discovered from the MUSHER_API_KEY environment variable,
# the OS keyring, or a credential file (~/.config/musher/credentials.yaml).
# To set credentials explicitly: musher.configure(token="mush_...")

bundle = musher.pull("musher-examples/demo-starter:1.0.0")

print(f"Bundle: {bundle.ref} v{bundle.version}")
print()

# List all files in the bundle
print(f"Files ({len(list(bundle.files()))}):")
for fh in bundle.files():
    print(f"  {fh.logical_path}  ({fh.media_type or 'unknown'})")
print()

# List available skills
print(f"Skills ({len(bundle.skills())}):")
for skill in bundle.skills():
    print(f"  {skill.name}")
    # Show a preview of the skill's SKILL.md content
    preview = skill.skill_md().text().strip().splitlines()
    # Skip frontmatter, show first content line
    in_frontmatter = False
    for line in preview:
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if not in_frontmatter and line.strip():
            print(f"    → {line.strip()[:100]}")
            break
print()

# List available agents
print(f"Agent specs ({len(bundle.agent_specs())}):")
for agent in bundle.agent_specs():
    print(f"  {agent.name}")
print()

# Access a specific skill by name
try:
    skill = bundle.skill("summarizing-changes")
    print(f"Skill content preview ({skill.name}):")
    print(skill.skill_md().text()[:300])
    print("...")
except KeyError:
    print("Skill 'summarizing-changes' not found in bundle")
