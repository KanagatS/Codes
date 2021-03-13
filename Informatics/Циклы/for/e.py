a, b = int(input()), int(input())
summ = 0
for i in range(2, b + 1):
    summ += a ** b
print (summ + a + 1)