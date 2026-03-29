# Usage Guide

This guide explains how to use the template during day-to-day Unity development with Codex.

## Basic Idea

The template splits support into three layers:

- `AGENTS.md`: working rules for Codex
- `skills/`: repeatable review instructions
- hooks and CI: lightweight mechanical checks

There is also a good startup workflow:

- `start-project`: use when a repo is new, imported, or not yet ready for implementation

Use them together:

- Put design and coding expectations in `AGENTS.md`
- Use skills for repeated review workflows
- Let hooks and CI catch obvious gameplay issues

## How To Ask Codex For Work

When you ask Codex to implement something, include:

- The feature goal
- Which files or folder area should change
- Any important constraints

Good example:

```text
Add a stamina system for the player.
Only touch Assets/Scripts/Gameplay and Assets/Scripts/UI.
Keep gameplay logic out of UI and avoid hardcoded balance values.
```

## How To Use The Design Review Skill

Use `design-review` before implementation when:

- The feature is still vague
- You are unsure where game state should live
- The system has multiple states or transitions
- UI and gameplay boundaries are unclear

Ask Codex for a design review before coding starts and have it check:

- state ownership
- UI and gameplay boundaries
- where balance values should live
- whether the design is easy to test and extend

If the repository itself is still being prepared, use `start-project` first and let Codex identify the smallest safe next setup step.

## How To Use The Code Review Skill

Use `code-review` after implementation when:

- You added gameplay code
- You changed player, enemy, combat, or state systems
- You touched `Update`, `FixedUpdate`, or `LateUpdate`
- A `MonoBehaviour` is becoming large

Ask Codex to review the changed files against the local `AGENTS.md` rules.

## What The Validator Checks

`[scripts/validate_unity_gameplay.py](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/scripts/validate_unity_gameplay.py)` scans `Assets/Scripts/Gameplay/**/*.cs` and flags:

- suspicious hardcoded numeric values
- `GameObject.Find`
- `FindObjectOfType`
- `FindAnyObjectByType`
- `public static Instance` style singleton growth
- per-frame `GetComponent`
- LINQ in `Update`, `FixedUpdate`, or `LateUpdate`
- string concatenation in per-frame methods

This is a light guardrail, not a perfect judge. A finding means "please inspect this carefully," not always "this code is wrong."

## Recommended Daily Workflow

1. Decide whether you need a design review first.
2. Ask Codex to implement a small, scoped change.
3. Run `python scripts/validate_unity_gameplay.py`.
4. Let the git hooks run on commit and push.
5. Ask Codex for a `code-review` on the change before merge.

## Common Mistakes This Template Tries To Reduce

- Putting gameplay rules directly into UI classes
- Letting a single `MonoBehaviour` grow too much
- Hardcoding damage, cooldowns, and tuning values
- Doing unnecessary work every frame
- Hiding state transitions inside scattered booleans

## When To Adjust The Template

Adjust the template when:

- Your project uses a different folder layout
- You need extra validation patterns
- Your team wants stricter or looser review rules

If you customize it, keep the overall split the same:

- rules in `AGENTS.md`
- repeatable review flow in `skills/`
- machine checks in hooks and CI
