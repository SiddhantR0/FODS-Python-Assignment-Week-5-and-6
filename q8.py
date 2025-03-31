'''
This is a very flexible library management system. This program allows the user to see the list of books, borrow a book,
check the availability of the book, search for a book, add a book. Progam has clean UI so the user can navigate properely.
Features of OOP and other concept of programming has been used to develop this program.
'''

import csv
import os

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available 

    def to_list(self):
        return [self.book_id, self.title, self.author, "Available" if self.available else "borrowd"]

class Library:
    def __init__(self, filename="question8books.csv"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        book_id, title, author, status = row
                        books.append(Book(book_id, title, author, status == "Available"))
        except FileNotFoundError:
            pass 
        return books

    def save_books(self):
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                for book in self.books:
                    writer.writerow(book.to_list())
        except Exception as e:
            print(f"Error saving to file: {e}")

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))
        self.save_books()
        print("Book added successfully!")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"The book '{book.title}' has been borrowed.")
                else:
                    print(f"Sorry, '{book.title}' is not available to borrow.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"The book '{book.title}' has been returned.")
                else:
                    print(f"'{book.title}' was not borrowd.")
                return
        print("Book not found.")

    def search_book(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            print("\nSearch Results:")
            print("{:<10} {:<30} {:<20} {:<10}".format("Book ID", "Title", "Author", "Status"))
            print("=" * 70)
            for book in found_books:
                print("{:<10} {:<30} {:<20} {:<10}".format(book.book_id, book.title, book.author, "Available" if book.available else "borrowd"))
        else:
            print("No books found matching the search criteria.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nLibrary Books:")
        print("{:<10} {:<30} {:<20} {:<10}".format("Book ID", "Title", "Author", "Status"))
        print("=" * 70)
        for book in self.books:
            print("{:<10} {:<30} {:<20} {:<10}".format(book.book_id, book.title, book.author, "Available" if book.available else "borrowd"))


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(book_id, title, author)

    elif choice == "2":
        book_id = input("Enter Book ID to Borrow: ")
        library.borrow_book(book_id)

    elif choice == "3":
        book_id = input("Enter Book ID to Return: ")
        library.return_book(book_id)

    elif choice == "4":
        keyword = input("Enter book title or author to search: ")
        library.search_book(keyword)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
