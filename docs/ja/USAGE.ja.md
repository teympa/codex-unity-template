# 利用ガイド

このガイドでは、このテンプレートを使って Unity 開発を Codex と進める基本的な流れを説明します。

より丁寧な日常開発の流れを見たい場合は、`[docs/ja/WORKFLOW_GUIDE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/WORKFLOW_GUIDE.ja.md)` もあわせて読んでください。

## 基本の考え方

このテンプレートは 3 層に役割を分けています。

- `AGENTS.md`: Codex の作業ルール
- `skills/`: 繰り返し使うレビュー手順
- hooks と CI: 機械的な軽いチェック

加えて、開始時の入口として次も用意しています。

- `start-project`: 新規導入や既存 repo 取り込み時の最初の確認用

使い分けの目安:

- 実装ルールや責務境界は `AGENTS.md`
- 毎回似た観点で見るレビューは `skills/`
- 明らかな危険パターンの検出は hooks と CI

## Codex への頼み方

Codex へ依頼するときは、次を入れると安定しやすいです。

- 何を作りたいか
- どのファイルやフォルダを触るか
- 重要な制約

例:

```text
プレイヤーにスタミナ制を追加してください。
Assets/Scripts/Gameplay と Assets/Scripts/UI だけ触ってください。
UI に gameplay ルールを書かず、バランス値は直書きしないでください。
```

## design-review を使うタイミング

次のようなときは、実装前に `design-review` を使うのがおすすめです。

- 仕様がまだ曖昧
- game state の持ち主が曖昧
- 状態遷移が多い
- UI と gameplay の境界が怪しい

見るポイント:

- state ownership
- UI と gameplay の責務分離
- バランス値の置き場
- テストしやすい構造か

repo 自体の準備がまだ怪しい場合は、先に `start-project` を使って「次にやるべき最小の安全な一手」を出してもらうのがおすすめです。

## code-review を使うタイミング

次のようなときは、実装後に `code-review` を使うのがおすすめです。

- gameplay コードを追加した
- Player / Enemy / Combat / State を変えた
- `Update` / `FixedUpdate` / `LateUpdate` を触った
- `MonoBehaviour` が大きくなってきた

## バリデータが見るもの

`[scripts/validate_unity_gameplay.py](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/scripts/validate_unity_gameplay.py)` は `Assets/Scripts/Gameplay/**/*.cs` を見て、次のようなものを検出します。

- 怪しい直書き数値
- `GameObject.Find`
- `FindObjectOfType`
- `FindAnyObjectByType`
- `public static Instance` 形式の singleton 増加
- 毎フレームの `GetComponent`
- `Update` などの中の LINQ
- 毎フレームの文字列連結

これは「軽い柵」です。findings が出たら必ず悪いという意味ではなく、「そこは一度ちゃんと見よう」という意味です。

## おすすめの日常フロー

1. まず design-review が必要か判断する
2. 小さめの単位で Codex に実装を依頼する
3. `python scripts/validate_unity_gameplay.py` を実行する
4. commit / push 時に hooks を通す
5. merge 前に `code-review` を使う

## このテンプレートが減らしたい事故

- UI に gameplay ルールを書いてしまう
- 1 つの `MonoBehaviour` に責務が集まりすぎる
- ダメージや cooldown をコードへ直書きする
- 毎フレーム無駄な処理をしてしまう
- state 遷移が bool だらけで追いにくくなる
