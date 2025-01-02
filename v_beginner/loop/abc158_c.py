A, B = map(int, input().split())

INF = 2 ** 30
ans = INF
for price in range(1001):
    if (price * 8) // 100 == A and price // 10 == B:
        ans = min(ans, price)

if ans == INF:
    print(-1)
else:
    print(ans)