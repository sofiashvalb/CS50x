import re
import sys

def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

sum = 0

while True:
    try:
        item = input("Item: ")
        item = titlecase(item)
        if item in menu:
            sum += menu[item]
            print(f"Total: $", end="")
            print("%.2f" %sum)

    except EOFError:
        print()
        break


