# ボールの数, 操作後の種類数
N, K = map(int, input().split())
A = list(map(int, input().split()))

# バケット
bucket = [0] * N

for v in A:
    bucket[v-1] += 1

# 個数の多いボールの種類順にソート
bucket.sort(reverse=True)

# 種類数がK種類以下になるように書き換えるボールの数を合計
print(sum(bucket[i] for i in range(K, N)))