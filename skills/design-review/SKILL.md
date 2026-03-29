---
name: design-review
description: Review Unity gameplay design before implementation for rule clarity, state transitions, data ownership, and UI-gameplay boundaries.
---

# Purpose

Use this skill before implementation to review gameplay design quality even when code does not exist yet. It is intended to be copied with this template into new Unity repositories.

## How To Review

1. Read the proposed feature or design description in full.
2. Read the relevant `AGENTS.md` guidance before judging structure.
3. Review data ownership, state flow, and class boundaries first.
4. Push unclear responsibilities or hidden coupling back into the design phase.

## Checklist

- Are game rules and presentation concerns separated?
- Is the owner of game state explicit?
- Is UI being asked to hold or decide gameplay rules?
- Can balance values live in ScriptableObjects or data definitions instead of code?
- Are state transitions explicit?
- Does the design overuse `Update` or `FixedUpdate`?
- Is the design easy to test through separation of pure logic?
- Is too much responsibility being concentrated in a single `MonoBehaviour`?
- Will future tuning and extension remain practical?
- Can each class responsibility be explained in one or two lines?

## Output Format

### Summary

Short assessment of the proposed design and whether implementation should start.

### Strong Points

Call out decisions that support maintainability or clarity.

### Risks

List the main structural or design risks.

### Required Changes Before Implementation

List design corrections that should happen first.

### Suggested Structure

Propose a cleaner split of data, orchestration, gameplay logic, and UI if needed.

### Verdict

State `Ready`, `Ready with adjustments`, or `Not ready`.
