# ファンデーション（トークン・タイポグラフィ・ベーススタイル）

正本は `dads/global.css`。ここは要約なので、値が必要なら global.css を grep すること。
ビルドスクリプトが global.css を必ずインライン化するため、以下の変数・クラスは常に利用できる。

## カラートークン（CSSカスタムプロパティ）

ページ独自のCSSを書くときは **生の色コードではなく必ずこれらの変数を使う**。

| 用途 | 変数 |
| --- | --- |
| キーカラー（ブランド青） | `--color-key-50` 〜 `--color-key-1200`（= primitive blue） |
| 本文テキスト | `--color-neutral-solid-gray-800` |
| 補助テキスト | `--color-neutral-solid-gray-600` / `-700` |
| 境界線 | `--color-neutral-solid-gray-420`（コントロール）, `-200`/`-300`（区切り線） |
| 背景（薄いグレー） | `--color-neutral-solid-gray-50` / `-100` |
| 白・黒 | `--color-neutral-white`, `--color-neutral-black` |
| 成功 | `--color-semantic-success-1`, `-2` |
| エラー | `--color-semantic-error-1`, `-2` |
| 警告 | `--color-semantic-warning-yellow-1`, `-2`, `--color-semantic-warning-orange-1`, `-2` |
| 透過グレー | `--color-neutral-opacity-gray-50` 〜 `-900` |

プリミティブ: `--color-primitive-{blue,light-blue,cyan,green,lime,yellow,orange,red,magenta,purple}-{50,100,200,…,1200}`

コントラスト: テキストと背景は WCAG 2.2 AA（通常文字 4.5:1 以上）を満たすこと。
白背景上のテキストは gray-536 (`#767676`, 4.54:1) 以上の濃さにする。

## エレベーション（影）

`--elevation-1` 〜 `--elevation-8`（`box-shadow` に指定）。カード等の浮き上がりに使う。

## フォント

- `--font-family-sans`: `"Noto Sans JP", -apple-system, BlinkMacSystemFont, sans-serif`（`html` に適用済み）
- `--font-family-mono`: `"Noto Sans Mono", monospace`

Noto Sans JP は Google Fonts から読み込む（テンプレートに記載済み）。オフラインでもフォールバックで表示は崩れない。

## テキストスタイル ユーティリティクラス

命名: `dads-u-{種別}-{サイズpx}{B|N}-{行間×100}`（B=bold, N=normal）。`!important` 付き。

| 種別 | 用途 | クラス |
| --- | --- | --- |
| `dsp` (Display) | ヒーロー等の特大見出し | `dsp-64`, `dsp-57`, `dsp-48` × `B/N` × `140` |
| `std` (Standard) | 見出し・本文 | `std-45{B,N}-140`, `std-36{B,N}-140`, `std-32{B,N}-150`, `std-28{B,N}-150`, `std-26{B,N}-150`, `std-24{B,N}-150`, `std-22{B,N}-150`, `std-20{B,N}-150`, `std-18{B,N}-160`, `std-17{B,N}-170`, `std-16{B,N}-170`, `std-16{B,N}-175` |
| `dns` (Dense) | 表・密なUI | `{17,16,14}{B,N}-{130,120}` |
| `oln` (One line) | 1行ラベル | `{17,16,14}{B,N}-100` |
| `mono` | 等幅 | `{17,16,14}{B,N}-150` |

例: `<p class="dads-u-std-16N-175">本文</p>`, `<h1 class="dads-u-std-36B-140">`

目安: 本文は `std-16N-175`（長文）/`std-16N-170`、ページタイトルは `std-36B-140`〜`std-45B-140`、
セクション見出しは `std-28B-150`/`std-24B-150`、小見出しは `std-20B-150`/`std-18B-160`。
見出しにアクセントが欲しいときは `heading` コンポーネント（`dads-heading`）を使う。

## その他のユーティリティ・ベーススタイル

- `.dads-u-visually-hidden` — 視覚的に隠し、スクリーンリーダーには読ませる
- `.dads-u-focus-outline` / `.dads-u-focus-within-outline` — フォーカスリングを強制
- `a` 要素はグローバルにリンク色・下線・visited/hover/active が当たる（`link` コンポーネント不要な場合も多い）
- `:focus-visible` には黒アウトライン＋黄色リングが当たる。**独自CSSで outline を消さない**
- モーダル表示中のスクロール抑止（`html:has(:modal)`）も global.css に含まれる

## 単位・CSSの書き方（リポジトリの規約に合わせる）

- サイズは `calc(px / 16 * 1rem)` で書く（例: `padding: calc(24 / 16 * 1rem);`）。罫線のみ `px`
- 独自クラスを作るときは `dads-` 接頭辞を **使わない**（DADS 本体と衝突・ビルドスクリプトの警告対象になる）。例: `page-header`, `l-container`
- `@media (forced-colors: active)` と `@media (prefers-reduced-motion: reduce)` に配慮する
- レスポンシブのブレークポイントはコンポーネント側で主に `@media (min-width: 48rem)`（モバイルファースト）。ページレイアウトも合わせると揃う
- ホバー表現は `@media (hover: hover)` で囲む（タッチ端末で張り付かないように）
