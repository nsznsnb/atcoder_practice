N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

candidates = [T - H[i] * 0.006 for i in range(N)]

INF = 2 ** 30
epsilon = INF
ans = 0
for i in range(N):
    if epsilon > abs(candidates[i] - A):
        epsilon = abs(candidates[i] - A)
        ans = i + 1
print(ans)