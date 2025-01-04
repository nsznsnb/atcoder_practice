S = input()
T = input()

INF = 2 ** 30
ans = INF
for i in range(len(S)-len(T)+1):
    mod_cnt = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            mod_cnt += 1
    ans = min(ans, mod_cnt)

print(ans)