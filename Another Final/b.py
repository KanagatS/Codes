d = dict()

for i in input().split():
    d[i] = d.get(i, 0) + 1

for key, value in sorted(d.items()):
    print(key + ' - ' + str(value))
