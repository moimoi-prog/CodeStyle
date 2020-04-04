from _collections import defaultdict

s = "df.kejhfrpvdfuhiobcdj,"

# 例: 文字列内で特定の文字がいくつ出てくるかを調べる
# 実装方法: 辞書で数える

# defaultdict ... 辞書のデフォルト値に引数で指定した方の初期値を格納する
d = defaultdict(int)
for a in s:
    d[a] += 1
print(d)
print(d["あ"])
print(d["f"])