S = input()

ans = 0
for i in range(len(S) // 2):
    if S[i] != S[len(S) - i - 1]:
        ans += 1

print(ans)