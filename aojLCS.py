Q = int(input())
XY = [[list(input().rstrip()) for i in range(2)] for q in range(Q)]


def lcs(xy):
  lx = len(xy[0])
  ly = len(xy[1])
  dp = [[0]*(ly+1) for l in range(lx+1)]
  for i in range(lx):
    for j in range(ly):
      if xy[0][i] == xy[1][j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i][j + 1], dp[i + 1][j])
  return max(dp[lx])

for xy in XY:
  print(lcs(xy))