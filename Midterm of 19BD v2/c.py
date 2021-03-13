n = int(input())
s = input().split()
s.sort()
my_set = set(s)
for i in range(len(my_set)):
    print(i+1, s[i])