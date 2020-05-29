import sys
input = sys.stdin.readline

N, W = map(int, input().split())
vw = [list(map(int, input().split())) for n in range(N)]

dp = [[0]*(W+1) for n in range(N+1)]

for n in range(N):
  for w in range(W+1):
    if w < vw[n][1]:
      dp[n+1][w] = dp[n][w]
    else:
      dp[n+1][w] = max(dp[n][w], dp[n+1][w-vw[n][1]] + vw[n][0])
  print(dp[n])

print(dp[N])
print(dp[N][W])