N = int(input())
H = list(map(int, input().split()))

ans = 0
ma = -1
for i in range(N):
    if ma <= H[i]:
        ans += 1
    ma = max(ma, H[i])

print(ans)