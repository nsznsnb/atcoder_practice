import sys
sys.setrecursionlimit(10 ** 9)
# 頂点の数
N = int(input())

#　頂点に隣接する頂点のリスト
G = [[] * N for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())

    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 各頂点の色リスト
color_list = [""] * N

# DFSで隣接する頂点を異なる色に塗り分ける
def dfs(v: int, color: str):
    if color == "R":
        color_list[v] = "B"
    else:
        color_list[v] = "R"
    for v2 in G[v]:
        if color_list[v2] != "":
            continue
        dfs(v2, color_list[v])

dfs(0, "R")

black_list = []
red_list = []
for i in range(N):
    if color_list[i] == "R":
        red_list.append(i+1)
    else:
        black_list.append(i+1)

# 頂点の数が多い色リストを採用
ans = red_list if len(red_list) >= len(black_list) else black_list
print(*[ans[i] for i in range(N // 2)])