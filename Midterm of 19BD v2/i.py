n = int(input())
list = [int(i) for i in input().split()]
if list == sorted(list):
    print("Interesting")
else:
    print("Not interesting")
