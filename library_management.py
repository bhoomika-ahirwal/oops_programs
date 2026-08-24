class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"

        print(
            f"{self.book_id} | "
            f"{self.title} | "
            f"{self.author} | "
            f"{status}"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nID | Title | Author | Status")

        for book in self.books:
            book.display()

    def issue_book(self, book_id):
        for book in self.books:

            if book.book_id == book_id:

                if book.is_issued:
                    print("Book is already issued.")
                else:
                    book.is_issued = True
                    print("Book issued successfully.")

                return

        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:

            if book.book_id == book_id:

                if not book.is_issued:
                    print("Book is already available.")
                else:
                    book.is_issued = False
                    print("Book returned successfully.")

                return

        print("Book not found.")


library = Library()

while True:

    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Book title: ")
        author = input("Author: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = input("Enter book ID: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Enter book ID: ")
        library.return_book(book_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")