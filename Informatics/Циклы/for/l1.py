a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(1002, -1, -1):
    if a*(i**3) + b*(i**2) + c*i + d == 0:
        print(i, end=' ')
