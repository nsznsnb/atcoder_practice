N, X = map(int, input().split())
L = list(map(int, input().split()))

D = [None] * (N+1)
D[0] = 0
for i in range(1,N+1):
    D[i] = D[i-1] + L [i-1]

ans = 0
for i in range(N+1):
    if D[i] > X:
        break
    ans += 1

print(ans)