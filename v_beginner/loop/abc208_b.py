from math import factorial

P = int(input())

ans = 0
for n in range(10,0,-1):
    ans += P // factorial(n)
    P %= factorial(n)

print(ans)