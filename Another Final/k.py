s = set([int(i) for i in input().split()])
s1 = set([int(i) for i in input().split()])
print(*sorted(s.symmetric_difference(s1)))