import re
pattern = r"(?P<year>1[0-9]{3}).(?P<month>\d{2}).(?P<day>\d{2})"
x = re.search(pattern, input())
if 1299 <= int(x.group('year')) <= 1922 and 1 <= int(x.group('month')) <= 12 and 1 <= int(x.group('day')) <= 31:
    print('YES')
else:
    print('NO')