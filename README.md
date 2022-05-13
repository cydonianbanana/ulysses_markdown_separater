# README

Separating Sheets from Ulysses (http://ulyssesapp.com) to regular markdown files

1. UlyssesのGUIにて、ライブラリの特定グループ内の全シートを選択してテキスト書き出し（Markdown）を実行する。
2. 書き出された.mdファイルの名称をグループ名にして、ソースコード内で指定したdirパス（デフォルトでは"./ulyz"）に置く
3. 1.〜2.を、必要なグループ分繰り返す。これにより、必要な全グループの.mdファイルを用意する。
4. 本スクリプトを実行する。これにより、ソースコード内で指定したoutdirパス（デフォルトでは"./ulyz/output"）に、グループごとにフォルダ分けして、見出し1（#）をファイル名として分割された.mdファイルが出力される。
