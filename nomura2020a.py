h1, m1, h2, m2, k = map(int, input().split())

t = (h2*60+m2)-(h1*60+m1)
print(t - k)