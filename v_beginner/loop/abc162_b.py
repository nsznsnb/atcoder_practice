N = int(input())

ans = 0
for i in range(1,N+1):
    if i % 3 == 0 and i % 5 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    else:
        ans += i

print(ans)