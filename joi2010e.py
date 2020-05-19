import sys
input = sys.stdin.readline
from collections import deque


H, W, N = map(int, input().split())
block = [list(input().rstrip()) for h in range(H)]
goal = [0]*N

for h in range(H):
  if 'S' in block[h]:
    startX = block[h].index('S')
    startY = h
  for n in range(N):
    if str(n+1) in block[h]:
      goal[n] = [block[h].index(str(n+1)), h]

def dfs(sx, sy, gx, gy):
  d = [[float('inf')]*W for h in range(H)]
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  que = deque()
  que.append((sx, sy))
  d[sy][sx] = 0

  while que:
    point = que.popleft()
    if point[0] == gx and point[1] == gy:
      break
    for i in range(4):
      nx = point[0] + dx[i]
      ny = point[1] + dy[i]
      if 0 <= nx < W and 0 <= ny < H and d[ny][nx] == float('inf') and block[ny][nx] != 'X':
        que.append((nx, ny))
        d[ny][nx] = d[point[1]][point[0]] + 1
    
  return d[gy][gx]

ans = dfs(startX, startY, goal[0][0], goal[0][1])
for i in range(1,N):
  ans += dfs(goal[i-1][0], goal[i-1][1], goal[i][0], goal[i][1])

print(ans)
