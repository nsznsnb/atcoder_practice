N = int(input())
S = [None] * N
T = [None] * N

for i in range(N):
    S[i], T[i] = input().split()
    T[i] = int(T[i])

v = list(enumerate(T))
v.sort(key=lambda x: x[1], reverse=True)

print(S[v[1][0]])