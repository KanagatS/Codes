l = [int(i) for i in input().split()]
print('YES') if len(l) == len(set(l)) else print('NO')
