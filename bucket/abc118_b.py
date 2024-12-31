from collections import defaultdict
# 調査人数、食べ物の種類
N, M = map(int, input().split())

K = [None] * N
A = [None] * N
# バケット
bucket = defaultdict(int)

# 好きだと答えた食べ物を種類ごとにカウントアップ
for i in range(N):
    K[i], *A =  map(int, input().split())
    for j in range(K[i]):
        bucket[A[j]-1] += 1

# 全員が好きだと答えた食べ物の種類数
ans = 0
for key in bucket.keys():
    if bucket[key] == N:
        ans += 1

print(ans)