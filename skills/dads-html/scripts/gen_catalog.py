#!/usr/bin/env python3
"""サブモジュールからコンポーネント一覧 (references/components.md) を生成する。

サブモジュール更新後に再実行する:
    python3 scripts/gen_catalog.py
"""

from __future__ import annotations

import re
from pathlib import Path

from build_standalone import COMPONENTS_DIR, DEFINE_RE, SKILL_DIR, runtime_files

GUIDE_URL_RE = re.compile(r"\((https://design\.digital\.go\.jp/[^)]+)\)")
STORY_TITLE_RE = re.compile(r'title:\s*"Components/([^"]+)"')


def main() -> None:
    rows = []
    for d in sorted(p for p in COMPONENTS_DIR.iterdir() if p.is_dir()):
        md = d / f"{d.name}.md"
        title, url = d.name, ""
        stories = d / f"{d.name}.stories.ts"
        if stories.exists() and (m := STORY_TITLE_RE.search(stories.read_text(encoding="utf-8"))):
            title = m.group(1)
        if md.exists() and (m := GUIDE_URL_RE.search(md.read_text(encoding="utf-8"))):
            url = m.group(1)
        css = [p.name for p in runtime_files("*.css") if p.parent == d]
        tags = sorted(
            t for js in runtime_files("*.js") if js.parent == d for t in DEFINE_RE.findall(js.read_text(encoding="utf-8"))
        )
        samples = sorted(p.name for p in d.glob("*.html"))
        rows.append((d.name, title, url, css, tags, samples))

    out = [
        "# コンポーネント一覧",
        "",
        "> `scripts/gen_catalog.py` による自動生成。手で編集しないこと。",
        "",
        "パスはスキルディレクトリからの相対パス。各コンポーネントの詳細は `dads/components/<name>/<name>.md` を、",
        "マークアップは同ディレクトリのサンプルHTMLを読むこと。",
        "",
        "| name | 名称 | CSS | カスタム要素(JS) | サンプルHTML |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name, title, url, css, tags, samples in rows:
        title_cell = f"[{title}]({url})" if url else title
        out.append(
            f"| `{name}` | {title_cell} | {', '.join(css)} | {', '.join(f'`<{t}>`' for t in tags) or '-'} | {', '.join(samples)} |"
        )
    out.append("")
    path = SKILL_DIR / "references" / "components.md"
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {path} ({len(rows)} components)")


if __name__ == "__main__":
    main()
