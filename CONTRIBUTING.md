# Contributing

This repository is a starter template for Unity development with Codex.

The goal is to keep it small, practical, and easy for beginners to adopt. Please prefer simple improvements over adding a lot of process.

## What To Update

Good contributions include:

- clearer setup instructions
- better beginner guidance
- safer Unity architecture rules
- lower-noise validator improvements
- better examples for using Codex in Unity projects

## Before You Change Things

1. Keep the template reusable across many Unity projects.
2. Avoid project-specific assumptions unless they are clearly marked as examples.
3. Keep hooks and CI lightweight.
4. Prefer guidance and light guardrails over strict automation.

## Change Guidelines

- Keep `AGENTS.md` short and practical.
- Put repeatable review workflows in `skills/`.
- Put mechanical checks in hooks or CI.
- Avoid adding dependencies unless they are clearly necessary.
- Do not mix large refactors with unrelated documentation changes.

## Recommended Contribution Flow

1. If the change affects feature structure, review the design first.
2. Make a small scoped update.
3. Run:

```bash
python scripts/validate_unity_gameplay.py
```

4. If you changed docs, skim them once as if you were a beginner.
5. Open a pull request with a short summary of:
   - what changed
   - why it helps
   - anything a user may need to customize

## Pull Request Checklist

- The change keeps the template reusable.
- The instructions are understandable for a beginner.
- The validator and hooks stay lightweight.
- Paths and examples still match the intended folder layout.
- Any new rules are explained clearly.

## Optional Improvements

These are good follow-up areas when the template grows:

- more examples under `docs/examples/`
- stricter but still low-noise validation rules
- team workflow docs for review habits
