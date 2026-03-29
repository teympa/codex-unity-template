# UI Local Rules

- UI should focus on presentation and input bridging.
- UI must not own game state.
- Do not place gameplay rule logic in UI code.
- Do not mix view updates and rule mutations in the same class.
- Do not put long gameplay logic directly behind button click handlers.
- Keep display strings replaceable in the future.
- Prefer UI updates driven by gameplay notifications or state changes.
