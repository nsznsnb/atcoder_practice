import bisect
N, M = map(int, input().split())

vals = [[] for i in range(N+1)]
P = [None] * M
Y = [None] * M
for i in range(M):
    P[i], Y[i] = map(int,input().split())
    vals[P[i]].append(Y[i])

for i in range(N+1):
    vals[i] = sorted(list(set(vals[i])))

for i in range(M):
    ans = f"{P[i]:06}"

    id = bisect.bisect_left(vals[P[i]], Y[i])
    ans += f"{(id+1):06}"
    print(ans)
