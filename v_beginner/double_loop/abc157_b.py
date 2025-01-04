def check_bingo(check_list: list[list]):
    size = len(check_list)
    for i in range(size):
        if all(check_list[i]):
            return True

    for j in range(size):
        if all(check_list[i][j] for i in range(size)):
            return True

    if all(check_list[i][i] for i in range(size)):
        return True

    if all(check_list[i][size-i-1] for i in range(size)):
        return True

    return False


A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

seen = [[False] * 3 for _ in range(3)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if A[j][k] == b[i]:
                seen[j][k] = True

print("Yes" if check_bingo(seen) else "No")