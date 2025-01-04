N, M = map(int, input().split())
s = [input() for _ in range(N)]

DX = [1, -1, 0, 0, 1, 1, -1, -1, 0]
DY = [0, 0, 1, -1, 1, -1, 1, -1, 0]

ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        for dx, dy in zip(DX, DY):
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < N) or not (0 <= nj < M):
                continue
            if s[ni][nj] == '#':
                ans[i][j] += 1

for i in range(N):
    print(*ans[i], sep="")