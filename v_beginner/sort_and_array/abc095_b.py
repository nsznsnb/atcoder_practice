N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]

ans = N
rest = X - sum(m)
ans += rest // min(m)

print(ans)