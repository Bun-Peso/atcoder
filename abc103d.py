import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for m in range(M)]

ab.sort(key= lambda x: x[1])
removed = -1
ans = 0

for a, b in ab:
  if a > removed:
    removed = b - 1
    ans += 1

# ans = float('inf')
# bridge = [False] * (N-1)
# def function1(i, s):
#   global ans
#   if i == M:
#     ans = min(ans, s)
#     return
#   a = ab[i][0] - 1
#   b = ab[i][1] - 1
#   if any(bridge[a:b]):
#     function1(i+1, s)
#   for j in range(a, b):
#     print(i, j, s)
#     bridge[j] = True
#     print(bridge)
#     s += 1
#     function1(i+1, s)


# function1(0, 0)
print(ans)