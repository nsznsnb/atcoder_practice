N, K = map(int, input().split())
p = list(map(int, input().split()))

# E[i]: 左からi番目までのさいころを振ったときの期待値
E = [0] * (N+1)
for i in range(N):
    E[i+1] = E[i] + (p[i]+1) / 2

# 隣接するK個のさいころを選んで独立に振ったときの、出る目の合計の期待値の最大値
ans = 0
for i in range(N - K + 1):
    ans = max(ans, E[i+K] - E[i])

print(ans)