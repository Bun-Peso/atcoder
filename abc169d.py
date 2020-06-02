N = int(input())
arr = []
for i in range(2, int(-(-N**0.5//1))+1):
  if N == 1:
    break
  if N % i == 0:
    cnt = 0
    while N % i == 0:
      cnt += 1
      N = int(N / i)
    arr.append([i, cnt])

if N != 1:
  arr.append([N, 1])

n = 0
for p, e in arr:
  temp = e
  j = 0
  while temp > 0:
    j += 1
    temp = temp - j
    if temp < 0:
      break
    n += 1

print(n)
    
