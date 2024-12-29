
# マスの個数
N = int(input())
# マスの高さ
H = list(map(int, input().split()))

i = 0
# 右隣に連続して移動できる最大移動数
ans = 0
while i < N - 1:
    j = i
    # 右隣の高さが低い場合
    while j < N - 1 and H[j] >= H[j+1]:
        j += 1
    ans = max(ans, j-i)
    i = j + 1

print(ans)