def is_ac(s: str):
    if s[A] != "-":
        return False
    for i in range(len(s)):
        if i == A:
            continue
        if not ('0' <= s[i] <= '9'):
            return False
    return True


A, B = map(int, input().split())
S = input()

print("Yes" if is_ac(S) else "No")

