---
name: code-review
description: Review Unity gameplay code for responsibility boundaries, hardcoded values, update-loop performance, and Unity-specific risks.
---

# Purpose

Use this skill to review Unity gameplay-oriented code against the repository `AGENTS.md` guidance. It is written to work as a reusable template skill across Unity projects that adopt this starter kit.

## How To Review

1. Read every target file in full before judging the change.
2. Read the nearest applicable `AGENTS.md` files and use them as the review baseline.
3. Focus on behavior risk, structure drift, and Unity-specific maintenance issues.
4. Prefer concrete findings with file references and actionable fixes.

## Use Cases

- New gameplay implementation
- Player, Enemy, Combat, or State changes
- UI and Gameplay boundary changes
- Larger refactors
- Changes with performance concerns
- Changes where `MonoBehaviour` growth is becoming a concern

## Checklist

- Are responsibilities mixed across rule handling, presentation, and orchestration?
- Are gameplay values hardcoded instead of coming from ScriptableObjects or config data?
- Does UI own game state?
- Does gameplay depend on UI types or direct UI control?
- Are `Time.deltaTime` and `FixedUpdate` used appropriately?
- Is there unnecessary work in `Update`, `FixedUpdate`, or `LateUpdate`?
- Is there per-frame `GetComponent`, LINQ, allocation, or string work?
- Is the code adding `FindObjectOfType`, `FindAnyObjectByType`, `GameObject.Find`, or risky singleton reliance?
- Are state transitions easy to follow and explicit?
- Is the logic structured in a way that is testable?
- Is a `MonoBehaviour` taking on too many responsibilities?
- Should hardcoded values be moved into ScriptableObjects or other configuration data?

## Output Format

### Summary

Short overview of what changed and the overall review result.

### Positive Observations

Call out concrete things that align with the repo rules.

### Required Changes

List blocking issues that should be addressed before merge.

### Suggested Improvements

List non-blocking improvements that would reduce future risk.

### Risk Level

State `Low`, `Medium`, or `High` with a short reason.

### Verdict

State `Approve`, `Approve with follow-ups`, or `Request changes`.
