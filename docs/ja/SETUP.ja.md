# セットアップガイド

このガイドでは、このテンプレートを Unity プロジェクトに入れて、最低限のチェックが動くまでの手順を説明します。

「まず何から始めればいいか」をもっとやさしく追いたい場合は、先に `[docs/ja/GETTING_STARTED.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/GETTING_STARTED.ja.md)` を読むのがおすすめです。

## 1. テンプレートを Unity プロジェクトへ入れる

次のファイルとフォルダを Unity repo のルートへコピーします。

- `AGENTS.md`
- `.gitignore`
- `skills/`
- `scripts/`
- `.githooks/`
- `.github/workflows/`
- `Assets/Scripts/Gameplay/AGENTS.md`
- `Assets/Scripts/UI/AGENTS.md`

おおよそ次のような構成になります。

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
  .gitignore
  AGENTS.md
```

## 2. Python が使えるか確認する

このテンプレートでは、軽量な gameplay 検査に Python を使います。

```bash
python --version
```

動かない場合は Python 3 を入れてからやり直してください。

## 3. Git hooks を有効にする

プロジェクトルートで次を実行します。

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
chmod +x .githooks/pre-push
```

Windows で `chmod` が使いにくい場合は、Git Bash か WSL で実行すると楽です。

## 4. バリデータを一度実行する

```bash
python scripts/validate_unity_gameplay.py
```

期待される動作:

- `Assets/Scripts/Gameplay/` がまだ無ければ skip 表示
- 問題が見つからなければ pass 表示
- 気になる実装が見つかれば一覧表示して終了コード `1`

## 5. GitHub Actions が動くことを確認する

GitHub を使う場合、この workflow は次で動きます。

- pull request
- `main` への push
- `develop` への push

workflow ファイルは `[.github/workflows/codex-checks.yml](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/.github/workflows/codex-checks.yml)` です。

## 6. 最初の動作確認

セットアップ後は次を試すのがおすすめです。

1. `Assets/Scripts/Gameplay/` に小さなスクリプトを置く
2. `python scripts/validate_unity_gameplay.py` を実行する
3. 小さな commit を作って pre-commit hook が動くか確認する

ここまで動けば、テンプレートの基本導入は完了です。
