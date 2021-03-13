import re
string = input()
sub = input()
pattern = re.compile(sub)
find = pattern.search(string)
if find:
    print("First time " + sub + " occured in position: " + str(find.start()))
else:
    print("Not found")
