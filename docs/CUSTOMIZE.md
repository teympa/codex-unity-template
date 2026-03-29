# Customization Guide

This guide explains what you can safely customize when using this template as a base repository.

## Safe Customizations

- Change wording in `AGENTS.md` to match your team tone
- Add project-specific review points
- Extend `scripts/validate_unity_gameplay.py` with more heuristic checks
- Change CI trigger branches
- Add more local `AGENTS.md` files for other folders

## Customizations To Treat Carefully

- Changing the script folder layout
- Removing the gameplay and UI boundary rules
- Making the validator fail on too many noisy patterns
- Turning hooks into heavy build steps

Those changes can make the template harder to reuse or more frustrating for beginners.

## If Your Project Uses Different Script Paths

By default, the validator checks:

```text
Assets/Scripts/Gameplay/
```

If your project uses another location, update `[scripts/validate_unity_gameplay.py](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/scripts/validate_unity_gameplay.py)` carefully instead of deleting the check.

## Suggested Repo-Level Tweaks

- Add a short project overview to `README.md`
- Add links to your issue tracker or task board
- Add Unity version information
- Add test commands if your repo already has them

## Suggested Team-Level Tweaks

- Decide when `design-review` is mandatory
- Decide when `code-review` is mandatory
- Decide which findings are blockers versus warnings

## Keep The Template Lightweight

This starter is intentionally small. If you add many custom rules, try to keep:

- the repo-wide AGENTS short
- the validator understandable
- the hooks fast
- the beginner path simple
