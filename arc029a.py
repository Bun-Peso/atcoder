N = int(input())
t = [int(input()) for i in range(N)]
ans = list()

for n in range(N):
  if n != 0:
    time1 = max((t[0]+t[n]), (sum(t)-t[0]-t[n]))
  else:
    time1 = float('inf')

  time2 = max(t[n], sum(t)-t[n])
  time = min(time1, time2)
  ans.append(time)
  


print(min(ans))