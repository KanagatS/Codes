a = int(input())
s1 = input().split()
b = int(input())
s2 = input().split()


for i in s1:
    if i in s2:
        s2.remove(i)
        s1.remove(i)
print("Missed students:")

for i in s1:
    print(" - " + i)

print("Not in the group:")

for i in s2:
    print(" - " + i)
