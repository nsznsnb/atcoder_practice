# 入力
s = input()
# 入力サイズ
N = len(s)

# 圧縮後の文字列リスト
compress_list = []
i = 0
while i < N:
    j = i
    # 同一文字が連続する間、添え字をカウントアップ
    while j < N and s[i] == s[j]:
        j += 1
    # 文字と連続した個数を連結して格納
    compress_list.append(s[i] + str(j-i))
    i = j

print("".join(compress_list))
