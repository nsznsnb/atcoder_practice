def cnt_div(v, n):
    """
        値を指定した数で割れる回数を求める
        args
            v: 値
            n: 割る数
    """
    cnt = 0
    while v % n == 0:
        v //= n
        cnt += 1
    return cnt


N = int(input())

ans = 0
max_div_cnt = 0
for i in range(1, N+1):
    cnt = cnt_div(i, 2)
    if cnt >= max_div_cnt:
        ans = i
        max_div_cnt = cnt

print(ans)