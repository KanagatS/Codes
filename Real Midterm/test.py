# f = open('test.txt')
# for i in f:
#     print(i)
# f.close()

# f = open('test2.txt', 'w')
# f.write('Kanagat will recieve full on midterm\n')
# f.write('Here is another second text\n')
# f.write('Here is another third text\n')
# f.close()

# f = open('test2.txt', 'a')
# f.write('The fourth text')

# f = open('test2.txt', 'r')
# print(f.read())

# f = open('test3.txt', 'x')
# f.write('Hello World')
# f.close()

import os
os.remove('test.txt', 'test2.txt')