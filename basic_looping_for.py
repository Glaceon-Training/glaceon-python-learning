"""
Looping program of books read with FOR
"""
book_count = 10
print(f"Budi has {book_count} books")

print('Mom said, "Read all your books"')

read_count = 0
print("Budi reads 1 unread book")
print(f"Number of books Budi has read are {read_count}")

for read_count in range(1, book_count + 1):
    print(f"Budi has read {read_count} books")

print(f"Number of books Budi has read are {read_count}")
print(f"Budi reports to mom that he had read all his {book_count} books")
