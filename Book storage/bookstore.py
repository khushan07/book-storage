books = []

def add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    year = input("Enter year of publication: ")
    books.append({'name': name, 'author': author, 'year': year, 'read': False})
    print("Book added!\n")

def view_books():
    if not books:
        print("No books in the collection.\n")
        return
    for i, book in enumerate(books):
        status = "Read" if book['read'] else "Unread"
        print(f"{i + 1}. {book['name']} by {book['author']} ({book['year']}) - {status}")
    print()

def mark_as_read():
    index = int(input("Enter book number to mark as read: ")) - 1
    if 0 <= index < len(books):
        books[index]['read'] = True
        print("Book marked as read!\n")
    else:
        print("Invalid book number!\n")

def delete_book():
    index = int(input("Enter book number to delete: ")) - 1
    if 0 <= index < len(books):
        books.pop(index)
        print("Book deleted!\n")
    else:
        print("Invalid book number!\n")

def main():
    while True:
        print("1. Add a new Book")
        print("2. View your all Books")
        print("3. Mark a Book as Read")
        print("4. Delete a Book from this directory")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            mark_as_read()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!\n")

if __name__ == "__main__":
    main()
