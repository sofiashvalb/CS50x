print("hello, world")
answer = input("What's your name?")
print("Hello,", answer)

x = int(input("x: "))
y = int(input("y: "))
z = x / y
print(x + y)
print(z)
a = int(input("What is a? "))
b = int(input("What is a? "))

if a < b:
    print("a is less than b")
elif x > y:
    print("a is greater than b")
else:
    print("a is equal to b")

c = input("Do you agree? ")
c = c.lower()
if c in ["y", "yes", "yeah"]:
    print("Agreed.")
elif c in ["n", "no"]:
    print("Not agreed.")

