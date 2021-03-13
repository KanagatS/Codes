import sys
dict = {}
list = str(sys.stdin.read()).split()
for i in list:
    dict[i] = dict.get(i, 0) + 1
for key, value in sorted(dict.items(), key=lambda x: (x[0], x[1])):
    if value % 2 == 0:
        print(key)