S = input()
N = len(S)

for i in range(1,N):
    s = S[:N-i]
    if len(s) % 2 == 1:
        continue
    if s[:len(s) // 2] == s[len(s)//2:]:
        print(len(s))
        break

