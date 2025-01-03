# 整数numが2で何回割れるか
def how_many_times(num):
    counter = 0
    while num % 2 == 0:
        num //= 2
        counter += 1
    return counter

N = int(input())
A = list(map(int, input().split()))

result = min(map(how_many_times, A))

print(result)