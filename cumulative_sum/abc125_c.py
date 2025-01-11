def gcd(a :int, b: int):
    """
    最大公約数を求める
    """
    return a if b == 0 else gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

# 左側からの累積GCD
left_cgcd = [0] * (N+1)
# 右側からの累積GCD
right_cgcd = [0] * (N+1)

for i in range(N):
    left_cgcd[i+1] = gcd(left_cgcd[i], A[i])
for i in range(N-1, -1, -1):
    right_cgcd[i] = gcd(right_cgcd[i+1], A[i])

# 配列Aのどれか一つの要素を書き換えた場合の、最大公約数の最大値
ans = 0
for i in range(N):
    ans = max(ans, gcd(left_cgcd[i], right_cgcd[i+1]))

print(ans)