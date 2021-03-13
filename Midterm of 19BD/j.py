import re
import sys
text = open('input.txt', 'r')
dict = {}
pattern_name = re.compile("\"name\": \".+\",")
pattern_price = re.compile("\"price\": \".+\",")
pattern_discount = re.compile("\"discount\": \".+\"")

string_name = re.compile("[A-Z][a-z]+.[a-z]+.[a-z]+")
string_price = re.compile("[0-9]+")
string_discount = re.compile("[0-9]+")

list_1 = pattern_name.findall(text.read())
list_2 = pattern_price.findall(text.read())
list_3 = pattern_discount.findall(text.read())

for i in range(len(list_1)):
    name = string_name.findall(list_1[i])[0]
    price = string_price.findall(list_2[i])[0]
    discount = string_discount.findall(list_3[i])[0]
    dict[name] = int(price) - int(price) * int(discount) // 100

for i in sorted(dict.items(), key=lambda x: (x[1], x[0])):
    print("Name: " + i[0] + "\n" + "Price: " + str(i[1]))
    exit()
