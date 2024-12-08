import sys
sys.setrecursionlimit(10**6)

# 都市数、道路の数
N, M = map(int, input().split())
A = [None] * M
B = [None] * M
# 都市ごとに道路で結ばれる都市を格納
G = [[] for i in range(N)]
for i in range(M):
     #都市Aと都市Bを結ぶ道路
    A[i], B[i] = map(int, input().split())

    A[i] -= 1
    B[i] -= 1

    G[A[i]].append(B[i])


def dfs(v: int) -> None:
    """
    都市vから0本以上の道路を使い移動できる都市を判定する

    Args:
        v int: 都市v
    """
    if seen[v]: 
        return
    
    seen[v] = True
    for v2 in G[v]:
        dfs(v2)

ans = 0
for i in range(N):
    seen = [False] * N
    dfs(i)
    ans += sum(seen)

print(ans)


