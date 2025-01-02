N, M = map(int, input().split())

S = [0] * M
C = [0] * M
for i in range(M):
    # S[i]桁目,数字C[i]
    S[i], C[i] = map(int, input().split())

# 入力条件S, Cを満たすN桁の最小整数
ans = -1
# 全探索
for num in range(0, 10**N):
    # N桁でない場合スキップ
    if len(str(num)) != N:
        continue
    str_num = str(num)
    is_ok = True
    # 入力条件チェック: 桁ごとに条件が合致しているか
    for i in range(M):
        if str_num[S[i]-1] != str(C[i]):
            is_ok = False
            break
    if is_ok:
        ans = str_num
        break

print(ans)