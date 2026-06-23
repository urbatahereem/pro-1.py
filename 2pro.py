"""2️⃣ Library Management System
Isme:

✔ Add book
✔ Issue book
✔ Return book
✔ Track available books

Concepts:
Classes
Lists
File Handling"""

# import json
# books = {}
# import json

# try:
#     with open("books.json", "r") as file:
#         books = json.load(file)
# except:
#     books = {}

# while True:
#     print("\n<-----------------------Library Management System------------------------------>")
#     print("1. Add book.")
#     print("2. Issue book.")
#     print("3. Return book.")
#     print("4. Tracker Available book.")
#     print("5. Exit")

#     choose = input("please choose the option: ")

#     if choose == "1":
#         print("Add book")

#     elif choose == "2":
#         print("Issue book")

#     elif choose == "3":
#         print("Return book")

#     elif choose == "4":
#         print("Tracker Available book")

#     elif choose == "5":
#         print("Exit")

#     else:
#         break

#     if choose == "1":
#         book = input("enter a book name: ")
#         price = int(input("enter a price: "))
#         auther = input("enter a auther name: ")
#         # date = int(input("enter a purches date: "))

#         books[book] = {
#             "price": price,
#             "author": auther
#         }
            
#         with open ("books.json", "w")as file:
#             json.dump(books, file, indent=4)
#         print("data saved successfully!")
        
#     elif choose == "2":
#         issue_book = input("book name: ")
#         if issue_book in books:
#             print("there is issue! ")
#         else:
#             print("every thing is nice")

#     elif choose == "3":
#         return_book = input("enter a book name: ")

#         if return_book in books:
#             del books[return_book]

#         with open("books.json", "w") as file:
#             json.dump(books, file, indent=4)

#             print("Book Returned Successfully!")

#     elif choose == "4":
#         if books:
#             for book, details in books.items():
#                 print(f"\nBook: {book}")
#                 print(f"Price: {details['price']}")
#                 print(f"Author: {details['author']}")
#         else:
#             print("No Books Available!")

#     elif choose == "5":
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Option!")



class Library:
    def __init__(self):
        self.books = {}

    # Add book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")

        if book_id in self.books:
            print("Book already exists!")
        else:
            self.books[book_id] = {
                "name": book_name,
                "available": True
            }
            print("Book added successfully!")

    # Issue book
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        if book_id in self.books:
            if self.books[book_id]["available"]:
                self.books[book_id]["available"] = False
                print("Book issued successfully!")
            else:
                print("Book is already issued!")
        else:
            print("Book not found!")

    # Return book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        if book_id in self.books:
            if not self.books[book_id]["available"]:
                self.books[book_id]["available"] = True
                print("Book returned successfully!")
            else:
                print("Book was not issued!")
        else:
            print("Book not found!")

    # Show books
    def show_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("\nLibrary Books:")
            for book_id, info in self.books.items():
                status = "Available" if info["available"] else "Issued"
                print(
                    f"ID: {book_id} | Name: {info['name']} | Status: {status}"
                )


# Main program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.issue_book()

    elif choice == "3":
        library.return_book()

    elif choice == "4":
        library.show_books()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")



        




