n = int(input())
d = {'up': 0, 'gg': 0, 'num': 0}
k = 'aoeiu'
for i in range(n):
    s = input()
    for i in range(len(s)):
        if s[i].isupper():
            d['up'] += 1
        elif k.find(s[i]) >= 0:
            d['gg'] += 1
        elif s[i].isdigit():
            d['num'] += 1
print(d)
