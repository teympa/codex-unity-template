---
name: start-project
description: Review the current Unity repository state, identify missing setup or structure, and recommend the next safe steps before heavy implementation starts.
---

# Purpose

Use this skill at the start of a new Unity project or when importing this template into an existing repository.

## Use Cases

- Starting a new Unity repository from this template
- Bringing this template into an existing Unity project
- Checking whether the repo is ready for Codex-driven development
- Figuring out the next safe step before implementation

## How To Review

1. Read the root `README.md` and `AGENTS.md`.
2. Check whether the expected Unity script folders exist.
3. Check whether hooks, CI, and validator paths still make sense.
4. Identify the smallest next action that improves readiness without causing churn.

## Checklist

- Is the repository actually a Unity project?
- Are `Assets/Scripts/Gameplay/`, `UI/`, `Core/`, and `Tests/` present or planned?
- Are AGENTS files placed where Codex will benefit from them?
- Is the project missing setup steps such as hooks or Python validation?
- Does the current structure make gameplay/UI boundaries unclear?
- Are there obvious risks before implementation starts?

## Output Format

### Current State

Short description of the repository readiness.

### Missing Pieces

List setup or structure gaps that should be addressed.

### Immediate Next Steps

List the smallest safe actions to take next.

### Risks

List risks that may slow down Codex or cause messy Unity structure.

### Verdict

State `Ready`, `Ready with setup`, or `Needs structure first`.
