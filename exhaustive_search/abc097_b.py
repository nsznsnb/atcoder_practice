import sys
# 正整数
X = int(input())

# 1以下の最大のべき乗数は1
if X == 1:
    print(1)
    sys.exit(0)

# X(2<=X<=1000)以下の最大のべき乗数
ans = 0
# 全探索
for i in range(2, X+1):
    a = i * i
    while a <= X:
        ans = max(ans, a)
        a *= i

print(ans)