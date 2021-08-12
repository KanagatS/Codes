def checkpos(s):
    l1, l2 = [], []
    one, two = None, None

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

    if one == True and two == True:
        return True
    else:
        return False


def ideal(s):
    if len(s) % 2 == 0:
        if s[0][0].isupper() == True:
            if s[-1].count('3') == 2:
                if checkpos(s):
                    return True
    return False


for _ in range(int(input())):
    s = input().split()
    print('Wow! That is perfect') if ideal(s) else print('Seriously?')
