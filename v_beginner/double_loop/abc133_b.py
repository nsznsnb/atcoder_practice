import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i):
        dist = math.sqrt(sum((X[i][k]-X[j][k])**2 for k in range(D)))
        if dist.is_integer():
            ans += 1

print(ans)