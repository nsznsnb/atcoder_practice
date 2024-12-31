from collections import defaultdict

# 整数列の個数
N = int(input())
# 整数列
A = list(map(int, input().split()))

# バケット
bucket = defaultdict(int)

# 出現した整数の個数をカウント
for v in A:
    bucket[v] += 1

# どの2つの要素も異なるか
ans = True
for key in bucket.keys():
    if bucket[key] > 1:
        ans = False

print("YES" if ans else "NO")

