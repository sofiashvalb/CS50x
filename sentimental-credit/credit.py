# TODO
from cs50 import get_string
#prompts the user for a credit card number
card = get_string("Number: ")
length = len(card)
if length == 15:
    print("AMEX")
elif length == 13:
    print("VISA")
elif length == 16:
    for i in range(length):
        if i[0] == 5:
            if i[1] == 1 or i[1] == 2 or i[1] == 3 or i[1] == 4 or i[1] == 5:
                print("MASTERCARD")
        elif i[0] == 4:
            print("VISA")
else:
    print("INVALID")





#print whether it is a valid American Express, MasterCard, or Visa card number
#AMEX\n or MASTERCARD\n or VISA\n or INVALID\n
print()
