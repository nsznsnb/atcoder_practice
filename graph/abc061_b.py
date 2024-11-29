# 都市数、都市同士を結ぶ道の本数
N, M = map(int, input().split())

# 都市iと結ばれている都市
G = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    G[a].append(b)
    G[b].append(a)

# 都市iにつながる都市の数を出力
for i in range(N):
    print(len(G[i]))