l = list(map(int, input().split()))
cnt = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            cnt += 1
print(cnt)