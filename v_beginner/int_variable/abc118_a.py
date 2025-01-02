A, B = map(int, input().split())

ans = 0
if B % A == 0:
    ans = A + B
else:
    ans = B - A

print(ans)