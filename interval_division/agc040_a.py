# a[i] と a[i+1]の大小関係(<,>)を表現する文字列
S = input()
# 大小関係の個数
N = len(S)

# 良い非負正数列
A = [0] * (N+1)
for i in range(N):
    if S[i] == "<":
        A[i+1] = max(A[i+1], A[i]+1)

for i in range(N-1, -1, -1):
    if S[i] == ">":
        A[i] = max(A[i], A[i+1] + 1)

print(sum(A))