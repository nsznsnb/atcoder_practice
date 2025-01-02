
def create_binary_num_list(n: int):
    """
       nビットの2進数リストを取得する
       args
        n: ビット数
       return
        nビットの2進数リスト
    """
    bit_list = []
    for i in range(2**n):
        s = ""
        for j in range(n):
            s += str((i >> j) & 1)
        bit_list.append(s)
    return bit_list

# 連結された4つの整数
S = input()
# 足し引きの合計操作回数
ope_num = 3

# 4つの整数の間に+,-の操作を加えた合計が7になるときの計算式
ans = ""
for bits in create_binary_num_list(ope_num):
    sum_num = int(S[0])
    ans = S[0]
    for i in range(ope_num):
        if bits[i] == "1":
            ans += "+" + S[i+1]
            sum_num += int(S[i+1])
        else:
            ans += "-" + S[i+1]
            sum_num -= int(S[i+1])
    if sum_num == 7:
        ans += "=7"
        break
print(ans)