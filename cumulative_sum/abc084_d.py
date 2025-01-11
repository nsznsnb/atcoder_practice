
n_max = 10 ** 5 + 1
# 整数iが素数か
is_prime = [True] * n_max
is_prime[0] = False
is_prime[1] = False
# エラトステネスの篩
for q in range(2, n_max):
    if not is_prime[q]:
        continue
    # 素数の倍数から素数ラベルをはく奪
    for i in range(2 * q, n_max, q):
        is_prime[i] = False


# S[i]: 1からiまでの間で条件を満たす整数の数の和
S = [0] * (n_max+1)
# 累積和
for i in range(n_max):
    if is_prime[i] and is_prime[(i+1) // 2]:
        S[i+1] = S[i] + 1
    else:
        S[i+1] = S[i]

Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    print(S[r+1] - S[l])
