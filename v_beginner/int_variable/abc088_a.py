N = int(input())
A = int(input())

# 500円玉を支払った後の残額
rest = N % 500
print("Yes" if rest <= A else "No")