S = input()

if all('0' <= ch <= '9' for ch in S):
    print(int(S)*2)
else:
    print("error")