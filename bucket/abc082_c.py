from collections import defaultdict
# 数列のサイズ
N = int(input())
# 数列
a = list(map(int, input().split()))

# バケット
bucket = defaultdict(int)
# 数字の出現回数を記録
for i in range(N):
    bucket[a[i]] += 1

# 良い数列にするために削除する回数
ans = 0
for key in bucket.keys():
    # 出現回数が数字と一致するように削除する回数をカウント
    if bucket[key] - key >= 0:
        ans += bucket[key] - key
    else:
        ans += bucket[key]

print(ans)