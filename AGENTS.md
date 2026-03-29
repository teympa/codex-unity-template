# Codex Unity Template

This repository is a reusable Codex starter template for Unity game development. Copy these files into a Unity project when you want lightweight guardrails that prefer maintainable structure over temporary fixes.

## Working Style

- Before implementation, summarize the goal, target files, and main risks in a few lines.
- If requirements are ambiguous, present 2 to 3 concrete options before implementing.
- For larger changes, show a short implementation plan before starting.
- Do not commit unless explicitly asked.
- Do not add dependencies unless explicitly asked.
- After changes, run test, lint, or build-equivalent checks when practical.
- Do not touch unrelated files.
- Avoid mixing refactors and behavior changes more than necessary.

## Template Notes

- This file set is designed to be copied into other Unity repositories as a starting point.
- Keep the default paths when possible so skills, hooks, and CI stay portable across projects.
- If a target project uses a different script layout, adjust paths carefully instead of weakening the rules.

## Responsibility Boundaries

- `Assets/Scripts/Gameplay/`: game rules, state transitions, progression control
- `Assets/Scripts/UI/`: presentation and input bridging
- `Assets/Scripts/Core/`: shared foundation, config, events, helpers
- `Assets/Scripts/Tests/`: test-related code

## Unity Gameplay Rules

- Do not hardcode balance values in code; read them from ScriptableObjects, config classes, or definition data.
- Handle time-dependent logic with `Time.deltaTime` or `FixedUpdate` according to responsibility.
- UI must not own game state.
- Gameplay must not directly depend on UI.
- Avoid casually increasing reliance on `GameObject.Find`, `FindObjectOfType`, or `FindAnyObjectByType`.
- Avoid adding unordered global singleton access patterns.
- Do not pack multiple responsibilities into one `MonoBehaviour`.
- Make state transitions explicit with `enum`, state classes, or state machines.
- In per-frame logic, avoid unnecessary `GetComponent`, LINQ, string concatenation, and allocations.
- If an Inspector reference is required, use `SerializeField` and keep ownership explicit.
- Separate pure logic from `MonoBehaviour` where possible so it stays testable.

## Review Priorities

- Separation of responsibilities
- Increase in hardcoded values
- Mixed or unclear state management
- Reversed dependency between UI and gameplay
- Bloated `MonoBehaviour` classes
- Wasteful per-frame processing
- Structures that are hard to test
- Risky Unity reference lookup patterns

## Done Criteria

- Runnable tests pass when available.
- No new hardcoded balance values or mixed responsibilities are introduced.
- Per-frame waste has not increased.
- Docs or design notes are updated when needed.
- The change can be explained briefly and clearly.
