N = int(input())
A = list(map(int, input().split()))
A2 = A * 2
total = sum(A)
K = total // 10

if total % 10 != 0:
    print("No")
    exit()
else:
    left, x = 0, 0
    for right in range(2 * N):
        x += A2[right]
        while x > K:
            x -= A2[left]
            left += 1
        if x == K:
            print("Yes")
            exit()

print("No")


