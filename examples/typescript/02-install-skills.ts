/**
 * Install skills from the repo-documentation-governance bundle into a Claude Code project.
 *
 * This copies multi-file skills (SKILL.md + companion files like rubrics,
 * templates, and checklists) into .claude/skills/ where the Claude Agent SDK
 * discovers them.
 *
 * Prerequisites:
 *   export MUSHER_API_KEY="mush_..."
 *
 * To use your own published bundle, set:
 *   export MUSHER_BUNDLE_REF="your-namespace/repo-documentation-governance:1.0.0"
 *
 * Run:
 *   npx tsx 02-install-skills.ts
 */

import { pull } from "@musher-dev/musher-sdk";

const bundleRef =
	process.env.MUSHER_BUNDLE_REF ?? "musher-examples/repo-documentation-governance:1.0.0";

const bundle = await pull(bundleRef);

// installClaudeSkills writes to .claude/skills/ under the given project root.
const projectRoot = ".";

const written = await bundle.installClaudeSkills(projectRoot);

console.log(`Installed ${written.length} file(s) to .claude/skills/`);
for (const filePath of written) {
	console.log(`  ${filePath}`);
}

console.log();
console.log("Skills are now available to the Claude Agent SDK.");
console.log("See examples/python/repo_docs_audit.py for the Agent SDK demo.");
