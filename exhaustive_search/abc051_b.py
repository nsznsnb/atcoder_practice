K, S = map(int, input().split())

# X + Y + Z = Sを満たす(x,y,z)の個数
ans = 0
# 全探索
for x in range(K+1):
    for y in range(K+1):
        Z = S - x - y
        if Z < 0 or Z > K:
            continue
        ans += 1

print(ans)