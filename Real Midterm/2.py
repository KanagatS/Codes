input = open('input.txt', 'r')
output = open('output.txt', 'w')
l = input.read().split()
ok = True

for i in range(1, len(l)):
    if len(l[i]) <= len(l[i-1]):
        ok = False
    else:
        ok = True

if ok:
    output.write('YES')
else:
    output.write('NO')

output = open('output.txt', 'r')
print(output.read())

input.close()
output.close()
