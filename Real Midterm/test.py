n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n, m+1):
    if i not in l:
        print(i, end = ' ')