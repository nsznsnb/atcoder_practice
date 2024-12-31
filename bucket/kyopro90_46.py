from collections import defaultdict
# 数列の長さ
N = int(input())
# 数列
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# バケット
bucket_a = defaultdict(int)
bucket_b = defaultdict(int)
bucket_c = defaultdict(int)
div = 46
# 数値(mod 46)の出現回数をリストA, B, Cそれぞれについてカウント
for i in range(N):
    A[i] %= div
    B[i] %= div
    C[i] %= div
    bucket_a[A[i]] += 1
    bucket_b[B[i]] += 1
    bucket_c[C[i]] += 1

# A[i] + B[j] + C[k] が46の倍数となる(i,j,k)の選び方の総数
ans = 0
for i in range(div+1):
    for j in range(div+1):
        for k in range(div+1):
            if (i + j + k) % div == 0:
                ans += bucket_a[i] * bucket_b[j] * bucket_c[k]

print(ans)



