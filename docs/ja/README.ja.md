# Codex Unity Template 日本語ガイド

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/LICENSE)
[![codex-checks](https://github.com/teympa/codex-unity-template/actions/workflows/codex-checks.yml/badge.svg)](https://github.com/teympa/codex-unity-template/actions/workflows/codex-checks.yml)

これは、Unity 開発を Codex と一緒に進めるための配布用テンプレートです。

Git hooks、CI、レビュー用 skills、Unity 向けの運用ルールを最小構成でまとめています。新しい Unity プロジェクトの土台としてコピーしたり、GitHub の Template Repository として使うことを想定しています。

GitHub で `Use this template` を押して新しい repo を作り、そのあとセットアップ手順に沿って導入する使い方を想定しています。Unity 開発初心者でも、最初から構造を崩しにくい状態で Codex を使い始めやすくするためのテンプレートです。

[セットアップ](#最初に読むもの) | [使い方](#最初に読むもの) | [GitHubでの使い方](#github-の雛形-repo-として使う場合) | [ライセンス](#ライセンス)

## GitHub での最短導入

```text
Use this template
    -> 新しい repository を作る
    -> 作成した repo を開く
    -> docs/ja/SETUP.ja.md を読む
    -> hooks と validator を有効化する
    -> Codex と Unity 開発を始める
```

## 最初にやること

1. GitHub で `Use this template` を押す
2. このテンプレートから新しい Unity repo を作る
3. `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)` を読む
4. git hooks を有効化して validator を一度実行する

## 目次

- [このテンプレートでできること](#このテンプレートでできること)
- [最初に読むもの](#最初に読むもの)
- [含まれている主なファイル](#含まれている主なファイル)
- [想定している Unity 構成](#想定している-unity-構成)
- [GitHub の雛形 repo として使う場合](#github-の雛形-repo-として使う場合)
- [ライセンス](#ライセンス)

## このテンプレートでできること

- Codex 向けの repo 全体ルールを入れられる
- Gameplay と UI の責務境界を明確にしやすくなる
- 実装前レビューと実装後レビューを定型化できる
- gameplay コードに対する軽い静的チェックを入れられる
- commit 前、push 前、PR 時に最低限の検査を回せる

## 最初に読むもの

- セットアップ手順: `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)`
- 利用ガイド: `[docs/ja/USAGE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/USAGE.ja.md)`
- カスタマイズガイド: `[docs/ja/CUSTOMIZE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/CUSTOMIZE.ja.md)`
- 貢献ガイド: `[docs/ja/CONTRIBUTING.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/CONTRIBUTING.ja.md)`
- 依頼例: `[docs/ja/examples/CODEX_PROMPTS.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/examples/CODEX_PROMPTS.ja.md)`

## 含まれている主なファイル

- `AGENTS.md`
- `Assets/Scripts/Gameplay/AGENTS.md`
- `Assets/Scripts/UI/AGENTS.md`
- `skills/code-review/SKILL.md`
- `skills/design-review/SKILL.md`
- `scripts/validate_unity_gameplay.py`
- `.githooks/pre-commit`
- `.githooks/pre-push`
- `.github/workflows/codex-checks.yml`

## 想定している Unity 構成

- `Assets/Scripts/Gameplay/`
- `Assets/Scripts/UI/`
- `Assets/Scripts/Core/`
- `Assets/Scripts/Tests/`

既存プロジェクトの構成が違う場合は、ルールを消すのではなく、パスだけ慎重に合わせるのがおすすめです。

## GitHub の雛形 repo として使う場合

1. この repo を GitHub に push する
2. GitHub で Template Repository を有効にする
3. このテンプレートから新しい Unity repo を作る
4. 新しい repo 側でセットアップ手順を実行する

## ライセンス

このテンプレートは MIT License です。詳細は `[LICENSE](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/LICENSE)` を見てください。
