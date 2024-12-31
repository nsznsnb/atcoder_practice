N = int(input())
S = input()

i = 0
# 連続する区間の長さリスト
group_nums = []
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    group_nums.append(j-i)
    i = j

# ２つを選ぶ全組合せから同一グループから２つ選ぶ組合せを排除する
ans = (N * (N+1)) // 2 - sum((v * (v+1)) // 2 for v in group_nums)
print(ans)