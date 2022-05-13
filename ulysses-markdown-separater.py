#!/usr/bin/python
#%%
import os, glob, re

#%%
dir = './ulyz' # specify folder containing copied Ulysses markdown files here
outdir = './ulyz/output'

files = glob.glob(dir+'/*.md')

#%%
for file in files:
    f = open(file)
    strings = f.read()
    # 改行後に"# "があるときに分割。(?=...)で空マッチしないとsplit後に#が消える。
    strings = re.split("(?<=\n)(?=# )", strings)
    f.close()

    # ファイル名を取得し、同名フォルダを作成
    dir_name = os.path.splitext( os.path.basename(file) )[0]
    dir_path = outdir + "/" + dir_name
    if os.path.exists(dir_path):
        print('フォルダ ' + dir_name + ' は既に存在しています')
    else:
        os.mkdir(dir_path)

    # 同名フォルダ以下にテキストを書き出す
    for string in strings:
        # テスト用出力：全見出し1（#）の出力
        print(string.split("\n")[0])

        file_name = string.split("\n")[0][2:] + ".md"
        file_path = dir_path + "/" + file_name
        with open(file_path, 'wb') as outfile:
            outfile.write(string.encode())
