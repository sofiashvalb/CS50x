people = {
    "Sofie": "+972-545-903-171",
    "Dor": "+972-502-277-063"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")

s = input("s: ")
t = input("t: ")

if s == t:
    print("same")
else:
    print("not same")

a = input("a: ")
b = a.capitalize()
print(b)

x = 1
y = 2
print(f"x: {x}, y: {y}")
x, y = y, x
print(f"x: {x}, y: {y}")
