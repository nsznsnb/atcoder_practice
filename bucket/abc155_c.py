from collections import defaultdict
N = int(input())

# バケット
bucket = defaultdict(int)

# 文字列の出現頻度をカウント
for i in range(N):
    bucket[input()] += 1

# 最頻値
mode_value = max(bucket.values())

# 最頻出の文字列リスト
mode_key_list = []
for key in bucket.keys():
    if bucket[key] == mode_value:
        mode_key_list.append(key)

# 辞書順にソート
mode_key_list.sort()
for key in mode_key_list:
    print(key)
