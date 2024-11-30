# 頂点数、辺数
N, M = map(int, input().split())

A = [None] * M
B = [None] * M
# 頂点iから到達できる頂点を格納
G = [[]  for i in range(N)]

for i in range(M):
    # 頂点a,bを結ぶ辺
    A[i], B[i] = map(int, input().split())

    A[i] -= 1
    B[i] -= 1

    #　頂点番号Fromより頂点番号Toが小さければ追加
    if A[i] > B[i]:
        G[A[i]].append(B[i])
    if B[i] > A[i]:
        G[B[i]].append(A[i])

ans = 0
for i in range(N):
    # 隣接頂点(iより小さい番号)がただ一つのみの場合
    if len(G[i]) == 1:
        ans += 1

print(ans)