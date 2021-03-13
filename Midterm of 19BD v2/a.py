import re
s = input()

pattern = re.compile("[A-Z][a-z]+")

find = pattern.search(s)

if find:
    print("Found a match!")
else:
    print("Not matched!")
