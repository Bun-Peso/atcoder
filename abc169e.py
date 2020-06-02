import itertools
N = int(input())
AB = [list(map(int, input().split())) for n in range(N)]
sortA = sorted(AB, key= lambda x:x[0])
sortB = sorted(AB, key= lambda x:x[1])
if N % 2 == 0:
  k1 = int(N/2-1)
  k2 = int(N/2)
  minM = sortA[k1][0] + sortA[k2][0]
  maxM = sortB[k1][1] + sortB[k2][1]
  print(maxM-minM+1)
else:
  k = int((N+1)/2)-1
  A = sortA[k][0]
  B = sortB[k][1]
  print(B-A+1)