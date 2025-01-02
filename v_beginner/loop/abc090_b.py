A, B = map(int, input().split())

ans = 0
for n in range(A, B+1):
    # 1桁目
    a = n // 10000 % 10
    # 2桁目
    b = n // 1000 % 10
    # 4桁目
    c = n // 10 % 10
    # 5桁目
    d = n % 10
    if a == d and b == c:
        ans += 1

print(ans)
