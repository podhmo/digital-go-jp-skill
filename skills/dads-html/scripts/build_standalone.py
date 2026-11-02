#!/usr/bin/env python3
"""デジタル庁デザインシステム(DADS)のCSS/JSをインライン化し、スタンドアロンHTMLを生成する。

使い方:
    python3 build_standalone.py draft.html -o page.html [--component NAME ...]

- draft.html 中の `class="dads-..."` とカスタム要素 `<dads-...>` を走査し、
  必要なコンポーネントの CSS / JS を自動で特定する。
- global.css（デザイントークン・ベーススタイル）は常に含める。
- `<!-- dads:assets -->` マーカーがあればその位置に、無ければ `</head>` の直前に
  `<style>` / `<script type="module">` を挿入する。
- 下書き中の DADS 資材への `<link>` / `<script src>` は削除する（二重読み込み防止）。
- どの CSS にも存在しない `dads-` クラス名は警告として stderr に出す（タイポ検出）。

標準ライブラリのみで動作する。
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = (SKILL_DIR / "dads").resolve()
COMPONENTS_DIR = SRC_DIR / "components"

CLASS_TOKEN_RE = re.compile(r"\.(dads-[a-z0-9-]+(?:__[a-z0-9-]+)?)")
TAG_SELECTOR_RE = re.compile(r"(?<![\w.#-])(dads-[a-z0-9-]+)(?![\w-])")
DEFINE_RE = re.compile(r'customElements\.define\(\s*"([a-z0-9-]+)"')
EXCLUDE_SUFFIXES = (".stories.css", ".vrt.js", ".test.js", ".unit.js")
MARKER = "<!-- dads:assets -->"


def runtime_files(pattern: str) -> list[Path]:
    return sorted(
        p
        for p in COMPONENTS_DIR.glob(f"*/{pattern}")
        if not p.name.endswith(EXCLUDE_SUFFIXES)
    )


class Index:
    """CSS / JS の所有関係インデックス。"""

    def __init__(self) -> None:
        self.css_blocks: dict[Path, set[str]] = {}
        self.known_classes: set[str] = set()
        for css in runtime_files("*.css"):
            text = css.read_text(encoding="utf-8")
            classes = set(CLASS_TOKEN_RE.findall(text))
            self.known_classes |= classes
            blocks = {c.split("__")[0] for c in classes}
            # 要素セレクタとして書かれたカスタム要素（例: dads-progress-indicator）
            blocks |= set(TAG_SELECTOR_RE.findall(_strip_css_comments(text)))
            self.css_blocks[css] = blocks
        # CSS では未定義だがサンプルHTMLで正規に使われるフック用クラス（例: dads-list__item）
        for sample in COMPONENTS_DIR.glob("*/*.html"):
            c = Collector()
            c.feed(sample.read_text(encoding="utf-8"))
            self.known_classes |= c.classes
        self.asset_names = {"global.css"} | {
            p.name for p in runtime_files("*.css") + runtime_files("*.js")
        }
        self.tag_js: dict[str, Path] = {}
        for js in runtime_files("*.js"):
            for tag in DEFINE_RE.findall(js.read_text(encoding="utf-8")):
                self.tag_js[tag] = js
        self.component_names = {p.name for p in COMPONENTS_DIR.iterdir() if p.is_dir()}

    def css_for_block(self, block: str) -> list[Path]:
        candidates = [f for f, blocks in self.css_blocks.items() if block in blocks]
        own_dir = block.removeprefix("dads-")
        if own_dir in self.component_names:
            owned = [f for f in candidates if f.parent.name == own_dir]
            if owned:
                return owned
        return candidates

    def css_for_component(self, name: str) -> list[Path]:
        return [f for f in self.css_blocks if f.parent.name == name]

    def js_for_component(self, name: str) -> list[Path]:
        return [js for js in set(self.tag_js.values()) if js.parent.name == name]


def _strip_css_comments(text: str) -> str:
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


class Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.classes: set[str] = set()
        self.tags: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.startswith("dads-"):
            self.tags.add(tag)
        for key, value in attrs:
            if key == "class" and value:
                self.classes |= {c for c in value.split() if c.startswith("dads-")}


LOCAL_LINK_RE = re.compile(
    r"""[ \t]*<link\b(?=[^>]*rel=["']?stylesheet)[^>]*href=["']([^"']+)["'][^>]*>[ \t]*\n?""", re.I
)
LOCAL_SCRIPT_RE = re.compile(
    r"""[ \t]*<script\b[^>]*src=["']([^"']+)["'][^>]*>\s*</script>[ \t]*\n?""", re.I
)


