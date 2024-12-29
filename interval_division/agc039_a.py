import sys
S = input()
N = len(S)
# 文字列Sの繰り返し数
K = int(input())

i = 0

# 連続する文字数リスト
s_list = []
# 連続する文字列をカウントして、順次、連続数を格納する
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    s_list.append(j-i)
    i = j

s_list_size = len(s_list)

# すべて同じ文字の場合
if len(s_list) == 1:
    print((N * K ) // 2)
    sys.exit(0)

# 隣りあう文字が異なるように文字の変更を行う回数の最小値
ans = 0
for i in range(s_list_size):
    # 文字列Sの端以外
    if i != 0 and i != s_list_size-1:
        ans += (s_list[i] // 2) * K

# 文字列Sを連結した際に、連結される端点どうしが同じ文字の場合
if S[0] == S[N-1]:
    # 端と内部の操作回数を合算
    ans += (s_list[0]//2 + s_list[s_list_size-1]//2)  \
                + ((s_list[0] + s_list[s_list_size-1]) // 2) * (K-1)
else:
    ans += (s_list[0] // 2) * K  + (s_list[s_list_size-1] // 2) * K

print(ans)