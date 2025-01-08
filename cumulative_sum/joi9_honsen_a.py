# 宿場町の数、旅日数
n, m = 0, 0

with open("./input.txt") as f:
    n,m = map(int, f.readline().split())
    # d[i]: 宿場iと宿場i+1間の距離
    dist = [None] * (n-1)
    # a[i]: i+1日目の移動方法
    a = [None] * m
    for i in range(n-1):
        dist[i] = int(f.readline())
    for i in range(m):
        a[i] = int(f.readline())

# S[i]: 宿場町0から宿場町iまでの総距離
S = [0] * n
for i in range(n-1):
    S[i+1] = S[i] + dist[i]

# m日間の総移動距離
ido_dist_sum = 0
cur_pos = 0
for i in range(m):
    if a[i] >= 0:
        ido_dist_sum += S[cur_pos+a[i]] - S[cur_pos]
    else:
        ido_dist_sum += (S[cur_pos] - S[cur_pos+a[i]])
    cur_pos += a[i]

with open("./output.txt", "w") as f:
    f.write(str(ido_dist_sum % (10**5)))