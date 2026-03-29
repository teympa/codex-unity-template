# テンプレート更新ガイド

このテンプレートは他の Unity repo にコピーして使う前提なので、あとから改善を取り込むときの考え方を決めておくと運用が楽です。

## おすすめの更新手順

1. 使っている Unity repo と最新テンプレートを見比べる
2. まずテンプレート専用ファイルだけを取り込む
   - docs
   - `AGENTS.md`
   - `skills/`
   - `scripts/`
   - `.githooks/`
   - `.github/workflows/`
3. validator や hooks のパス前提が合っているか確認する
4. project 固有の gameplay 実装と混ぜすぎない
5. 取り込み後にセットアップと検査をやり直す

## 比較的取り込みやすいもの

- `AGENTS.md`
- docs
- review skill
- validator の改善
- git hooks
- CI workflow の調整

## 慎重に見るべきもの

- フォルダパスの変更
- 厳しすぎる validator ルール
- git hook の挙動変更
- チーム運用前提を増やす変更

## 更新チェックリスト

- 最新の `README.md` を読む
- `docs/ja/CUSTOMIZE.ja.md` を読む
- `scripts/validate_unity_gameplay.py` の変更点を確認する
- 次を実行する

```bash
python scripts/validate_unity_gameplay.py
```

- 次も確認する

```bash
git config core.hooksPath .githooks
```

## project 側の所有を守る

project 固有の追加がある場合は、テンプレートの更新を丸ごと上書きせず、手動で取り込む方が安全です。
