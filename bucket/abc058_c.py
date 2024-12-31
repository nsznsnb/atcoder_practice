n = int(input())

# bucket['a'][i]: i番目の文字列に'a'が何回出現するか
bucket = {}
for cd in range(ord('a'), ord('z')+1):
    bucket[chr(cd)] = [0] * n

for i in range(n):
    s = input()
    for ch in s:
        bucket[ch][i] += 1

# 各文字列から共通する文字を取り出して作れる辞書順で最小の文字列
ans = ""
for cd in range(ord('a'), ord('z')+1):
    ans += chr(cd) * min(bucket[chr(cd)])

print(ans)



