import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

W, H = map(int, input().split())
c = [list(map(int, input().split())) for h in range(H)]
count = 0

def landCount(h, w):
  north = h-1
  west = w-1
  south = h+1
  east = w+1
  move = [True]*8
  c[h][w] = 0
  if 0 <= north < H and c[north][w] == 1:
    landCount(north, w)
  else:
    move[0] = False
  if 0 <= north < H and 0 <= west < W and c[north][west] == 1:
    landCount(north, west)
  else:
    move[1] = False
  if 0 <= west < W and c[h][west] == 1:
    landCount(h, west)
  else:
    move[2] = False
  if 0 <= west < W and 0 <= south < H and c[south][west] == 1:
    landCount(south, west)
  else:
    move[3] = False
  if 0 <= south < H and c[south][w] == 1:
    landCount(south, w)
  else:
    move[4] = False
  if 0 <= south < H and 0 <= east < W  and c[south][east] == 1:
    landCount(south, east)
  else:
    move[5] = False
  if  0 <= east < W and c[h][east] == 1:
    landCount(h, east)
  else:
    move[6] = False
  if 0 <= east < W and 0 <= north < H and c[north][east] == 1:
    landCount(north, east)
  else:
    move[7] = False

for h in range(H):
 for w in range(W):
   if c[h][w] == 1:
    landCount(h, w)
    count += 1

print(count)
