n = int(input())
cur, cnt = 1, 0
for i in range(1, n+1):
    print(cur, end=' ')
    cnt += 1
    if cnt == cur:
        cur += 1
        cnt = 0
