S = input()
T = input()
N = len(S)

if S == T:
    print("Yes")
    exit()
else:
    for i in range(N-1):
        S2 = S[:i] + S[i+1] + S[i] + S[i+2:]
        if S2 == T:
            print("Yes")
            exit()
print("No")