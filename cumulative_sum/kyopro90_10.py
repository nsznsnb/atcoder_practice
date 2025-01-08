N = int(input())
# C[i]: 学籍番号iの所属するクラス
C = [None] * N
# P[i]: 学籍番号iの点数
P = [None] * N
# クラス1の点数の累積和
cs_1 = [0] * (N+1)
# クラス2の点数の累積和
cs_2 = [0] * (N+1)
for i in range(N):
    C[i], P[i] = map(int, input().split())
    if C[i] == 1:
        cs_1[i+1] = cs_1[i] + P[i]
        cs_2[i+1] = cs_2[i]
    else:
        cs_2[i+1] = cs_2[i] + P[i]
        cs_1[i+1] = cs_1[i]

# クエリの数
Q = int(input())
for i in range(Q):
    # 学籍番号の範囲取得
    L, R = map(int, input().split())

    # 累積和を使って、各クラスの合計を表示
    print(cs_1[R] - cs_1[L-1], cs_2[R] - cs_2[L-1])





