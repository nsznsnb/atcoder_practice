# ユーザ数、ログ行数
N, Q = map(int, input().split())
# ユーザのフォロー状態
f = [['N'] * N for i in range(N)]

for i in range(Q):
    x, a, *b = map(int, input().split())
    a -= 1
    # フォロー
    if x == 1:
        b = b[0] - 1
        f[a][b] = 'Y'
    # フォロー全返し
    elif x == 2:
        for j in range(N):
            if f[j][a] == 'Y':
                f[a][j] = 'Y'
    # フォローフォロー
    elif x == 3:
        for j in [j for j in range(N) if f[a][j] == 'Y']:
            for k in range(N):
                if k != a and f[j][k] == 'Y':
                    f[a][k] = 'Y'

# ログから復元したフォロー状態を出力
for i in range(N):
    print(''.join(f[i]))