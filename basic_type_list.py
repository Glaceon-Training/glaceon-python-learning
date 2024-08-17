book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens"]

print("Show book list:")
print(book_list)

print("\nShow book list with FOR syntax:")
for books in book_list:
    print(books)

print("\nShow book list from indexed syntax:")
print(book_list[0])
print(book_list[1])
print(book_list[2])

print("\nShow book list with FOR and indexed syntax:")
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [232, "Crimson Eyes", -21, 2.453]
print("\nShow book list with FOR and indexed syntax, new list with varied data type:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\nRollover book list:")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens"]
print(book_list)

print('\nAdd one new list:')
book_list.append("Mein Kampf")
print(book_list)

print('\nShow book list with FOR and indexed syntax with new append:')
for i in range(0, len(book_list)):
    print(book_list[i])

print("\nClear list:")
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

print("\nRestore book list:")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(book_list)

print("\nChange first element of the list:")
book_list[0] = "The Bitter Spot"
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n---Take elements with Pop: Pop 0")
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
book_poplist = book_list.pop(0)
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])
print(">Pop list 0:")
print(book_poplist)

print("\n---Take elements with Pop from behind:")
print("--THE FIRST CASE: POP -1")
print(">Book list before:")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
for i in range(0, len(book_list)):
    print(book_list[i])
book_poplist = book_list.pop(-1)
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])
print(">Pop list -1:")
print(book_poplist)

print("\n--THE SECOND CASE: POP -2")
print(">Book list before:")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
for i in range(0, len(book_list)):
    print(book_list[i])
book_poplist = book_list.pop(-2)
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])
print(">Pop list -2:")
print(book_poplist)
