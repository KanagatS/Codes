s = [int(i) for i in input().split()]
cnt = 0

for i in range(len(s)):
    if s.count(s[i]) == 1:
        cnt += s[i]

print(cnt)