def strip_local_assets(html: str, index: Index) -> tuple[str, list[str]]:
    """DADS 資材への相対参照を削除する。DADS 以外のローカル参照は残して警告対象として返す。"""
    leftovers: list[str] = []

    def repl(m: re.Match[str]) -> str:
        url = m.group(1)
        if re.match(r"^(?:[a-z]+:)?//|^data:", url, re.I):
            return m.group(0)  # 外部URL（Google Fonts 等）はそのまま
        if url.rsplit("/", 1)[-1].split("?")[0] in index.asset_names:
            return ""
        leftovers.append(url)
        return m.group(0)

    html = LOCAL_LINK_RE.sub(repl, html)
    html = LOCAL_SCRIPT_RE.sub(repl, html)
    return html, leftovers


INLINED_RE = re.compile(r"""<(style|script)\b[^>]*\bdata-dads=["'][^"']*["'][^>]*>.*?</\1>\s*\n?""", re.S | re.I)


def strip_inlined(html: str) -> str:
    """生成済みHTMLを入力にした場合に備え、前回インライン化した資材をマーカーへ戻す（冪等化）。"""
    first = True

    def repl(_: re.Match[str]) -> str:
        nonlocal first
        if first:
            first = False
            return MARKER + "\n"
        return ""

    return INLINED_RE.sub(repl, html)


def build(html: str, extra_components: list[str], index: Index) -> tuple[str, list[str], list[str]]:
    html = strip_inlined(html)
    collector = Collector()
    collector.feed(html)

    css_files: list[Path] = []
    js_files: list[Path] = []

    def add(lst: list[Path], items: list[Path]) -> None:
        for item in items:
            if item not in lst:
                lst.append(item)

    unknown: list[str] = []
    for cls in sorted(collector.classes):
        if cls.startswith("dads-u-"):
            continue  # global.css のユーティリティ
        if cls not in index.known_classes:
            unknown.append(f"unknown DADS class: {cls}")
        add(css_files, index.css_for_block(cls.split("__")[0]))

    for tag in sorted(collector.tags):
        add(css_files, index.css_for_block(tag))
        if tag in index.tag_js:
            add(js_files, [index.tag_js[tag]])
        else:
            unknown.append(f"unknown DADS element: <{tag}>")

    for name in extra_components:
        if name not in index.component_names:
            raise SystemExit(f"unknown component: {name}")
        add(css_files, index.css_for_component(name))
        add(js_files, index.js_for_component(name))

    parts = [
        '<style data-dads="global.css">',
        (SRC_DIR / "global.css").read_text(encoding="utf-8").rstrip(),
        "</style>",
    ]
    for css in sorted(css_files):
        rel = css.relative_to(COMPONENTS_DIR)
        parts += [f'<style data-dads="{rel}">', css.read_text(encoding="utf-8").rstrip(), "</style>"]
    for js in sorted(js_files):
        rel = js.relative_to(COMPONENTS_DIR)
        parts += [f'<script type="module" data-dads="{rel}">', js.read_text(encoding="utf-8").rstrip(), "</script>"]
    assets = "\n".join(parts)

    html, leftovers = strip_local_assets(html, index)
    unknown += [f"local asset is not inlined (standalone では読めません): {u}" for u in leftovers]
    if MARKER in html:
        html = html.replace(MARKER, assets, 1)
    elif re.search(r"</head>", html, re.I):
        html = re.sub(r"</head>", lambda _: assets + "\n</head>", html, count=1, flags=re.I)
    else:
        raise SystemExit(f"neither {MARKER!r} nor </head> found in input")

    used = [str(p.relative_to(COMPONENTS_DIR)) for p in sorted(css_files) + sorted(js_files)]
    return html, used, unknown


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, help="下書きHTML")
    parser.add_argument("-o", "--output", type=Path, help="出力先（省略時は stdout）")
    parser.add_argument(
        "-c", "--component", action="append", default=[],
        help="自動検出に加えて強制的に含めるコンポーネント名（ディレクトリ名）。複数指定可",
    )
    args = parser.parse_args()

    if not COMPONENTS_DIR.is_dir():
        raise SystemExit(
            f"components not found: {COMPONENTS_DIR}\n"
            "サブモジュールが未取得の可能性があります: git submodule update --init"
        )

    index = Index()
    html, used, unknown = build(args.input.read_text(encoding="utf-8"), args.component, index)

    if args.output:
        args.output.write_text(html, encoding="utf-8")
    else:
        sys.stdout.write(html)

    print("included: global.css" + "".join(f", {u}" for u in used), file=sys.stderr)
    for u in unknown:
        print(f"warning: {u}", file=sys.stderr)


if __name__ == "__main__":
    main()
