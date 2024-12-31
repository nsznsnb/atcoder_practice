# 入力のサイズ
N = int(input())
# 文字列
S = input()

#　文字列を2つに分割した際に、両方に含まれる文字種の最大数
ans = 0
# 文字列の分割位置を全探索
for i in range(1, N):
    left_str = S[0:i]
    right_str = S[i:]
    # 両方の文字列に含まれる文字種をカウント
    cnt = 0
    # 文字種を全探索
    for cd in range(ord('a'), ord('z')+1):
        ch = chr(cd)
        if ch in left_str and ch in right_str:
            cnt +=1
    ans = max(ans, cnt)


print(ans)
