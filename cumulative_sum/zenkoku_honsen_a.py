N = int(input())
# A[i]:区画iの資源埋蔵量
A = list(map(int, input().split()))

# 資源埋蔵量の累積和
cs = [0] * (N+1)
for i in range(N):
    cs[i+1] = cs[i] + A[i]


for k in range(1, N+1):
    # 連続するk個の区画を選んだ時の、資源埋蔵量の最大値
    ans = - 2 ** 30
    for i in range(N - k + 1):
        ans = max(ans, cs[i+k] - cs[i])
    print(ans)

