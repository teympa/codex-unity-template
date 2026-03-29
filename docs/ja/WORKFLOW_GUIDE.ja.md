# ゲーム開発ワークフローガイド

このガイドでは、このテンプレートを使って Codex と Unity ゲーム開発をどう進めるかを、できるだけ丁寧に説明します。

特に、「機能を思いついてから完成まで、何をどの順番でやるか」を分かりやすくすることが目的です。

## まず全体像

このテンプレートを使った開発では、基本的に次の流れで進めます。

1. 作りたい機能を言葉にする
2. 実装前に設計を軽く整理する
3. Codex に小さな単位で実装してもらう
4. validator と review で崩れを減らす
5. 必要なら調整して仕上げる

これは少し遠回りに見えるかもしれませんが、結果的に手戻りが減りやすく、構造も崩れにくいです。

## ワークフロー 1. 作りたい機能を言葉にする

いきなりコードを書き始める前に、まずは次の 3 つを言葉にします。

- 何を作りたいか
- プレイヤーに何が起きるか
- どこを触りそうか

例:

- プレイヤーにスタミナを追加したい
- ダッシュや回避でスタミナが減る
- Gameplay と UI を触りそう

これだけでも、Codex はかなり動きやすくなります。

## ワークフロー 2. 実装前に設計を軽く整理する

仕様が少しでも複雑そうなら、実装前に `design-review` を使うのがおすすめです。

特に次のような機能は、先に設計を見た方が安全です。

- 状態遷移がある
- Player / Enemy / Combat に関わる
- UI と gameplay の両方を触る
- 調整値が多い

もし仕様整理が苦手なら、まずは `[docs/ja/templates/FEATURE_DESIGN_TEMPLATE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/templates/FEATURE_DESIGN_TEMPLATE.ja.md)` を埋めるところから始めるとやりやすいです。

## ワークフロー 3. Codex に実装を頼む

Codex に頼むときは、次の 4 つを入れると安定しやすいです。

- 機能の目的
- 触ってよい範囲
- 守ってほしい制約
- 必要なら review の依頼

例:

```text
プレイヤーにスタミナシステムを追加してください。
Assets/Scripts/Gameplay と Assets/Scripts/UI だけ触ってください。
バランス値はコードへ直書きしないでください。
UI は表示だけにして、gameplay のルールを持たせないでください。
```

## ワークフロー 4. 小さな単位で進める

ここがとても大事です。

このテンプレートでは、1 回で全部作るより、次のように小さく分ける方が向いています。

悪い例:

- スタミナ、ダッシュ、UI、SE、アニメーション、エフェクトを一気に追加する

良い例:

1. gameplay 上のスタミナ状態だけ作る
2. UI でスタミナを表示する
3. ダッシュと接続する
4. 演出や調整を足す

このやり方だと、どこで壊れたか分かりやすく、Codex も安定して作業しやすいです。

## ワークフロー 5. 実装後に validator を回す

実装後は次を実行します。

```bash
python scripts/validate_unity_gameplay.py
```

このチェックは、よくある Unity の崩れ方を軽く見ています。

例えば:

- gameplay 値の直書き
- `FindObjectOfType` などの参照増加
- `Update` での無駄な処理
- 毎フレームの `GetComponent`

結果の見方:

- pass
  まずは問題なし
- findings あり
  該当箇所を見直す。必要なら Codex に理由を説明してもらう

## ワークフロー 6. 実装後に code-review を使う

機能がひとまずできたら、`code-review` を使うのがおすすめです。

特に次の変更では効果が大きいです。

- 新しい gameplay 実装
- Player / Enemy / Combat / State 変更
- `Update` を触る変更
- `MonoBehaviour` が大きくなった変更

見るポイントは主に次です。

- 責務分離
- 直書き値の増加
- UI と gameplay の混線
- state 管理の分かりやすさ
- 毎フレーム処理の無駄

## ワークフロー 7. 調整と仕上げ

review の結果、少し直した方が良い点が出ることがあります。

そのときは、また小さく直します。

おすすめの考え方:

- まず危険なところを直す
- 次に構造を整える
- 最後に見た目や演出を整える

リファクタと仕様変更を一気にやりすぎないのがポイントです。

## 日常のおすすめ運用

毎回、次の流れを意識するとかなり安定します。

1. 作るものを短く書く
2. 必要なら design-review
3. 小さく実装
4. validator 実行
5. code-review
6. commit / push

## 何を Codex に任せて、何を自分で決めるか

Codex に任せやすいもの:

- 小から中規模の実装
- 既存コード整理
- review
- 仕様の整理補助
- 危険そうな箇所の洗い出し

自分で決めた方がよいもの:

- ゲームの面白さの方向性
- 仕様の最終判断
- どこまで作るか
- スコープ管理

Codex は強い補助役ですが、ゲームの方向性そのものを自動で決める役ではありません。

## よくある失敗と避け方

### 失敗 1. いきなり大きく頼む

避け方:

- 1 機能を 3〜4 段階に分ける

### 失敗 2. UI に gameplay を書く

避け方:

- 「そのコードはルールを決めているか？」で考える
- ルールなら gameplay 側に置く

### 失敗 3. 数値を全部コードに直書きする

避け方:

- 調整しそうな値は ScriptableObject や設定クラスへ寄せる

### 失敗 4. `Update` に何でも入れる

避け方:

- event でできないか考える
- 本当に毎フレーム必要か考える

### 失敗 5. review を飛ばす

避け方:

- 小さくても `design-review` か `code-review` を挟む習慣をつける

## 初心者向けのおすすめスタート

最初の 1 週間くらいは、次のような小さいテーマで練習するのがおすすめです。

- HP バー表示
- スタミナ表示
- シンプルな cooldown
- 状態異常 1 種類
- 敵の簡単な state 切り替え

これらは gameplay、UI、state、レビューの流れを学びやすいです。

## 困ったときの戻り先

困ったら次のどれかに戻ると整理しやすいです。

- `[docs/ja/GETTING_STARTED.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/GETTING_STARTED.ja.md)`
- `[docs/ja/SETUP.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/SETUP.ja.md)`
- `[docs/ja/USAGE.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/USAGE.ja.md)`
- `[docs/ja/examples/CODEX_PROMPTS.ja.md](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/docs/ja/examples/CODEX_PROMPTS.ja.md)`

## 最後に

このテンプレートで大事なのは、「AI に全部やらせること」ではなく、「AI と一緒に崩れにくく作ること」です。

そのための基本はとてもシンプルです。

- 小さく頼む
- 役割を混ぜない
- review を挟む
- 毎フレーム処理を雑に増やさない

この 4 つを意識するだけでも、かなり安定します。
