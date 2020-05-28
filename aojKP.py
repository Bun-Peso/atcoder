import sys
input = sys.stdin.readline

N, W = map(int, input().split())
VW = [tuple() for n in range(N)]

for n in range(N):
  v, w = map(int, input().split())
  vpw = v/w
  VW[n] = (v, w, vpw)

VW.sort(key = lambda x: x[2], reverse=True)
weight = 0
value = 0
while weight < W:
  # print(weight)
  for i, vw in enumerate(VW):
    if (W - weight) >= vw[1]:
      value = value + vw[0]
      weight = weight + vw[1]
      break
    if i == N-1:
      weight = weight + W

print(value)
