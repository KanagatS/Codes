n = int(input())
sm = 0.0

for i in range(0, n + 1):
    sm += 4*(((-1)**n) / (2*n + 1))

print(sm)


