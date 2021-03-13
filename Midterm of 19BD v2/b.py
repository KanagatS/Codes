import re
s = input()

a = re.search("[A-Z]", s)
b = re.search("[a-z]", s)
c = re.search("[0-9]", s)
d = re.search("[_]", s)

if a and b and c and d:
    print("Found a match!")
else:
    print("Not matched!")
