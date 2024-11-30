# 島の数、定期便の種類数
N, M = map(int, input().split())

A = [None] * M
B = [None] * M
# 島iから到達できる島を格納
G = [[]  for i in range(N)]

for i in range(M):
    # 島a,bを結ぶ定期船
    A[i], B[i] = map(int, input().split())

    A[i] -= 1
    B[i] -= 1

    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# 島1から島2まで定期便を２つ使い到達できるか
is_possible = False
for v in G[0]:
    for v2 in G[v]:
        if v2 == N-1:
            is_possible = True

print("POSSIBLE" if is_possible else "IMPOSSIBLE")

