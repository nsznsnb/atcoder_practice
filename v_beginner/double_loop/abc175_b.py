N = int(input())
L = list(map(int, input().split()))

def is_ac_triangle(li, lj, lk):
    if li == lj or lj == lk or lk == li:
        return False
    if lj + lk <= li:
        return False
    if li + lj <= lk:
        return False
    if li + lk <= lj:
        return False
    return True

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_ac_triangle(L[i], L[j], L[k]):
                ans += 1

print(ans)

