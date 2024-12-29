# スライムの数
N = int(input())
# スライムの色
a = list(map(int, input().split()))

i = 0
# スライムの色を変える回数
ans = 0
while i < N:
    j = i
    while j < N and a[i] == a[j]:
        j += 1
    # 同じ色のスライムが2匹以上連続する場合
    if j - i >= 2:
        # 色を変える回数を足す
        ans += (j - i) // 2
    i = j

print(ans)
