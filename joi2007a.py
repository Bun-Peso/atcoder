import sys
input = sys.stdin.readline

price = int(input())
ans = 0

def change(p):
  global ans
  if p == 0:
    return
  elif p >= 500:
    ans += 1
    change(p-500)
  elif p >= 100:
    ans += 1
    change(p-100)
  elif p >= 50:
    ans += 1
    change(p-50)
  elif p >= 10:
    ans += 1
    change(p-10)
  elif p >= 5:
    ans += 1
    change(p-5)
  elif p >= 1:
    ans += 1
    change(p-1)
  
change(1000-price)
print(ans)