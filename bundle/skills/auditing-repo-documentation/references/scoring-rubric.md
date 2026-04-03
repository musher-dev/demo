# Documentation Scoring Rubric

This rubric is referenced by the `auditing-repo-documentation` skill. Each file is scored 0–3 and multiplied by its weight to produce a weighted score.

## Score Scale

| Score | Meaning |
|-------|---------|
| 0 | Missing — file does not exist |
| 1 | Poor — file exists but is a stub, placeholder, or severely incomplete |
| 2 | Adequate — file covers the basics but lacks depth or polish |
| 3 | Good — file is thorough, well-structured, and actionable |

## Scored Files

### Tier 1: Critical (Weight 5)

#### README.md
- **Path:** `README.md` (or `readme.md`, `README.rst`)
- **Quality criteria:**
  - Contains project name and description (score ≥ 1)
  - Includes installation/setup instructions (score ≥ 2)
  - Includes usage examples, badges, contributing link, and license reference (score = 3)
- **Why:** The single most important file. First thing every visitor reads.

#### LICENSE
- **Path:** `LICENSE`, `LICENSE.md`, `LICENSE.txt`, or `LICENCE`
- **Quality criteria:**
  - Contains a recognized license text (score ≥ 2)
  - Clearly identifies the license type (score = 3)
- **Why:** Legal requirement for open-source adoption.

### Tier 2: Important (Weight 3)

#### CONTRIBUTING.md
- **Path:** `CONTRIBUTING.md`
- **Quality criteria:**
  - Describes how to submit changes (score ≥ 1)
  - Includes code style, branch strategy, and PR process (score ≥ 2)
  - Covers development setup, testing expectations, and communication channels (score = 3)
- **Why:** Removes friction for new contributors.

#### SECURITY.md
- **Path:** `SECURITY.md`
- **Quality criteria:**
  - Contains a reporting mechanism (score ≥ 1)
  - Specifies supported versions and response timeline (score ≥ 2)
  - Includes disclosure policy and security contacts (score = 3)
- **Why:** Gives vulnerability reporters a safe channel.

#### CODE_OF_CONDUCT.md
- **Path:** `CODE_OF_CONDUCT.md`
- **Quality criteria:**
  - Adopts or references a standard code of conduct (score ≥ 2)
  - Includes enforcement contact and consequences (score = 3)
- **Why:** Sets behavioral expectations for contributors.

#### CHANGELOG.md
- **Path:** `CHANGELOG.md`, `CHANGES.md`, or `HISTORY.md`
- **Quality criteria:**
  - Contains at least one version entry (score ≥ 1)
  - Follows a consistent format (score ≥ 2)
  - Covers recent releases with categorized entries (score = 3)
- **Why:** Lets users understand release history without reading commits.

### Tier 3: Recommended (Weight 2)

#### CODEOWNERS
- **Path:** `CODEOWNERS` or `.github/CODEOWNERS`
- **Quality criteria:**
  - Contains at least one ownership rule (score ≥ 2)
  - Covers major directories with specific teams or individuals (score = 3)
- **Why:** Automates PR review assignment.

#### .github/PULL_REQUEST_TEMPLATE.md
- **Path:** `.github/PULL_REQUEST_TEMPLATE.md`
- **Quality criteria:**
  - Contains a structured template with sections (score ≥ 2)
  - Includes checklist items for testing, docs, and breaking changes (score = 3)
- **Why:** Standardizes PR descriptions.

### Tier 4: Nice to Have (Weight 1)

#### .github/ISSUE_TEMPLATE/
- **Path:** `.github/ISSUE_TEMPLATE/` directory or `.github/ISSUE_TEMPLATE.md`
- **Quality criteria:**
  - At least one template exists (score ≥ 1)
  - Separate templates for bugs and features (score ≥ 2)
  - Includes `config.yml` for template chooser (score = 3)
- **Why:** Reduces incomplete bug reports.

#### .github/FUNDING.yml
- **Path:** `.github/FUNDING.yml`
- **Quality criteria:**
  - Contains at least one valid funding platform entry (score ≥ 2)
- **Why:** Enables GitHub's sponsor button.

## Maximum Possible Score

| Tier | Files | Max per File | Weight | Max Weighted |
|------|-------|-------------|--------|--------------|
| Critical | 2 | 3 | 5 | 30 |
| Important | 4 | 3 | 3 | 36 |
| Recommended | 2 | 3 | 2 | 12 |
| Nice to Have | 2 | 3 | 1 | 6 |
| **Total** | **10** | | | **84** |

Overall score = (sum of weighted scores / 84) × 100, rounded to nearest integer.
