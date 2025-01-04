N = int(input())
W = 2 * N - 1
S = [input() for _ in range(N)]

T = [S[N-1]]

for i in range(N-2, -1, -1):
    T2 = T[len(T)-1]
    S2 = S[i]
    newT = ""
    for j in range(W):
        if S2[j] == ".":
            newT += "."
        else:
            exist_x = False
            for k in range(-1,2):
                if 0 <= j + k < W and T2[j+k] == "X":
                    exist_x = True
            if exist_x:
                newT += "X"
            else:
                newT += S2[j]
    T.append(newT)

for i in range(N):
    print(T[N - 1 - i])

