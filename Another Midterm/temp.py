s = input().split()
one, two = None, None
l1, l2 = [], []
for i in range(len(s)):
    if s.index(s[i]) % 2 != 0:
        l1.append(s[i])
    else:
        l2.append(s[i])

for i in range(len(l1)):
    if (len(l1[i]) % 2 == 0):
        one = True
for i in range(len(l2)):
    if (len(l2[i]) % 2 != 0):
        two = True


print(one, two)
