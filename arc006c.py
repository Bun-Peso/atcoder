import sys
input = sys.stdin.readline

N = int(input())
w = [int(input()) for n in range(N)]
block = list()

for n in range(N):
  if n == 0 or w[n] > max(block): 
    block.append(w[n])
  else:
    for i, b in enumerate(block):
      if b >= w[n]:
        block[i] = w[n]
        break

print(len(block))
