N = int(input())

# S[i]: i日目の登録者名
S = [''] * N
# 登録済みのユーザ名
toroku_set = set()

for i in range(N):
    S[i] = input()
    if S[i] in toroku_set:
        continue
    else:
        # i日目の登録ユーザ名が未登録の場合、その日を記録
        print(i+1)
        toroku_set.add(S[i])





