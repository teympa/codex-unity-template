# Codex Prompt Examples

These examples show how to ask Codex for help when using this template in a Unity project.

## 1. Ask For A Small Gameplay Change

```text
Add a dash cooldown system for the player.
Only touch Assets/Scripts/Gameplay and Assets/Scripts/UI.
Do not hardcode balance values in code.
Keep UI as a display/input bridge only.
```

## 2. Ask For A Design Review Before Coding

```text
Use the design-review skill for this feature idea:
The player can charge an attack, release it early for small damage,
or fully charge it for high damage and recoil.
I want help deciding state ownership, UI boundaries, and where tuning values should live.
```

## 3. Ask For A Code Review After Implementation

```text
Use the code-review skill for the changed gameplay files.
Focus on responsibility boundaries, update-loop cost, hardcoded values,
state transitions, and risky Unity reference lookups.
```

## 4. Ask For A Safer Refactor

```text
Refactor the enemy controller so MonoBehaviour stays thin.
Move pure logic into plain classes where practical.
Do not change gameplay behavior unless required.
Summarize goal, touched files, and risks before editing.
```

## 5. Ask For A UI Change Without Breaking Boundaries

```text
Add a stamina bar UI.
UI should only render and react to gameplay state changes.
Do not move gameplay rules into the UI classes.
```

## 6. Ask Codex To Explain A Risk

```text
Review this gameplay script and explain whether Update is doing wasteful work.
Point out GetComponent, LINQ, allocations, or string work if present.
```

## Tips

- Keep requests scoped to a folder or feature.
- Mention whether behavior changes are allowed.
- Mention if you want design review before implementation.
- Mention if you want code review after implementation.
