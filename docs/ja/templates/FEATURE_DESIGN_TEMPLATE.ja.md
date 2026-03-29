# 機能設計テンプレート

gameplay 機能を実装する前に、仕様整理用として使うテンプレートです。

## 機能名

機能の短い名前

## 目的

プレイヤー体験として何を実現したいか

## 期待する挙動

- 何が起きるか
- いつ起きるか
- 何は起きてほしくないか

## state の所有者

- game state をどのクラスやシステムが持つか
- どのシステムは観測や表示だけを行うか

## Gameplay と UI の境界

- gameplay に置くもの
- UI に置くもの
- UI は gameplay 変更をどう受け取るか

## データと調整値

- 設定可能にしたい値は何か
- ScriptableObject、設定クラス、データ asset のどこに置くか

## 状態遷移

- 主な状態は何か
- 何が遷移のきっかけになるか
- enum、state class、state machine のどれが合うか

## Update まわりの考慮

- `Update`、`FixedUpdate`、`LateUpdate` が本当に必要か
- event 駆動で減らせないか

## テスト方針

- 純粋ロジックに分けられる箇所はどこか
- `MonoBehaviour` 非依存でテストできる部分はどこか

## リスク

- 将来崩れやすそうな点はどこか

## レビュー依頼

- 実装前に `design-review` を依頼する
- 実装後に `code-review` を依頼する
