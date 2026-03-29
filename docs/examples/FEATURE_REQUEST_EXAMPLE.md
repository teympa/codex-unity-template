# Feature Request Example

This is a simple example of a feature request a beginner can hand to Codex before implementation starts.

## Example Request

```text
Feature: Enemy stun system

Goal:
Enemies should enter a stunned state for a short duration after receiving a heavy hit.

Desired behavior:
- Heavy attacks can trigger stun
- Stunned enemies cannot move or attack
- A visual indicator can appear while stunned
- After stun ends, the enemy returns to its normal state

Constraints:
- Keep gameplay logic in Assets/Scripts/Gameplay
- Keep UI and VFX separate from gameplay rules
- Do not hardcode stun duration or threshold values directly in logic
- Make the state transition explicit

Review request:
- First do a design review
- Then implement only after the structure looks good
```

## Why This Request Is Good

- It states the goal clearly
- It separates behavior from implementation detail
- It explains folder boundaries
- It asks for explicit state handling
- It warns against hardcoded tuning values

## What Codex Should Usually Do Next

1. Summarize the goal, touched area, and risks.
2. Review the design first.
3. Propose where state, tuning data, and UI updates should live.
4. Implement in a scoped way.
5. Run lightweight validation after the change.
