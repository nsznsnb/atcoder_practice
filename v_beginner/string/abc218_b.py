alpha = [chr(cd) for cd in range(ord('a'), ord('z')+1)]
P = list(map(int, input().split()))

print("".join([alpha[p-1] for p in P]))

