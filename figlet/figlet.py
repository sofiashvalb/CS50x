from sys import argv
from pyfiglet import Figlet
import random

figlet = Figlet()
#You can then get a list of available fonts with code like this:

figlet.getFonts()

if len(argv) == 1:
    font=random.choice(figlet.getFonts())
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
    try:
        figlet.setFont(font=argv[2])
    except:
        print("Invalid usage")
        exit(1)
else:
    print("Invalid usage")
    exit(1)


text = input("Input: ")
print("Output: ", figlet.renderText(text))

exit(0)

