N, Q = map(int, input().split())
S = input()

# 累積和csを求める
cs = [0] * (N+1)
for i in range(1, N):
    cs[i+1] = cs[i] + (S[i-1:i+1] == "AC")

# 各クエリに答える
for q in range(Q):
    # 区間を取得
    l, r = map(int, input().split())

    l -= 1
    r -= 1

    # 累積和を用いて答えを求める
    print(cs[r+1] - cs[l+1])