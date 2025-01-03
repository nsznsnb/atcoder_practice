N = int(input())
S = input()

alpha = [chr(cd) for cd in range(ord('A'),ord('Z')+1)]
cipha = [None] * len(alpha)
for i in range(len(alpha)):
    cipha[i] = alpha[(i+N) % len(alpha)]


ans = ""
for ch in S:
    cd = ord(ch) - ord('A')
    ans += cipha[cd]

print(ans)
