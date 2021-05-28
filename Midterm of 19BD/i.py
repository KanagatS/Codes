n = int(input())
l = input().split()
k = int(input())
x, y = '', ''

for i in range(k):
    x += str(l[i])

for i in range(k, n):
    y += str(l[i])

print(int(x)*int(y))