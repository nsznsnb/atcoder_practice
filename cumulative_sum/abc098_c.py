N = int(input())
# S[i]: i番目の人が向いている方向:(E: 東 or W: 西)
S = input()

# 東を向いている人数の累積和
cs_e = [0] * (N+1)
# 西を向いている人数の累積和
cs_w = [0] * (N+1)

for i in range(N):
    if S[i] == "E":
        cs_e[i+1] = cs_e[i] + 1
        cs_w[i+1] = cs_w[i]
    else:
        cs_e[i+1] = cs_e[i]
        cs_w[i+1] = cs_w[i] + 1

# 向く方向を変える人数の最小値
ans = 2 ** 30
for i in range(N):
    ans = min(ans, cs_w[i] + (cs_e[N] - cs_e[i+1]))

print(ans)