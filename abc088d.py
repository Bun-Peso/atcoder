import sys
input = sys.stdin.readline
from collections import Counter
from collections import deque

H, W = map(int, input().split())
s = [list(input().rstrip()) for h in range(H)]

bc = 0
for h in range(H):
  n = Counter(s[h])
  bc += n['#']


def dfs():
  que = deque()
  que.append((0,0))
  di = [1, 0, -1, 0]
  dj = [0, 1, 0, -1]
  d = [[float('inf')]*W for h in range(H)]
  d[0][0] = 0
  while que:
    point = que.popleft()
    if point[0] == H-1 and point[1] == W-1:
      break
    for i in range(4):
      ni = point[0] + di[i]
      nj = point[1] + dj[i]
      if 0 <= ni < H and 0 <= nj < W and d[ni][nj] == float('inf') and s[ni][nj] != '#':
        que.append((ni, nj))
        d[ni][nj] = d[point[0]][point[1]] + 1
  return d[H-1][W-1]

    
score = H*W - bc - dfs() -1 
if dfs() == float('inf'):
  score = -1
print(score)
  