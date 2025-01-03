import math

N, D = map(int, input().split())
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0
for i in range(N):
    if math.sqrt(X[i]**2 + Y[i]**2) <= D:
        ans += 1

print(ans)