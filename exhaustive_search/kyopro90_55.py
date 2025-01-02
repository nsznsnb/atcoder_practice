from itertools import combinations

# 整数の数、割る数、余り
N, P, Q = map(int, input().split())
# 整数列
A = list(map(int, input().split()))

# 整数列から5個を選び、その積をPで割ってQ余るものの組合せ数
ans = 0
combs = combinations(A, 5)
for a, b, c, d, e in combs:
    temp = a % P
    temp = (temp * b) % P
    temp = (temp * c) % P
    temp = (temp * d) % P
    temp = (temp * e) % P
    if temp == Q:
        ans += 1
print(ans)