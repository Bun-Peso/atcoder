# from decimal import *
# A, B = map(float, input().split())
# B = Decimal(B).quantize(Decimal('.01'), rounding=ROUND_DOWN)
# AB = Decimal(A)*Decimal(B)
# print(Decimal(AB).quantize(Decimal('1.'), rounding=ROUND_DOWN))

# 文字列で読み取ればいける
A, B = map(str, input().split())
A = int(A)
B = B.replace('.','')
while len(B) < 3:
  B = B + '0'

B = int(B)
print(A*B//100)
