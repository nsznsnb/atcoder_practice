N, K = map(int, input().split())
# 数列
A = list(map(int, input().split()))

S = [0] * (N+1)

# S[i]: i項までの累積和
for i in range(N):
    S[i+1] = S[i] + A[i]

for i in range(N-K+1):
    print(S[i+K] - S[i])