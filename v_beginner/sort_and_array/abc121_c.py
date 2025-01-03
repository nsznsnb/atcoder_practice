N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))

X.sort(key=lambda x: x[0])

i = 0
sum_num = 0
purchase = 0
for i in range(N):
    if sum_num + X[i][1] >= M:
        purchase += X[i][0] * (M - sum_num)
        sum_num = M
        break
    else:
        purchase += X[i][0] * X[i][1]
        sum_num += X[i][1]

print(purchase)