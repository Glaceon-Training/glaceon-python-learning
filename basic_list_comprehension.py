print("---List Comprehension")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]

print("\n--DEL syntax: DEL 0")
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL 1")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[1]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [:] means [All]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[:]
print(">Book list after:")
for i in (range(0, len(book_list))):
    print(book_list[i])

print("\n--DEL syntax: DEL [0:1] means [Start index 0:Amount deleted 1]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0:1]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [0:2] means [Start index 0:Amount deleted 2]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0:2]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [0:-1] means [Start index 0:Delete index until remains -1]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0:-1]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [0:-2] means [Start index 0:Delete index until remains -2]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0:-2]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [0::2] means [Start index 0:Delete all index:Stepping 2 to delete next index]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park", "Manhattan", "Brooklyn", "Constantine"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0::2]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\n--DEL syntax: DEL [0::3] means [Start index 0:Delete all index:Stepping 3 to delete next index]")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park", "Manhattan", "Brooklyn", "Constantine"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
del book_list[0::3]
print(">Book list after:")
for i in range(0, len(book_list)):
    print(book_list[i])

print("\nMaking new lists with index: [0:3] means [Start index 0:Amount to Take 3")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park", "Manhattan", "Brooklyn", "Constantine"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
new_book_list = book_list[0:3]
print(">New book list:")
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print("\nMaking new lists with index: [0:-2] means [Start index 0:Except last 2")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park", "Manhattan", "Brooklyn", "Constantine"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
new_book_list = book_list[0:-2]
print(">New book list:")
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print("\nMaking new lists with index: [0:-1:2] means [Start index 0:Except last 1:Stepping 2")
book_list = ["The Sweet Spot", "Becoming Wise", "Sapiens", "Central Park", "Manhattan", "Brooklyn", "Constantine"]
print(">Book list before:")
for i in range(0, len(book_list)):
    print(book_list[i])
new_book_list = book_list[0:-1:2]
print(">New book list:")
for i in range(0, len(new_book_list)):
    print(new_book_list[i])
