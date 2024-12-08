# 頂点数, 辺数
N, M = map(int, input().split())

A = [None] * M
B = [None] * M
# 頂点ごとに辺で結ばれる頂点を格納
G = [[] for i in range(N)]
for i in range(M):
    #頂点Aと頂点Bを結ぶ辺
    A[i], B[i] = map(int, input().split())

    A[i] -= 1
    B[i] -= 1

    G[A[i]].append(B[i])

# 頂点iが探索済みかどうか
seen = [False] * N

def dfs(v: int) -> None:
    """
    頂点vを始点として、辺をたどってパス数をカウントする

    Args:
        v int: 頂点v
    """
    global ans 
    ans += 1
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]:
            continue
        dfs(v2)
    seen[v] = False



ans = 0
for i in range(N):
    dfs(i)

print(ans)


