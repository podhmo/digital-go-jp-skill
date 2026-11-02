# digital-go-jp-skill

[デジタル庁デザインシステム コードスニペット（HTML版）](https://github.com/digital-go-jp/design-system-example-components-html)を使って、
CSS/JSをすべてインライン化したスタンドアロンHTMLを作成する Claude Code スキル `dads-html`。

## 構成

```
vendor/design-system-example-components-html/   # git submodule（公式リポジトリ）
skills/dads-html/
├── SKILL.md
├── dads -> ../../vendor/design-system-example-components-html/src
├── references/
│   ├── components.md     # コンポーネント一覧（gen_catalog.py で自動生成）
│   └── foundations.md    # トークン・タイポグラフィ・CSS規約の要約
├── assets/template.html  # 下書きの雛形
└── scripts/
    ├── build_standalone.py  # 下書き → スタンドアロンHTML
    └── gen_catalog.py       # references/components.md の再生成
.claude/skills/dads-html -> ../../skills/dads-html   # このリポジトリ内で使う用
```

## セットアップ

```bash
git clone --recursive https://github.com/podhmo/digital-go-jp-skill
# 既にクローン済みなら
git submodule update --init
```

このリポジトリ内で Claude Code を起動すればスキルが使える。
他のプロジェクトでも使いたい場合はユーザースキルとしてリンクする（相対シンボリックリンクはリポジトリ内で解決されるので動く）:

```bash
ln -s "$PWD/skills/dads-html" ~/.claude/skills/dads-html
```

## 使い方

Claude Code に「デジタル庁デザインシステムで住所変更届のフォームページを作って」などと頼む。

スクリプト単体でも使える:

```bash
python3 skills/dads-html/scripts/build_standalone.py page.draft.html -o page.html
```

## サブモジュールの更新

```bash
git submodule update --remote vendor/design-system-example-components-html
python3 skills/dads-html/scripts/gen_catalog.py
```

## ライセンス

デザインシステムのコードスニペットは MIT License（digital-go-jp/design-system-example-components-html）。
