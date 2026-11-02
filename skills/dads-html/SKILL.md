---
name: dads-html
description: デジタル庁デザインシステム(DADS)のHTMLコンポーネントを使って、CSS/JSをすべてインライン化したスタンドアロンの単一HTMLファイルを作成する。行政・公共サービス風のページ、フォーム、申請画面、お知らせページ、ランディングページ、モックアップなどを「デジタル庁デザインシステムで」「DADSで」「デジタル庁っぽく」作ってほしいと頼まれたときに使う。
---

# DADS スタンドアロンHTML作成

デジタル庁デザインシステム コードスニペット（HTML版）を使い、外部ファイルに依存しない1枚のHTMLを作る。

このファイルのあるディレクトリを `SKILL_DIR` と呼ぶ。以下のパスはすべて `SKILL_DIR` からの相対パス。

- `dads/` — 公式リポジトリの `src/`（git submodule へのシンボリックリンク）。**正本はここ**
  - `dads/global.css` — デザイントークン・ベーススタイル・テキストユーティリティ
  - `dads/components/<name>/` — `<name>.md`（仕様・使い方）、サンプル `*.html`、`*.css`、`*.js`
- `references/components.md` — 全コンポーネントの一覧（名称・CSS・カスタム要素・サンプル）
- `references/foundations.md` — カラートークン・タイポグラフィ・CSS規約の要約
- `assets/template.html` — 下書きの雛形
- `scripts/build_standalone.py` — 下書きからスタンドアロンHTMLを生成（Python 3.9+, 標準ライブラリのみ）

`dads/components` が空なら、リポジトリで `git submodule update --init` が必要とユーザーに伝える。

## 手順

### 1. 使うコンポーネントを決める

`references/components.md` を読み、要件に合うコンポーネントを選ぶ。
ページのレイアウトやトークンの使い方は `references/foundations.md` を読む。

### 2. 選んだコンポーネントの仕様とサンプルを読む

各コンポーネントについて **必ず** 以下を読んでからマークアップを書く。記憶や推測でクラス名・属性を書かない。

1. `dads/components/<name>/<name>.md` — バリエーション（`data-*` 属性）、使い方、アクセシビリティ上の注意
2. 近いサンプル `dads/components/<name>/*.html` の `<body>` 部分 — これをコピーして中身を差し替えるのが基本

`.md` 中の `[xxx.html](./xxx.html#.selector)` は「そのサンプルのそのセレクタの部分を見よ」という意味。
サンプルの `<head>` にある `<link>` は依存コンポーネントのヒントになる（例: フォーム部品は `form-control-label` と組み合わせる）。

### 3. 下書きHTMLを書く

`assets/template.html` をコピーして出力先の近くに下書き（例: `page.draft.html`）を作り、`<body>` を組み立てる。

- `<!-- dads:assets -->` マーカーは残す（ここにCSS/JSが挿入される）
- DADS の CSS/JS を `<link>`/`<script src>` で読み込む必要はない（書いてもビルド時に除去される）
- コンポーネントのマークアップ構造・クラス名・`data-*` 属性・ARIA 属性はサンプルどおりに保つ
- JS付きコンポーネントはカスタム要素（`<dads-tab>` 等）で包む構造をサンプルどおりに書く
- ページ固有のCSSは template の `<style>` に書く。色・影・フォントは必ずトークン変数を使い、独自クラスに `dads-` 接頭辞は付けない
- 文字サイズは `dads-u-std-*` 等のテキストユーティリティクラスで指定する
- 画像はユーザー指定がなければ使わない。アイコンはサンプル内のインライン `<svg>` を流用する
- アクセシビリティ: 見出し階層を飛ばさない、フォームには必ずラベル、装飾SVGに `aria-hidden="true"`、`lang="ja"`

### 4. スタンドアロンHTMLを生成する

```bash
python3 SKILL_DIR/scripts/build_standalone.py page.draft.html -o page.html
```

- 使われている `dads-*` クラスとカスタム要素から必要な CSS/JS を自動判定し、global.css と共に `<style>` / `<script type="module">` としてインライン化する
- stderr の `included:` で取り込まれたファイルを確認する
- `warning: unknown DADS class` / `unknown DADS element` が出たら **タイポか存在しないクラス**。サンプルを読み直して修正し、再ビルドする
- `warning: local asset is not inlined` は相対パスの外部ファイル参照が残っている。インライン化するか削除する
- クラス名からは判定できないコンポーネントを強制的に含めたい場合は `-c <name>` を付ける（複数可）

最終成果物は生成された `page.html` の1ファイル。下書きは、ユーザーが残したいと言わない限り削除してよい。
Google Fonts の `<link>` のみ外部参照として残る（オフラインでもフォールバックフォントで表示される）。

### 5. 確認する

可能ならブラウザで開いて表示を確認する（例: macOS なら `open page.html`、
ヘッドレスChromeが使えればスクリーンショットを撮って崩れを確認）。
JS付きコンポーネント（タブ、日付ピッカー、ファイルアップロード等）はクリック等で動作することも確認する。

## 修正依頼への対応

生成済みHTMLは直接編集して、同じスクリプトで再ビルドしてよい（入力と出力が同じファイルでも可）。
スクリプトは `data-dads` 属性の付いた `<style>` / `<script>`（前回インライン化した資材）を取り除いてから組み直すので、
コンポーネントの追加・削除に追従し、二重に埋め込まれることはない。
インライン化された `data-dads` 付きブロックの中身は編集しない（再ビルドで上書きされる）。
大きなファイルなので、編集時は `<body>` やページ固有 `<style>` の該当箇所だけを読む。

## サブモジュールの更新（メンテナンス）

```bash
git submodule update --remote vendor/design-system-example-components-html
python3 SKILL_DIR/scripts/gen_catalog.py   # references/components.md を再生成
```
