s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i],sep='')

for i in range(len(s)):
    if i % 2 == 1:
        #print(s[i])
        print(s[i], end='\n')

print(s[::-1])

s = s[::-1]

for i in range(len(s)):
    if i % 2 == 0:
        #print(s[i])
        print(s[i], end='\n')

print(len(s))
