d = {}
for _ in range(int(input())):
    name, gpa = input().split()
    gpa = int(gpa)

    if not d.get(name):
        d[name] = [1, gpa]
    else:
        d[name][0] += 1
        d[name][1] += gpa

for k, v in sorted(d.items(), key=lambda x: x[1]):
    GPA = v[1] / v[0]
    print(k, ': ', f'{GPA:.3f}', sep='')
