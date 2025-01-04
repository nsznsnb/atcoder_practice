N = int(input())

ans = False
for i in range(30):
    for j in range(30):
        if 4 * i + 7 * j == N:
            ans = True
            break

print("Yes" if ans else "No")