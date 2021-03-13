n = int(input())

l = [int(i) for i in input().split()]

if len(l) == len(set(l)):
    print("YES")
else:
    print("NO")
