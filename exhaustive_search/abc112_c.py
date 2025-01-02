# ピラミッドの調査地点の数
N = int(input())
x = [0] * N
y = [0] * N
h = [0] * N
# ピラミッドの座標(x[i], y[i])における高さh[i]
for i in range(N):
    x[i], y[i], h[i] = map(int, input().split())


# 可能性のある中心座標について全探索
for cx in range(101):
    for cy in range(101):
        H = 0
        for i in range(N):
            if h[i] != 0:
                H = abs(x[i]-cx) + abs(y[i]-cy) + h[i]
                break
        is_ok = True
        for i in range(N):
            if h[i] != max(H - abs(x[i] - cx) -abs(y[i] - cy), 0):
                is_ok = False

        if is_ok:
            print(cx, cy, H)
            break
    if is_ok:
        break
