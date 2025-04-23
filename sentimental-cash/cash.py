# TODO
from cs50 import get_float

change = get_float("Change owed: ")
while change < 0:
    change = get_float("Change owed: ")

cent = int(change * 100)

quarters = int(cent / 25)
cent = cent - quarters * 25

dimes = int(cent / 10)
cent = cent - dimes * 10

nickels = int(cent / 5)
cent = cent - nickels * 5

pennies = int(cent)

coins = quarters + dimes + nickels + pennies

print(coins)
