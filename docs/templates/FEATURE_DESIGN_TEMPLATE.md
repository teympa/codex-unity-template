# Feature Design Template

Use this template before implementation when a gameplay feature is still being designed.

## Feature Name

Short name of the feature.

## Goal

What player-facing outcome should this feature create?

## Desired Behavior

- What should happen?
- When should it happen?
- What should not happen?

## State Ownership

- Which class or system owns the game state?
- Which system is only observing or rendering it?

## Gameplay And UI Boundary

- What belongs in gameplay?
- What belongs in UI?
- How will UI learn about gameplay changes?

## Data And Tuning

- Which values should be configurable?
- Should they live in ScriptableObjects, config classes, or other data assets?

## State Transitions

- What are the main states?
- What causes transitions between them?
- Should they be represented by enum, state classes, or a state machine?

## Update Loop Considerations

- Does this feature require `Update`, `FixedUpdate`, or `LateUpdate`?
- Can event-driven updates reduce per-frame cost?

## Testing Approach

- Which parts can be pure logic?
- What can be tested without `MonoBehaviour`?

## Risks

- What is most likely to become messy or expensive later?

## Review Request

- Ask for `design-review` before implementation
- Ask for `code-review` after implementation
