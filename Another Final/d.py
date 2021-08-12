a, b = map(int, input().split())

l = [int(i) for i in input().split()]

for i in range(a, b+1):
    if i not in l:
        print(i, end=' ')
