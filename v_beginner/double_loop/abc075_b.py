# 0:下, 1: 右, 2: 上, 3:左, 4:右下, 5:右上, 6:左上, 7:左下
DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

H, W = map(int, input().split())
S = [input() for i in range(H)]

result = [[0 if v == "." else "#" for v in row] for row in S]

for i in range(H):
    for j in range(W):
        if S[i][j] != ".":
            continue

        for dx, dy in zip(DX, DY):
            ni, nj = i + dx, j + dy

            if not (0 <= ni < H) or not (0 <= nj < W):
                continue

            if S[ni][nj] == "#":
                result[i][j] += 1

for row in result:
    print(*row, sep="")
