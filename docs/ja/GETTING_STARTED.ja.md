# はじめて使う人向けガイド

このガイドは、Unity 開発や Codex にまだ慣れていない人向けの、とても丁寧な導入ガイドです。

「このテンプレートを新しいゲーム開発でどう使い始めればいいのか」が分かるように、できるだけ順番に説明します。

## まず知っておくこと

このテンプレートは、Unity ゲーム開発を Codex と進めやすくするための土台です。

主に次の役割があります。

- Codex に守ってほしい作業ルールを伝える
- Gameplay と UI の役割を混ぜにくくする
- 実装前レビューと実装後レビューをやりやすくする
- 危なそうな gameplay コードを軽くチェックする

難しく見えるかもしれませんが、最初に全部理解しなくても大丈夫です。最初は「Codex が暴れすぎないようにするための最低限の道具が入っている」と思っておけば十分です。

## このテンプレートで使う主なもの

- `AGENTS.md`
  Codex がこの repo で作業するときの基本ルールです。
- `skills/`
  レビューや開始確認など、繰り返し使う手順です。
- `scripts/validate_unity_gameplay.py`
  gameplay コードの危なそうな書き方を軽く見つけるスクリプトです。
- `.githooks/`
  commit 前、push 前に自動で軽い確認をするための仕組みです。
- `.github/workflows/codex-checks.yml`
  GitHub 上でも同じような軽い確認をするための設定です。

## 一番最初にやること

やることは大きく分けて 5 つです。

1. Unity プロジェクトにこのテンプレートを入れる
2. Python が使えるか確認する
3. Git hooks を有効にする
4. validator を一度動かす
5. Codex に小さな作業を頼んでみる

## 手順 1. Unity プロジェクトにテンプレートを入れる

このテンプレート repo をそのまま使うか、必要なファイルを自分の Unity repo にコピーします。

最初は次が入っていれば十分です。

- `AGENTS.md`
- `.gitignore`
- `skills/`
- `scripts/`
- `.githooks/`
- `.github/workflows/`
- `Assets/Scripts/Gameplay/AGENTS.md`
- `Assets/Scripts/UI/AGENTS.md`

## 手順 2. Python が使えるか確認する

このテンプレートでは Python を 1 つ使います。難しいことには使っておらず、軽いチェック用です。

ターミナルで次を実行します。

```bash
python --version
```

もしエラーが出たら:

- Python 3 をインストールする
- もう一度 `python --version` を試す

## 手順 3. Git hooks を有効にする

次のコマンドをプロジェクトルートで実行します。

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
chmod +x .githooks/pre-push
```

意味は次の通りです。

- `core.hooksPath .githooks`
  Git に「このフォルダの hook を使ってください」と伝えます。
- `chmod +x ...`
  hook ファイルを実行できるようにします。

Windows で `chmod` が使いにくい場合は、Git Bash か WSL を使うとわかりやすいです。

## 手順 4. validator を一度動かす

次を実行します。

```bash
python scripts/validate_unity_gameplay.py
```

何が起きるか:

- `Assets/Scripts/Gameplay/` が無い場合
  まだ gameplay フォルダが無いので、チェックを飛ばします
- 問題が無い場合
  pass と表示されます
- 気になるコードがある場合
  どのファイルのどこが気になるかを出します

ここで findings が出ても、すぐに「全部ダメ」という意味ではありません。まずは「そこを確認しよう」という軽いサインです。

## 手順 5. Codex に小さな作業を頼んでみる

最初は小さな依頼から始めるのがおすすめです。

例:

```text
プレイヤーにスタミナ値を追加してください。
Assets/Scripts/Gameplay と Assets/Scripts/UI だけ触ってください。
UI は表示だけにして、gameplay ルールを UI に書かないでください。
```

このテンプレートでは、最初から大きな機能を丸投げするより、小さく区切って頼む方がうまくいきやすいです。

## 迷ったときのおすすめの順番

迷ったら、いつでも次の順番に戻ると進めやすいです。

1. まず何を作りたいかを 2〜3 行で書く
2. gameplay と UI のどちらが関係するか考える
3. 実装前に design-review が必要か考える
4. Codex に小さく実装を頼む
5. validator を回す
6. 実装後に code-review を頼む

## どのドキュメントをいつ読むか

- とにかく導入したいとき
  このファイル
- 実際のセットアップ手順を確認したいとき
  `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)`
- 普段どう使うか知りたいとき
  `[docs/ja/USAGE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/USAGE.ja.md)`
- project に合わせて調整したいとき
  `[docs/ja/CUSTOMIZE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/CUSTOMIZE.ja.md)`
- Codex への頼み方の例を見たいとき
  `[docs/ja/examples/CODEX_PROMPTS.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/examples/CODEX_PROMPTS.ja.md)`

## よくあるつまずき

### validator が怖い

大丈夫です。これは厳しい自動採点ではなく、軽い見張りです。findings が出たら、まずはその理由を Codex に聞くのがおすすめです。

### UI と gameplay の違いがまだよく分からない

最初はざっくりで十分です。

- gameplay
  ルール、状態、進行
- UI
  表示、入力、見た目

迷ったら「そのコードはゲームのルールを決めているか？」で考えると分かりやすいです。

### いきなり大きい機能を作りたくなる

気持ちは自然ですが、最初は小さく分けた方が失敗しにくいです。

- まず状態だけ作る
- 次に UI 表示を足す
- 最後に演出や微調整を足す

この順番の方が Codex との開発は安定しやすいです。

## 最後に

このテンプレートの目的は、「Codex に全部丸投げすること」ではありません。

目的は、Codex を使いながらも Unity の構造を崩しにくくし、あとから直しやすいゲーム開発を進めることです。

最初は完璧を目指さず、次の 1 つだけ覚えておけば十分です。

「小さく頼む、ルールを守る、レビューを挟む」
