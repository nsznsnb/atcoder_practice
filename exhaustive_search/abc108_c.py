N, K = map(int, input().split())

bucket = [0] * K
# bucket[x]: 区間[1,N]にKで割ってx余る数がいくつあるか
for i in range(1,N+1):
    bucket[i%K] += 1

# N以下の正の整数の組(a,b,c)について、a+b,b+c,c+aがすべてKの倍数であるようなものの個数
ans = 0
# a % Kについて全探索
for a in range(K):
    b = (K-a) % K
    c = (K-a) % K
    if ((b+c) % K != 0):
        continue
    ans += bucket[a] * bucket[b] * bucket[c]

print(ans)