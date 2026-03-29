# Upgrading This Template

This template is meant to be copied into new Unity repositories, so it helps to have a simple rule for pulling in improvements later.

## Recommended Upgrade Approach

1. Compare your project against the latest template repository.
2. Pull in template-only changes first:
   - docs
   - `AGENTS.md`
   - `skills/`
   - `scripts/`
   - `.githooks/`
   - `.github/workflows/`
3. Review path assumptions before copying validator or hook changes.
4. Keep project-specific gameplay code separate from template updates.
5. Re-run setup and validation after merging updates.

## What Usually Upgrades Cleanly

- `AGENTS.md`
- docs
- review skills
- validator improvements
- git hooks
- CI workflow tweaks

## What Needs Extra Care

- Folder path changes
- New strict validator rules
- Changes to git hook behavior
- Any instructions that assume a new team workflow

## Suggested Upgrade Checklist

- Read the latest `README.md`
- Read `docs/CUSTOMIZE.md`
- Re-check `scripts/validate_unity_gameplay.py`
- Re-run:

```bash
python scripts/validate_unity_gameplay.py
```

- Re-check:

```bash
git config core.hooksPath .githooks
```

## Keep Local Ownership Clear

If your Unity repo has project-specific additions, prefer merging template improvements manually instead of overwriting files blindly.
