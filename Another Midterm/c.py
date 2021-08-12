l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
t = int(input())

cnt = 0

for a, b in zip(l1, l2):
    if t in range(a, b+1):
        cnt += 1

print(cnt)
