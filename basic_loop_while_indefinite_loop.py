"""
Looping program of books read with WHILE
"""
book_count = 10
print(f"Budi has {book_count} books")

print('Mom said, "Read and master all your books"')

mastered_count = 0
total_read_count = 0
print("Budi reads 1 unread and hasn't mastered book")
print(f"Number of books Budi has read and mastered are {mastered_count}")

while total_read_count < book_count * 2:
    total_read_count = total_read_count + 1
    if mastered_count == 9:
        print(f"Budi reads the {mastered_count + 1}th book")
    else:
        mastered_count = mastered_count + 1
        print(f"Budi has read {mastered_count} books")

print(f"Number of books Budi has read and mastered are {mastered_count}")

if mastered_count < book_count:
    print("Budi reports to mom that not all the books he read can be mastered")
else:
    print(f"Budi reports to mom that he had read all his {book_count} books")
