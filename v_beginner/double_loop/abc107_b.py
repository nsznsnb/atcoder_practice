H, W = map(int, input().split())
a = [input() for _ in range(H)]

A = []

for i in range(H):
    if all(a[i][j] == "." for j in range(W)):
        pass
    else:
        A.append(a[i])

A2 = [[] for _ in range(len(A))]
for i in range(W):
    if all(a[j][i] == "." for j in range(H)):
        pass
    else:
        for j in range(len(A)):
            A2[j].append(A[j][i])

for i in range(len(A2)):
    print(*A2[i], sep="")