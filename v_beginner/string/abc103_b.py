S = input()
T = input()
N = len(S)

ans = False
for i in range(N):
    S = S[N-1] + S[0:N-1]
    if S == T:
        ans = True
        break

print("Yes" if ans else "No")
