N = int(input())

ans = False
for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            ans = True
            break

print("Yes" if ans else "No")