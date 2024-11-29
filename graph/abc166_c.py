# 展望台の数、展望台どうしを結ぶ道の数
N, M = map(int, input().split())
# 展望台の標高
H = list(map(int, input().split()))

# 展望台iにつながる展望台の高さを格納
G = [[] for i in range(N)]

A = [None] * M
B = [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

    A[i] -= 1
    B[i] -= 1

    G[A[i]].append(H[B[i]])
    G[B[i]].append(H[A[i]])

# 良い展望台の数をカウント
ans = 0
for i in range(N):
    # 他のどの展望台にも通じていない
    if len(G[i]) == 0:
        ans += 1
    # 通じている他のどの展望台よりも高い
    elif H[i] > max(G[i]):
        ans += 1

print(ans)
