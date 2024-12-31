from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

bucket = defaultdict(int)

# 数字ごとの出現回数を記録
for i in range(N):
    bucket[A[i]] += 1

# 整数組(i,j)の全選び方
ans = N * (N-1) // 2
# A[i] = A[j]となる組合せを差し引く
for key in bucket.keys():
    if bucket[key] > 1:
        ans -= bucket[key] * (bucket[key] - 1) // 2

# A[i] != A[j]となる整数組(i,j)の数
print(ans)