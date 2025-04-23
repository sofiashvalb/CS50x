books = []

# Add three books to your shelf
for i in range(3):
    book = dict()
    book['title'] = input("title: ").capitalize().strip()
    book['author'] = input("author: ")
    books.append(book)


# Print book titles
for book in books:
    print(book['title'])
