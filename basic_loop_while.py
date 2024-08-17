"""
Looping program of books read with WHILE
"""
book_count = 10
print(f"Budi has {book_count} books")

print('Mom said, "Read all your books"')

read_count = 0
print("Budi reads 1 unread book")
print(f"Number of books Budi has read are {read_count}")

while read_count < book_count:
    read_count = read_count + 1
    print(f"Budi has read {read_count} books")


print(f"Number of books Budi has read are {read_count}")
print(f"Budi reports to mom that he had re   ad all his {book_count} books")
