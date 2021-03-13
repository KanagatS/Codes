n = int(input())

list = [int(i) for i in input().split()]

if 0 in list and 1 not in list:
    print("Clean:" + str(n) + "\nDirty:0")
else:
    print("Clean:0\nDirty:" + str(n))
