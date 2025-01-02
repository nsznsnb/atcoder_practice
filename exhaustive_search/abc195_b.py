# みかんの重さのA:最小値、B:最大値、W:選んだみかんの重さ(kg)の合計
A, B, W = map(int, input().split())
# 1kg = 1000g
kg_unit = 1000
# グラム換算
W2 = W * kg_unit

# 選んだミカンの個数の最小値
num_max = 0
# 選んだミカンの個数の最大値
num_min = 2 ** 30
# 全探索
for n in range(10**6+1):
    if A * n <= W2 <= B * n:
        num_max = max(num_max, n)
        num_min = min(num_min, n)

if num_max == 0:
    print("UNSATISFIABLE")
else:
    print(num_min, num_max)
