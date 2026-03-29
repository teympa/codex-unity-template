# Gameplay Local Rules

- Keep `MonoBehaviour` classes thin and move pure logic into separate classes.
- Move balance values into ScriptableObjects or configuration data.
- Make state transitions explicit with `enum`, state classes, or state machines.
- Do not push heavy work into update loops.
- Avoid per-frame lookups, per-frame `GetComponent`, LINQ, and large allocations.
- Do not control UI directly from gameplay code.
- Do not mix presentation effects and gameplay rule evaluation more than necessary.
- Keep logic testable without `MonoBehaviour` when practical.
