n = int(input())
list = []
s = set(input())
list.append(s)
for i in range(n - 1):
    list.append(set(input()))
final = list[0].intersection(*list)
final = sorted(final)
if final:
    print(*final)
else:
    print("NO COMMON CHARACTERS")
