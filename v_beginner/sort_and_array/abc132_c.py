N = int(input())
d = list(map(int, input().split()))

d.sort()

left = d[N // 2 - 1]
right = d[N // 2]

print(right - left)


