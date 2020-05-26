from collections import deque
X, Y = map(int, input().split())
que = deque()
que.append(X)
ans = 1

while que:
  x = que.popleft()
  nx = x * 2
  if nx <= Y:
    que.append(nx)
    ans += 1

print(ans)