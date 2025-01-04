H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = [input() for _ in range(H)]

Dx = [0, 1, 0, -1]
Dy = [-1, 0, 1, 0]

ans = 1
for dx, dy in zip(Dx, Dy):
    x = X
    y = Y
    while True:
        x += dx
        y += dy
        if not (0 <= x < H) or not (0 <= y < W):
            break

        if S[x][y] == "#":
            break

        ans += 1

print(ans)
