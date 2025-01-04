H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

C2 = [[''] * W for _ in range(2*H)]

for i in range(H):
    for j in range(W):
        C2[2*i][j] = C[i][j]
        C2[2*i+1][j] = C[i][j]

for i in range(2*H):
    print("".join(C2[i]))