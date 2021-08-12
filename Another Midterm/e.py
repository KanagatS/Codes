ans = {'a': 0, 'b': 0, 'c': 0}
vowels = ['a', 'e', 'o', 'i', 'u']

for _ in range(int(input())):
    l = input().split()

    for i in range(len(l[0])):
        if l[0][i].isupper():
            ans['a'] += 1

    for i in range(len(l[1])):
        if l[1][i] in vowels:
            ans['b'] += 1

    for i in l[2]:
        if i.isdigit():
            ans['c'] += 1

print(ans)
