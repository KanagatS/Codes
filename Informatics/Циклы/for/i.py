n = int(input())
sm = 0.0

def fact(n):
    ff = 1.0
    for i in range (1, n+1):
        ff *= i
    return ff

for i in range (1, n+1):
   sm += 1/fact(i)

print (sm + 1)