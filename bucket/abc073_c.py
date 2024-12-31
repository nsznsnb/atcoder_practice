from collections import defaultdict
# 数字の発表回数
N = int(input())
bucket = defaultdict(int)

for i in range(N):
    # 発表された数字
    a = int(input())
    # 紙に書かれていなければカウントアップ
    if bucket[a] == 0:
        bucket[a] = 1
    else:
        bucket[a] = 0

# N回の発表後に紙に書かれている数字の数
ans = 0
for key in bucket.keys():
    if bucket[key] == 1:
        ans += 1

print(ans)