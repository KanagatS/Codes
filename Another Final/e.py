s = input().split()
s1 = sorted(s)
cnt = 0

for i in range(len(s)):
    if s[i] != s1[i]:
        cnt+=1

print(cnt)