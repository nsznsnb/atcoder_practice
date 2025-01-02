# 支払う金額
N = int(input())
# A円硬貨, B円硬貨, C円硬貨
A, B, C = map(int, input().split())

# 使える硬貨枚数の限度
limit = 10 ** 4

# それぞれの硬貨を組み合わせて、N円支払うの時の硬貨枚数の最小値
ans = 2 ** 30
# 全探索
for a in range(limit):
    for b in range(limit):
        # C円硬貨の枚数が整数値出ない場合、スキップ
        if (N - A * a - B * b) % C != 0:
            continue
        c = (N - A * a - B * b) // C
        if 0 <= c < limit and (a+b+c) < limit:
            ans = min(ans, a + b + c)

print(ans)