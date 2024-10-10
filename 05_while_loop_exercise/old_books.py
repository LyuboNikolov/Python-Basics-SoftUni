searched_book = input()
books_counter = 0
current_book = input()
book_is_found = False
while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        print(f"You checked {books_counter} books and found it.")
        break
    books_counter += 1
    current_book = input()

if not book_is_found:
    print(f"The book you search is not here!\nYou checked {books_counter} books.")
