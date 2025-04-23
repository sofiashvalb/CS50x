import sys

names = ["Billy", "Sofie", "Charlie", "Dorie", "Ron", "Harry"]
name = input("Name: ")
if name in names:
    print("Found")
    sys.exit(0)
else:
    print("Not found")
    sys.exit(1)
