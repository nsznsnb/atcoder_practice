
# 整数nの各桁の和を求める関数
def calc_sum_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

N, A, B = map(int, input().split())

result = 0
for i in range(1, N+1):
    if A <= calc_sum_digits(i) <= B:
        result += i


print(result)