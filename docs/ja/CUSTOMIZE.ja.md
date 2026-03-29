# カスタマイズガイド

このガイドでは、このテンプレートを各 Unity プロジェクト向けに調整するときの考え方を説明します。

## 安全にカスタマイズしやすい場所

- `AGENTS.md` の文言をチーム向けに調整する
- project 固有の review 観点を追加する
- `scripts/validate_unity_gameplay.py` に軽い検査を足す
- CI の対象ブランチを変える
- 他のフォルダ向けにローカル `AGENTS.md` を増やす

## 慎重に扱いたい変更

- script フォルダ構成の大幅変更
- gameplay と UI の責務境界ルールを弱める変更
- ノイズの多い validator への変更
- hooks に重い build や長時間処理を入れる変更

これらは、テンプレートの再利用性や初心者の使いやすさを落としやすいです。

## script パスが違う場合

デフォルトでは validator は次を見ます。

```text
Assets/Scripts/Gameplay/
```

別の構成を使う場合は、ルールを消すのではなく、`[scripts/validate_unity_gameplay.py](c:/Users/teymp/OneDrive/ドキュメント/codex/codex_unity_rules/scripts/validate_unity_gameplay.py)` の対象パスを丁寧に合わせるのがおすすめです。

## repo レベルで追加すると良いもの

- project 概要
- Unity バージョン情報
- issue tracker や task board へのリンク
- 既存 test コマンド
- Unity の editor や運用に合わせた `.gitignore` の微調整

## チームで決めると運用しやすいもの

- `design-review` を必須にする場面
- `code-review` を必須にする場面
- validator findings のうち何を blocker とみなすか

## 軽さは残す

このテンプレートは小さいことが価値です。カスタマイズするときも次はなるべく保つのがおすすめです。

- repo 全体の AGENTS は短くする
- validator は読める範囲に保つ
- hooks は速くする
- 初学者でも追える導線を残す
