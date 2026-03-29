# Codex Unity Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/LICENSE)
[![codex-checks](https://github.com/teympa/codex-unity-template/actions/workflows/codex-checks.yml/badge.svg)](https://github.com/teympa/codex-unity-template/actions/workflows/codex-checks.yml)

Reusable template repository for running Unity development with Codex using lightweight rules, review skills, git hooks, and CI.

This template is meant to be copied or used as a base repository for new Unity game projects. It is designed for teams that want a small, practical operating set instead of a heavy framework.

If you publish this on GitHub, you can use it as a Template Repository so new Unity projects can start from the same Codex-ready operating set.

[Setup](#start-here) | [Usage](#start-here) | [Japanese Docs](#japanese-docs) | [License](#license)

Start a new project with GitHub's `Use this template` button, then open the new repository and follow the setup guide. This template is meant to help beginners start with a clean Unity structure, lightweight guardrails, and Codex-friendly working rules from day one.

## Quick Start On GitHub

```text
Use this template
    -> Create a new repository
    -> Open the new repo
    -> Follow docs/SETUP.md
    -> Start building your Unity game with Codex
```

## What You Do First

1. Click `Use this template` on GitHub.
2. Create your new Unity project repository from this template.
3. Read `[docs/SETUP.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/SETUP.md)` or `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)`.
4. Enable git hooks and run the gameplay validator once.

## Table Of Contents

- [What This Template Gives You](#what-this-template-gives-you)
- [Who This Is For](#who-this-is-for)
- [Start Here](#start-here)
- [Japanese Docs](#japanese-docs)
- [Using This As A GitHub Template](#using-this-as-a-github-template)
- [Template Layout](#template-layout)
- [Default Unity Structure](#default-unity-structure)
- [Template Scope](#template-scope)
- [Notes](#notes)
- [License](#license)

## What This Template Gives You

- Short repo rules for Codex in `[AGENTS.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/AGENTS.md)`
- Local rules for gameplay and UI folders
- Repeatable review skills for code review and design review
- Lightweight git hooks for local checks
- Minimal GitHub Actions CI
- A small static validator focused on common Unity gameplay risks

## Who This Is For

- Solo developers using Codex while learning Unity
- Small teams that want simple guardrails
- Projects that want to reduce messy `MonoBehaviour` growth and gameplay/UI coupling

## Start Here

- Setup guide: `[docs/SETUP.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/SETUP.md)`
- Usage guide: `[docs/USAGE.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/USAGE.md)`
- Template customization notes: `[docs/CUSTOMIZE.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/CUSTOMIZE.md)`
- Template upgrade notes: `[UPGRADING.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/UPGRADING.md)`
- Contribution guide: `[CONTRIBUTING.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/CONTRIBUTING.md)`
- Codex prompt examples: `[docs/examples/CODEX_PROMPTS.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/examples/CODEX_PROMPTS.md)`
- Feature design example: `[docs/examples/FEATURE_REQUEST_EXAMPLE.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/examples/FEATURE_REQUEST_EXAMPLE.md)`
- Feature design template: `[docs/templates/FEATURE_DESIGN_TEMPLATE.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/templates/FEATURE_DESIGN_TEMPLATE.md)`

## Japanese Docs

- README overview in Japanese: `[docs/ja/README.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/README.ja.md)`
- Setup guide in Japanese: `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)`
- Usage guide in Japanese: `[docs/ja/USAGE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/USAGE.ja.md)`
- Customization guide in Japanese: `[docs/ja/CUSTOMIZE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/CUSTOMIZE.ja.md)`
- Upgrade guide in Japanese: `[docs/ja/UPGRADING.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/UPGRADING.ja.md)`
- Contribution guide in Japanese: `[docs/ja/CONTRIBUTING.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/CONTRIBUTING.ja.md)`
- Codex prompt examples in Japanese: `[docs/ja/examples/CODEX_PROMPTS.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/examples/CODEX_PROMPTS.ja.md)`
- Feature design example in Japanese: `[docs/ja/examples/FEATURE_REQUEST_EXAMPLE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/examples/FEATURE_REQUEST_EXAMPLE.ja.md)`
- Feature design template in Japanese: `[docs/ja/templates/FEATURE_DESIGN_TEMPLATE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/templates/FEATURE_DESIGN_TEMPLATE.ja.md)`

## Using This As A GitHub Template

1. Push this repository to GitHub.
2. Enable the repository's Template Repository setting.
3. Create a new Unity project repository from this template.
4. Open the new repository and follow the setup guide.

## Template Layout

- `AGENTS.md`
- `Assets/Scripts/Gameplay/AGENTS.md`
- `Assets/Scripts/UI/AGENTS.md`
- `skills/code-review/SKILL.md`
- `skills/design-review/SKILL.md`
- `skills/start-project/SKILL.md`
- `scripts/validate_unity_gameplay.py`
- `.githooks/pre-commit`
- `.githooks/pre-push`
- `.github/workflows/codex-checks.yml`
- `.gitignore`

## Default Unity Structure

This template assumes the following script layout when possible:

- `Assets/Scripts/Gameplay/`
- `Assets/Scripts/UI/`
- `Assets/Scripts/Core/`
- `Assets/Scripts/Tests/`

If your project already uses a different layout, adjust the paths carefully instead of removing the guardrails.

## Template Scope

- Keeps rules short and practical
- Adds light guardrails rather than heavy automation
- Focuses on common Unity failure modes:
  - bloated `MonoBehaviour`
  - hardcoded gameplay values
  - UI and gameplay coupling
  - wasteful update-loop code

## Notes

- The validator uses heuristic checks, not full static analysis.
- If `Assets/Scripts/Gameplay/` does not exist yet, validation skips cleanly.
- This template does not add Unity packages, test frameworks, or build automation by default.

## License

This template is available under the MIT License. See `[LICENSE](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/LICENSE)`.
