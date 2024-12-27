S = input()
N = len(S)

# 単語のリスト
words = []

# 文字列Sを単語ごとに分解する
i = 0
while i < N:
    # 初めてS[j]が大文字になるjを見つける
    j = i + 1
    while j < N and S[j].islower():
        j += 1
    # 単語を切り出してリストに追加する
    words.append(S[i:j+1])

    i = j + 1

# 単語を大文字小文字を無視した状態で辞書順にソートする
words.sort(key=str.lower)

# 単語を
print("".join(words))
