# コンポーネント一覧

> `scripts/gen_catalog.py` による自動生成。手で編集しないこと。

パスはスキルディレクトリからの相対パス。各コンポーネントの詳細は `dads/components/<name>/<name>.md` を、
マークアップは同ディレクトリのサンプルHTMLを読むこと。

| name | 名称 | CSS | カスタム要素(JS) | サンプルHTML |
| --- | --- | --- | --- | --- |
| `accordion` | [アコーディオン](https://design.digital.go.jp/dads/components/accordion/) | accordion.css | - | playground.html, stacked.html |
| `blockquote` | [引用ブロック](https://design.digital.go.jp/dads/components/blockquote/) | blockquote.css | - | multiple-paragraphs.html, playground.html, with-list.html |
| `breadcrumb` | [パンくずナビゲーション](https://design.digital.go.jp/dads/components/breadcrumb/) | breadcrumb.css | - | plain.html, with-home-icon.html, with-visible-label.html |
| `button` | [ボタン](https://design.digital.go.jp/dads/components/button/) | button.css | - | all-buttons-using-button.html, all-buttons-using-link.html, as-link.html, disabled-link.html, disabled.html, playground.html, with-icon.html |
| `calendar` | [日付ピッカー/カレンダー](https://design.digital.go.jp/dads/components/date-picker/) | calendar.css | `<dads-calendar>` | playground.html |
| `card` | [カード](https://design.digital.go.jp/dads/components/card/) | card-example-1.css, card-example-2.css, card-example-3.css, card-example-4.css, card-example-5.css, card-example-6.css | - | example-1.html, example-2.html, example-3.html, example-4.html, example-5.html, example-6.html |
| `carousel` | [カルーセル](https://design.digital.go.jp/dads/components/carousel/) | carousel-single.css, carousel.css | `<dads-carousel>`, `<dads-carousel-step-nav>` | container.html, key-visual-multi.html, key-visual-single.html |
| `checkbox` | [チェックボックス](https://design.digital.go.jp/dads/components/checkbox/) | checkbox.css | - | all-checkboxes.html, errored.html, indeterminate.html, playground.html, stacked.html, standalone.html |
| `chip-label` | [チップラベル](https://design.digital.go.jp/dads/components/chip-label/) | chip-label.css | - | all-chip-labels.html, custom-color.html, playground.html, with-icon.html, without-icon.html |
| `date-picker` | [日付ピッカー](https://design.digital.go.jp/dads/components/date-picker/) | date-picker.css | `<dads-date-picker>` | disabled.html, error.html, playground-consolidated-with-calendar.html, playground-consolidated.html, playground-separated-with-calendar.html, playground-separated.html, readonly.html, with-form-control-label.html |
| `description-list` | [説明リスト](https://design.digital.go.jp/dads/components/description-list/) | description-list.css | - | bullet.html, custom-icon-marker.html, custom-marker.html, without-marker.html |
| `disclosure` | [ディスクロージャー](https://design.digital.go.jp/dads/components/disclosure/) | disclosure.css | - | playground.html |
| `divider` | [ディバイダー](https://design.digital.go.jp/dads/components/divider/) | divider.css | - | all-dividers.html, decorative.html, playground.html |
| `drawer` | [ドロワー](https://design.digital.go.jp/dads/components/drawer/) | drawer.css | - | left.html, right.html |
| `emergency-banner` | [緊急時バナー](https://design.digital.go.jp/dads/components/emergency-banner/) | emergency-banner.css | - | playground.html |
| `file-upload` | [ファイルアップロード／ドロップエリア](https://design.digital.go.jp/dads/components/file-upload/) | file-upload.css | `<dads-file-upload>` | non-expandable.html, playground.html, single-file.html, with-error.html, with-existing-files.html, with-form-control-label.html, without-drop-area.html |
| `form-control-label` | フォームコントロールラベル | form-control-label.css | - | horizontal.html, multiple.html, single.html |
| `hamburger-menu-button` | [ハンバーガーメニューボタン](https://design.digital.go.jp/dads/components/hamburger-menu-button/) | hamburger-menu-button.css, hamburger-menu-icon-button.css | - | desktop-and-mobile.html, icon-button.html, mobile-conditional-en.html, mobile-conditional.html, text-button.html |
| `heading` | [見出し](https://design.digital.go.jp/dads/components/heading/) | heading.css | - | basic.html, playground.html, with-chip.html, with-icon.html, with-rule.html, with-shoulder.html |
| `horizontal-menu` | [水平メニュー](https://design.digital.go.jp/dads/components/horizontal-menu/) | horizontal-menu.css | - | links-only.html, playground.html, submenu-button.html |
| `image` | [画像](https://design.digital.go.jp/dads/components/image/) | image.css | - | borderless.html, caption-solid.html, full-width.html, playground.html, with-link.html, with-picture-element.html, without-caption.html |
| `input-text` | [インプットテキスト](https://design.digital.go.jp/dads/components/input-text/) | input-text.css | - | basic.html, disabled.html, errored.html, readonly.html, with-form-control-label.html |
| `language-selector` | [ランゲージセレクター](https://design.digital.go.jp/dads/components/language-selector/) | language-selector.css | `<dads-language-selector>` | playground.html |
| `link` | リンク | link.css | - | new-tab.html, playground.html |
| `list` | [箇条書きリスト](https://design.digital.go.jp/dads/components/list/) | list.css | - | bullet.html, custom-marker-format.html, nested.html, numbered-with-links.html, numbered.html |
| `menu-list` | [メニューリスト](https://design.digital.go.jp/dads/components/menu-list/) | menu-list.css | - | basic.html, has-children.html, playground.html |
| `menu-list-box` | [メニューリストボックス](https://design.digital.go.jp/dads/components/menu-list-box/) | menu-list-box.css | `<dads-menu-list-box>` | playground.html |
| `modal-dialog` | [モーダルダイアログ](https://design.digital.go.jp/dads/components/modal-dialog/) | modal-dialog.css | - | fixed-width.html, full-width.html, inner-scroll-with-fixed-actions.html, inner-scroll-with-fixed-both.html, inner-scroll-with-fixed-header.html, inner-scroll.html, playground.html |
| `notification-banner` | [ノティフィケーションバナー](https://design.digital.go.jp/dads/components/notification-banner/) | notification-banner.css | - | color-chip.html, error.html, info-1.html, info-2.html, mobile-compact.html, success.html, warning.html |
| `page-navigation` | [ページナビゲーション](https://design.digital.go.jp/dads/components/page-navigation/) | page-navigation.css | - | arrow-button.html, first-page.html, last-page.html, outlined-button.html, text-button.html |
| `progress-indicator` | [プログレスインジケーター](https://design.digital.go.jp/dads/components/progress-indicator/) | progress-indicator.css | `<dads-progress-indicator>` | interactive-demo.html, linear-fill.html, linear-loop.html, spinner-fill.html, spinner-loop.html, static.html |
| `radio` | [ラジオボタン](https://design.digital.go.jp/dads/components/radio/) | radio.css | - | all-radios.html, errored.html, playground.html, stacked.html, standalone.html |
| `resource-list` | [リソースリスト](https://design.digital.go.jp/dads/components/resource-list/) | resource-list.css | - | multiple-items.html, plain-with-inline-link.html, plain-with-whole-link.html, plain.html, selectable-with-inline-interaction.html, selectable-with-whole-interaction.html |
| `search-box` | [検索ボックス](https://design.digital.go.jp/dads/components/search-box/) | search-box.css | - | playground.html, with-detail.html, without-select.html |
| `select` | [セレクトボックス](https://design.digital.go.jp/dads/components/select/) | select.css | - | disabled.html, error.html, optgroup.html, playground.html, with-form-control-label.html |
| `step-navigation` | [ステップナビゲーション](https://design.digital.go.jp/dads/components/step-navigation/) | step-navigation.css | - | as-navigation.html, number-only.html, playground.html, set-step-width.html, step-completed.html, step-default.html, step-editing.html, step-error.html, step-reached.html, step-skipped.html |
| `switch` | [スイッチ](https://design.digital.go.jp/dads/components/switch/) | switch-mode.css, switch-on-off.css | `<dads-switch-mode>`, `<dads-switch-on-off>` | playground-mode.html, playground-on-off.html, with-form-control-label-mode.html, with-form-control-label-on-off.html |
| `tab` | [タブ](https://design.digital.go.jp/dads/components/tab/) | tab.css | `<dads-tab>`, `<dads-tab-aria>` | basic-aria.html, basic-static.html, basic.html, example.html, playground-aria.html, playground-static.html, playground.html |
| `table` | [テーブル／データテーブル](https://design.digital.go.jp/dads/components/table/) | table.css | `<dads-scroll-shadow>` | border-on-row-and-column.html, condensed-table.html, example.html, first-column-as-header-cell.html, first-row-and-column-as-header-cell.html, first-row-as-header-cell.html, highlight-hovered-row.html, indented-rows.html, linked-text-in-cell.html, overflow-on-mobile.html, plain.html, playground.html, selectable-table.html, sortable-header-dense.html, sortable-header.html, stripe-table.html, table-header-with-colspan.html, table-header-with-rowspan.html, with-caption.html |
| `textarea` | [テキストエリア](https://design.digital.go.jp/dads/components/textarea/) | textarea.css | `<dads-textarea-counter>` | basic.html, disabled.html, errored.html, readonly.html, with-counter.html, with-form-control-label.html |
| `toc` | [目次](https://design.digital.go.jp/dads/components/toc/) | toc.css | - | nested.html, playground.html |
| `utility-link` | [ユーティリティーリンク](https://design.digital.go.jp/dads/components/utility-link/) | utility-link.css | - | basic.html, multiple.html, playground.html, with-lead-icon.html |
