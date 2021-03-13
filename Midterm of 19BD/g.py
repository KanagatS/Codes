import re
string, t, s, f = input(), input(), input(), input()
string = string.replace(t, s)
list = re.findall(f, string)
print(len(list))