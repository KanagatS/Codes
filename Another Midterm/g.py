n = int(input())

for _ in range(n):
    l1 = [i for i in input().split()]
    l2 = [i for i in input().split()]

    print('Absent: ', end='')
    for i in sorted(l1):
        if i not in l2:
            print(i, end=' ')

    print()

    print('Lost: ', end='')
    for i in sorted(l2):
        if i not in l1:
            print(i, end=' ')
    print()
