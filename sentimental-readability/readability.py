# TODO
from cs50 import get_string

text = get_string("Text: ")
text = text.lower()
letters = 0
words = 1
sentences = 0
for x in text:
    if x.isalpha():
        letters += 1

for i in text:
    if i.isspace():
        words += 1

for j in text:
    if j == chr(33) or j == chr(46) or j == chr(63):
        sentences += 1

L = letters * 100 / words
S = sentences * 100 / words
index = (0.0588 * L) - (0.296 * S) - 15.8
index = round(index)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
