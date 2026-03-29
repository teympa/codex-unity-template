# Setup Guide

This guide explains how to put this template into a Unity project and get the basic checks working.

## 1. Put The Template In Your Project

Copy these files and folders into the root of your Unity repository:

- `AGENTS.md`
- `skills/`
- `scripts/`
- `.githooks/`
- `.github/workflows/`
- `Assets/Scripts/Gameplay/AGENTS.md`
- `Assets/Scripts/UI/AGENTS.md`

Your project root should end up looking roughly like this:

```text
YourUnityProject/
  Assets/
    Scripts/
      Gameplay/
      UI/
      Core/
      Tests/
  .github/
  .githooks/
  skills/
  scripts/
  AGENTS.md
```

## 2. Make Sure Python Is Available

This template uses Python for the lightweight gameplay validator.

Check it with:

```bash
python --version
```

If that does not work, install Python 3 and try again.

## 3. Enable Git Hooks

Run these commands in the project root:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
chmod +x .githooks/pre-push
```

If you are on Windows and `chmod` does not work, run those commands in Git Bash or WSL.

## 4. Run The Validator Once

```bash
python scripts/validate_unity_gameplay.py
```

Expected behavior:

- If `Assets/Scripts/Gameplay/` does not exist yet, the script prints a skip message.
- If gameplay scripts exist and no findings are detected, it prints a pass message.
- If findings are detected, it prints them and exits with code `1`.

## 5. Confirm GitHub Actions Will Run

If your project uses GitHub, this workflow will run automatically:

- On pull requests
- On pushes to `main`
- On pushes to `develop`

The workflow file is `[.github/workflows/codex-checks.yml](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/.github/workflows/codex-checks.yml)`.

## 6. Recommended First Test

After setup:

1. Create or open a small script under `Assets/Scripts/Gameplay/`.
2. Run `python scripts/validate_unity_gameplay.py`.
3. Make a small git commit and confirm the pre-commit hook runs.

If that works, the template is ready.
