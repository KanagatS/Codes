a = int(input())
b = int(input())
c = int(input())

p1 = a * c
p2 = b * c

if p2 >= 100:
    p1 += p2 // 100
    p2 %= 100
    print (p1, p2, sep = " ")

elif p2 > 0 and p2 < 100:
    print (p1, p2, sep = " ")

