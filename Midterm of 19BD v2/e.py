n = int(input())
dict = {}

for i in range(n):
    list = [i for i in input().split()]
    dict[list[0]] = list[2::1]

k = int(input())

for i in range(k):
    city = input()
    result = ''
    for key, value in dict.items():
        if city in value:
            result = key
            break
    if result:
        print(result)
    else:
        print("Unknown")