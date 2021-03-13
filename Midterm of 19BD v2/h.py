n, k = map(int, input().split())
check = False
for i in range(n):
    a, b, c = map(int, input().split())
    if (a + b + c) / 3 >= k:
        check = True
if check:
    print("YES")
else:
    print("NO")
