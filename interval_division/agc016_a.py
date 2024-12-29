s = input()
N = len(s)

# 必要な操作の最小回数
ans = 2 ** 30
# 文字列の各文字ごとに必要な操作の回数を求め、その最小値が答えとなる
for ch in s:
    i = 0
    # 文字列を単一文字chにするために必要な操作回数
    ope_max = 0
    while i < N:
        if s[i] == ch:
            i += 1
            continue
        j = i
        while j < N and s[j] != ch:
            j += 1
        ope_max = max(ope_max, j-i)
        i = j
    ans = min(ans, ope_max)

print(ans)
