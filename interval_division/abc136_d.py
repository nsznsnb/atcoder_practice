S = input()
N = len(S)
ans = [0] * N

# 連続するRとLの境界を記録
boundaries = [0]

i = 0
while i < N:
    j = i
    # 文字が連続する間
    while j < N and S[i] == S[j]:
        j += 1
    # 境界をメモ
    boundaries.append(j)

    b_size = len(boundaries)
    if S[i] == "L":
        # 連続するRの個数
        left_size = boundaries[b_size-2] - boundaries[b_size-3]
        # 連続するLの個数
        right_size = boundaries[b_size-1] - boundaries[b_size-2]
        ans[i-1] = (left_size+1) // 2 + right_size // 2
        ans[i] = left_size // 2 + (right_size + 1) // 2

    i = j

print(*ans)

