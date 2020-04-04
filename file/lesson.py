import string
import csv
import os
import pathlib
import glob
import shutil
import tarfile
import zipfile
import tempfile
import datetime

# ファイル操作
# モード一覧
# w ... 書き込み(開いた瞬間中身が消える。)
# a ... 追記される
# r ... 読み込み

# print関数は、ファイルへの書き込みにも使用できる。(writeの方が多く使用する。)
# f ... 書き込むファイルを指定(open されている必要あり)
# sep ... 何で区切って書き込みするかを指定
# end ... 最後の文字を指定 → ""を指定すると改行しなくなる。

f = open("text.txt", "w")
f.write("test")
print("Good job", file=f)
f.close()

# withを使用して開く
# closeを勝手にしてくれる。

# """\ 文字列 """ ...　文字列をそのままの形で格納してくれる。
s = """\
AAA
BBB
CCC
DDD
"""

with open("text.txt", "w") as f:
    f.write(s)

# 一気にファイルを読み込み
print("一気にファイルを読み込み")
with open("text.txt", "r") as f:
    print(f.read())

# １行ずつ読み込み
# readline
print("１行ずつファイルを読み込み")
with open("text.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break

        print(line, end="")

# 一定の区切りで読み込み(ネットワークのプログラミングで、パケットを読みたいときに使用する。)
# readの引数に区切りたい文字数を指定
print("2文字で区切ってファイルを読み込み")
with open("text.txt", "r") as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        if not line:
            break

        print(line)

# 位置(seek)
# f.tell ... 今いる位置を取得(文字単位)
# f.seek ... 移動(文字単位, 最初から数えた位置に移動する。)


print("sheekを使用する")
with open("text.txt", "r") as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.tell())
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(1)
    print(f.read(1))

# 書き込み読み込みモード
# w+
# 書き込んだものを最初から読みこむ場合はseekで移動する必要あり。

# 読み込み書き込みモード
# r+
# 読みこむファイルがない場合、エラーが発生する。

print("書き込み読み込みモード")
with open("text.txt", "w+") as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# テンプレート
# import Stringをする
# 文字列内で代入したい位置の前に$をつける
# stringのTemplateメソッド(コンストラクタ)を呼び出し、引数に作成したテンプレートを指定する。
# 代入する場合は、Templateオブジェクトのsubstituteメソッドを呼び出す。
# テキストファイル等にテンプレートを保存しておいて、
# 読み込んで使いと良い。

print("テンプレート生成")

s = """\

Hi $name.

$contents

Good bye.

"""

t = string.Template(s)
contents = t.substitute(name="Mike", contents="I kill you.")
print(contents)

# csvファイルを開く
# import csvでライブラリをインポート
# 書き込み
# with openでCSVファイルを書き込みモードで開く
# csv.DickWriterでファイルを生成
# csv.writeheaderでヘッダーを書き込み
# csv.writerowで内容を書き込み
#
# 読み込み
# with openでcsvファイルを読み込みモードで開く
# DickReaderで読み込み用オブジェクトを生成
# for in(拡張for文)で１行ずつ読み込み、格納
#

with open("text.csv", "w") as csv_file:
    field_names = ["name", "count"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({"name": "mike", "count": 1})
    writer.writerow({"name": "jan", "count": 2})

with open("text.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row["name"], row["count"])

# ファイル操作
# import osを行う
# ファイルの存在を確認
# os.path.exists
print(os.path.exists("lesson.py"))

# 種類を確認したい場合
# os.path.isfile ... ファイルであるかを判定
# os.file.isdir ... フォルダであるかを判定
print(os.path.isfile("lesson.py"))
print(os.path.isdir("lesson.py"))

# 名前を変更する
# os.rename
os.rename("text.txt", "text2.txt")

# シムリンク ... (ショートカットみたいなもの)
# os.symlink

# フォルダ作成
# os.mkdir
os.mkdir("lesson_folder")

# フォルダ削除(中身がない場合のみ削除可能)
# os.rmdir
os.rmdir("lesson_folder")

# フォルダ削除(中身がある場合でも可能 → 注意すること)
# shutil.rmtree

# ファイル生成
# import pathlib ... ファイルを作成するときに使用
# pathlib.Path(ファイル名).touch()
pathlib.Path("lesson.txt").touch()

# ファイル削除
# os.remove
os.remove("lesson.txt")

# フォルダ内のフォルダを一覧表示
# os.listdir
print(os.listdir("../"))

# フォルダ内のファイルを一覧表示(全て)
# import glob
# glob.glob(フォルダ名/*)
print(glob.glob("../*"))

# ファイルのコピー
# shutil.copy(コピー対象ファイル名, コピー後ファイル名)
shutil.copy("text2.txt", "text3.txt")

# 現在のディレクトリを取得
# os.getcwd  カレントワーキングディレクトリ
print(os.getcwd())

# ファイルの圧縮、解凍
# tarファイル編
# import tarfile(mac. Linuxで使用)

# tarファイルを作成
# with tarfile.openでtarファイルを開く
# ファイル名: 任意.tar.gz
# モード: w:gz
# オブジェクトにファイルを追加
# オブジェクト.add
with tarfile.open("test.tar.gz", "w:gz") as tar:
    tar.add("tar_test")

# tarファイルを開く
# with tarfile.openでtarファイルを開く
# モード: r:gz
# 解凍
# オブジェクト.extractall(path=保存後ファイル名)

# 特定のファイルのみを見る
# with tarファイルオブジェクト.extractfile(対象のパス)

with tarfile.open("test.tar.gz", "r:gz") as tar:
    with tar.extractfile("tar_test/test.txt") as f:
        print(f.read())
    tar.extractall(path="tar_test2")

# zipファイル編
# import zipfile
# with zipfile.ZipFile()でフォルダに書き込み
# ファイル名: 任意.zip
# モード: w
# オブジェクトにファイルを追加
# オブジェクト.write(ファイル名) ... フォルダの中身も全て列記しなければならない
with zipfile.ZipFile("tar_test.zip", "w") as z:
    z.write("tar_test")
    z.write("tar_test/test.txt")

# 全て格納したい場合
with zipfile.ZipFile("tar_test2.zip", "w") as z:
    for f in glob.glob("tar_test/**", recursive=True):
        z.write(f)

# zipファイルを開く
# with zipfile.ZipFile()でフォルダを読み込み
# ファイル名: 開きたいファイル名
# モード: r
# オブジェクト.extractall(保存後ファイル名)

with zipfile.ZipFile("tar_test.zip", "r") as z:
    z.extractall("tar_test3")

# tempfile
# IOバッファにpythonがファイルを作ってくれる　→　実際のファイルを作成しなくても良い。

with tempfile.TemporaryFile(mode="w+") as t:
    t.write("hello")
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, "w+") as f:
        f.write("bye")
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as t:
    print(t)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

# 時間を操る
# import datetime
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime("%d/%m/%y"))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime("%y/%m"))

time = datetime.time(hour=1, minute=1, second=1, microsecond=1)
print(time)

print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)
