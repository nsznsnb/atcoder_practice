O = input()
E = input()

ans = ""
for i in range(min(len(O), len(E))):
    ans += O[i] + E[i]

if len(O) > len(E):
    ans += O[len(O)-1]

print(ans)