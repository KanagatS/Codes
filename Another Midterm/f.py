from re import *
s = input()
p = compile(r"^[a-zA-Z0-9_]{4,}#[0-9]{4}")
m = p.findall(s)
print("Welcome to Discord") if m else print("Invalid password or username")
