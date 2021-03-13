l1, l2 = list(map(int, input().split())), list(map(int, input().split()))
n, cnt = int(input()), 0
for i in range(len(l1)):
    for j in range(len(l2)):
        if (i == j) and ((n in range(l1[i], l2[j]+1)) or (n in range(l2[j], l1[i] + 1))):
            cnt += 1
print(cnt)
