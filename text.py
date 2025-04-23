text = "In the great green room"
words = text.split()
print(words)

# Round 1
print("Round 1")
for word in words:
    print(word)
print()
#prints each word from the list

# Round 2
print("Round 2")
for word in words:
    for c in word:
        print(c)
print()
#prints every character in each word of the words list

# Round 3
print("Round 3")
for word in words:
    if "g" in word:
        print(word)
print()
#for every word of the words list, if the word has 'g' in it, prints the word

# Round 4
print("Round 4")
for word in words[2:]:
    print(word)
print()
#for every word in words list, from the third word on the list, prints the word.
#means it won't print the first two words

# Round 5
print("Round 5")
for word in words:
    print("Goodnight Moon")
print()
#for every word on words list, it prints the phrase.
#number of 'words' will mean number of time it will print the same phrase
