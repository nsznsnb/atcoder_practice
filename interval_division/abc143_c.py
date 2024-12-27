# 入力サイズ
N = int(input())
# スライムの色
S = input()

# 融合後のスライムの数
ans = 0
i = 0
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    # iからjまでのスライムは融合して一つになる
    ans += 1
    i = j

print(ans)
