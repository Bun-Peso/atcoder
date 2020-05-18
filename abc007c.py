import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
startY, startX = map(int, input().split())
goalY, goalX = map(int, input().split())
startX -= 1
startY -= 1
goalX -= 1
goalY -= 1
c = [list(map(str, input())) for r in range(R)]
d = [[float('inf')] * C for r in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque()
que.append([startY, startX])

def bfs():
  while que:
    y, x = que.popleft()
    d[startY][startX] = 0
    if y == goalY and x == goalX:
      break
    else:
      for j in range(4):
        ny = y + dy[j]
        nx = x + dx[j]
        if 0 <= nx <= C and 0 <= ny <= R and c[ny][nx] != '#' and d[ny][nx] == float('inf'):
          que.append([ny, nx])
          d[ny][nx] = d[y][x] + 1
  return d[goalY][goalX]




print(bfs())