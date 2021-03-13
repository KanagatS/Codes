a = int(input())
hour = a % (60 * 24) // 60
minute = a % 60
print (hour, minute)