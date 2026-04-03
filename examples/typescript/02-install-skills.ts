/**
 * Install skills from the demo-starter bundle into a Claude Code project.
 *
 * This copies skill files into a .claude/skills/ directory so that
 * Claude Code auto-discovers them when running in the project.
 *
 * Prerequisites:
 *   export MUSHER_API_KEY="mush_..."
 *
 * Run:
 *   npx tsx 02-install-skills.ts
 */

import { pull } from "@musher-dev/musher-sdk";

const bundle = await pull("musher-examples/demo-starter:1.0.0");

// installClaudeSkills writes to .claude/skills/ under the given project root.
const projectRoot = ".";

const written = await bundle.installClaudeSkills(projectRoot);

console.log(`Installed ${written.length} skill(s) to .claude/skills/`);
for (const filePath of written) {
	console.log(`  ${filePath}`);
}

console.log();
console.log("Skills are now available in Claude Code.");
console.log("Try asking: 'Summarize the changes since the last release'");
console.log("Or: 'Write a commit message for my staged changes'");
