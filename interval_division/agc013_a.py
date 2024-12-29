N = int(input())
A = list(map(int, input().split()))

i = 0
# 単調非増加列・非減少列に分割できる最小数
ans = 0
while i <= N-1:
    j1 = i
    j2 = i
    # 単調増加列を調べる
    while j1 < N-1 and A[j1] <= A[j1+1]:
        j1 += 1
    # 単調減少列を調べる
    while j2 < N-1 and A[j2] >= A[j2+1]:
        j2 += 1
    ans += 1
    #　より区間の長い方を採用
    i = max(j1+1, j2+1)

print(ans)

