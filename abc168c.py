import math
A, B, H, M = map(int, input().split())

dA = (H*60+M)*math.pi/360
dB = M*math.pi/30
dC = abs(dB - dA)
C = (A**2 + B**2 - 2*A*B*math.cos(dC))**(1/2)

print(C)