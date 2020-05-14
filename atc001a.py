import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
H, W = map(int, input().split())
C = [input() for h in range(H)]
for c in C:
  if 's' in c:
    start = [C.index(c), c.find('s')]
  if 'g' in c:
    goal = [C.index(c), c.find('g')]

def root(s):
  if s == goal:
    print('Yes')
    sys.exit()
  else:
    C[s[0]] = C[s[0]][:s[1]] + '#' + C[s[0]][s[1]+1:]
    sh = [s[0]-1, s[1]]
    sw = [s[0], s[1]-1]
    se = [s[0], s[1]+1]
    ss = [s[0]+1, s[1]]
    if sh[0] >= 0 and C[sh[0]][sh[1]] != '#':
      root(sh)
    if sw[1] >= 0 and C[sw[0]][sw[1]] != '#':
      root(sw)
    if se[1] <= W-1 and C[se[0]][se[1]] != '#':
      root(se)
    if ss[0] <= H-1 and C[ss[0]][ss[1]] != '#':
      root(ss)

root(start)
print('No') 