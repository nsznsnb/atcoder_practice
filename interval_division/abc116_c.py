
# 花の本数
N = int(input())
# 花壇の花の高さ
H = list(map(int, input().split()))

# 水やりの回数
ans = 0
while max(H) > 0:
    i = 0
    while i < N:
        if H[i] == 0:
            i += 1
        else:
            # 連続する区間の始まり
            ans += 1
            while i < N and H[i] > 0:
                # 水をやった花の高さを減らす
                H[i] -= 1
                i += 1

print(ans)