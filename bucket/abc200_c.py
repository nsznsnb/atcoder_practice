from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

div = 200
# A[i] - A[j]が200の倍数になるかどうかが問題なので、200で割っておく
for i in range(N):
    A[i] %= div

# バケット
bucket = defaultdict(int)
# 数値ごとの出現回数を記録
for i in range(N):
    bucket[A[i]] += 1

# A[i] - A[j] mod 200 = 0となる(i,j)の個数
ans = 0
for key in bucket.keys():
    ans += bucket[key] * (bucket[key]-1) // 2

print(ans)


