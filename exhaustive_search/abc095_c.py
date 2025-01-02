# A:Aピザの単価
# B:Bピザの単価
# C:ABピザの単価
# X:Aピザの購入枚数
# Y:Bピザの購入枚数
A, B, C, X, Y = map(int, input().split())

INF = 2 ** 30

# 購入金額の最小値
ans = INF

# ABピザの購入枚数を全探索
for i in range(2*10**5+1):
    # ABピザの購入金額
    purchase = C * i
    # ABピザ購入後のAピザ購入枚数
    rest_A = max(0, X-(i // 2))
    rest_B = max(0, Y-(i // 2))

    # Aピザの購入枚数を加算
    purchase += A * rest_A
    purchase += B * rest_B

    ans = min(ans, purchase)

print(ans)