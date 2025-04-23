# TODO

n = input("Choose a number between 1-8: ")
while n.isdigit() == False:
    n = input("Choose a number between 1-8: ")

n = int(n)
while n < 1 or n > 8:
    n = int(input("Choose a number between 1-8: "))
for i in range(n, 0, -1):
    print(" " * (i - 1), end="#" * (n - (i - 1)))
    print()
print()

for j in range(n):
    print((n - 1 - j) * " ", end="")
    print((j + 1) * "#", " ", (j + 1) * "#", end="")
    print((n - 1 - j) * " ")


