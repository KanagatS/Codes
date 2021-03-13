n = int(input())
l = list(input().split())
k = int(input())
x, y = '', ''
for i in range(k):
    x += str(l[i])
for i in range(k, n):
    y += str(l[i])
print(int(x)*int(y))


""" n = int(input())
list = [int(i) for i in input().split()]
k = int(input())
num_1 = ""
num_2 = ""
for i in range(k):
    num_1 += str(list[i])
for i in range(k, n):
    num_2 += str(list[i])
if len(num_1) == 0 or len(num_2) == 0:
    print(0)
    exit()
print(int(num_1) * int(num_2))
 """
