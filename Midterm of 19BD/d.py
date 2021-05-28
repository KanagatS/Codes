s = input()

x1, y1 = map(int, input().split())
x, y = 0, 0

for i in range(len(s)):
    if x1 == x and y1 == y:
        print('Passed')
        break
    elif s[i] == 'L':
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y += 1
    elif s[i] == 'D':
        y -= 1
else:
    print('Missed')
