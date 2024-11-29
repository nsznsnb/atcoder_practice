# 社員数
N = int(input())
# 社員番号iの直属の社員番号A[i]
A = [None] * (N+1)

tmp = list(map(int,input().split()))
for i in range(2, N+1):
    A[i] = tmp[i-2]

# 各社員番号ごとに直属の部下の社員番号を格納
G = [[] for i in range(N+1)]

for i in range(2, N+1):
    G[A[i]].append(i)

# 直属の部下の人数を出力
for i in range(1, N+1):
    print(len(G[i]))


