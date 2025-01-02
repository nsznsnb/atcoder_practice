# グリッドの縦横の幅
c_len = 3
# グリッド
C = [None] * c_len
# グリッドの各点に置かれた整数を記録
for i in range(c_len):
    C[i] = list(map(int, input().split()))

# グリッドに置かれた整数の最大値
e_max = 100

# マス(i,j)に置かれたC[i][j]に対して、ai+bj=c[i][j]となるようなa1,a2,a3,b1,b2,b3があるか
ans = False
for a1 in range(e_max+1):
    for a2 in range(e_max+1):
        for a3 in range(e_max+1):
            if C[0][0] - a1 != C[1][0] - a2 or C[1][0] -a2 != C[2][0] - a3:
                continue
            if C[0][1] - a1 != C[1][1] - a2 or C[1][1] -a2 != C[2][1] - a3:
                continue
            if C[0][2] - a1 != C[1][2] - a2 or C[1][2] -a2 != C[2][2] - a3:
                continue
            ans = True

print("Yes" if ans else "No")