# 頂点の数、辺の数
N, M = map(int, input().split())
a = [None] * M
b = [None] * M

# 頂点の探索済みフラグリスト
seen = [False] * N
# グラフ
G = [[False] * N  for _ in range(N)]

for i in range(M):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    G[a[i]][b[i]] = True
    G[b[i]][a[i]] = True

# DFSで頂点をたどって探索できるところまで探索する
def dfs(v : int) -> None:
    seen[v] = True
    for i in range(N):
        if G[v][i] and not seen[i]:
            dfs(i)

# 橋の本数
ans  = 0
for i in range(M):
    for j in range(N):
        seen[j] = False

    # 辺abを通過できないようにする
    G[a[i]][b[i]] = False
    G[b[i]][a[i]] = False

    dfs(0)

    # 辺abが橋であるか
    bridge = False

    for j in range(N):
        # 到達できない頂点がある場合
        if not seen[j]:
            bridge = True
    if bridge:
        ans += 1

    # 辺abを通過できるように戻す
    G[a[i]][b[i]] = True
    G[b[i]][a[i]] = True

print(ans)