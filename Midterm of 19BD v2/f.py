n = int(input())
s = input()
for i in s:
    val = ord(i)
    if val + n > 90:
        i = chr(val + n - 26)
        print(i, end="")
    else:
        i = chr(val + n)
        print(i, end="")
