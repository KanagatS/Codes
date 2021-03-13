list = input().split()
print(str(max(list, key=len)) + "\n" + str(len(max(list, key=len))))
