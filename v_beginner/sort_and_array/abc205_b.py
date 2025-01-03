N = int(input())
A = list(map(int, input().split()))

A.sort()
B = list(range(1,N+1))
if(all(A[i] == B[i] for i in range(N))):
    print("Yes")
else:
    print("No")