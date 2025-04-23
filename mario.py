def main():
    height = get_height()
    for i in range(height):
        for j in range(height):
            print("#","", end="")
        print()
    print(("? ")* height)

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")
main()

for i in range(4):
    print("?", end="")
print()

s = 10
for n in range(s):
    for l in range(s):
        print("* ", end="")
    s = s - 1
    print()


