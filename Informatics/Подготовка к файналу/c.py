s, d = input().split(), dict()

for i in s:
    d[i] = d.get(i, 0) + 1

for key, value in sorted(d.items()):
    print(key + " - " + str(value))
