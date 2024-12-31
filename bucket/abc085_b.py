# バケットのサイズ
M = 101

N = int(input())

# バケット
exist = [0] * M

# バケットを作成
for i in range(N):
    d = int(input())
    # バケットを更新
    exist[d] = 1

print(sum(exist))