M, N = map(int, input().split())
K = int(input())
block = [input() for _ in range(M)]

# cs_J[i][j]: 区画(1,1)から区画(i,j)までの長方形領域に占めるジャングルの区画数
cs_J = [[0] * (N+1) for _ in range(M+1)]
# cs_O[i][j]: 区画(1,1)から区画(i,j)までの長方形領域に占める海の区画数
cs_O = [[0] * (N+1) for _ in range(M+1)]
# cs_I[i][j]: 区画(1,1)から区画(i,j)までの長方形領域に占める氷の区画数
cs_I = [[0] * (N+1) for _ in range(M+1)]

# 2次元累積和を求める
for i in range(M):
    for j in range(N):
        cs_J[i+1][j+1] = cs_J[i+1][j] + cs_J[i][j+1] - cs_J[i][j] + (1 if block[i][j] == "J" else 0)
        cs_O[i+1][j+1] = cs_O[i+1][j] + cs_O[i][j+1] - cs_O[i][j] + (1 if block[i][j] == "O" else 0)
        cs_I[i+1][j+1] = cs_I[i+1][j] + cs_I[i][j+1] - cs_I[i][j] + (1 if block[i][j] == "I" else 0)

for i in range(K):
    a, b, c, d = map(int, input().split())
    print(cs_J[c][d] - cs_J[c][b-1] - cs_J[a-1][d] + cs_J[a-1][b-1],
        cs_O[c][d] - cs_O[c][b-1] - cs_O[a-1][d] + cs_O[a-1][b-1],
          cs_I[c][d] - cs_I[c][b-1] - cs_I[a-1][d] + cs_I[a-1][b-1])
