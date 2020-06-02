N = int(input())
A = list(map(int, input().split()))
if 0 in A:
  print(0)
  exit()
ans = A[0]

for n in range(1,N):
  ans = ans * A[n]
  if ans > 10**18:
    print(-1)
    exit()


print(ans)