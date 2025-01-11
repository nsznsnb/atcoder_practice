from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

# S[i]: A[j](0<=j<=i-1)までの和
S = [0] * (N+1)
for i in range(N):
    S[i+1] = S[i] + A[i]

# 累積和の分布
bucket = defaultdict(int)

for s in S:
    bucket[s] += 1

# Aの部分列で総和が0になるものの取り出し方の総数
ans = 0
for key in bucket.keys():
    ans += bucket[key] * (bucket[key]-1) // 2

print(ans)
