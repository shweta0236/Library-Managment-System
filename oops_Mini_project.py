# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    list_of_books = []
    library_name = ""
    lend_book_records = {}

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name

    def DisplayBook(self):
        print(f"{self.library_name} Books List :")
        print("{:<100} {:<40}".format("Book", "Author"))
        for bookname, author in self.list_of_books.items():
            print("{:<100} {:<40}".format(bookname, author))

    def LendBook(self):
        l1.DisplayBook()
        user_name = input("Enter Your Name : ")
        lend_book = input("Enter the the book name which you want to lend : ")
        if (lend_book not in self.lend_book_records.keys()) and (lend_book in self.list_of_books.keys()):
            self.lend_book_records[lend_book] = user_name
            print(f"{user_name} lend the book {lend_book}")
            print(self.lend_book_records)

        else:
            print(f"Book {lend_book} is lent by {self.lend_book_records[i]} ")

    def AddBook(self):
        new_book = input("Enter the Book you want to add : ")
        author = input("Enter the Author of book : ")
        if new_book not in self.list_of_books.keys():
            self.list_of_books[new_book] = author
            print(f"Your Book {new_book} is Added!")

    def ReturnBook(self):
        user_name = input("Enter Your Name : ")
        return_book = input("Enter the the book name which you want to return : ")
        if return_book in self.lend_book_records.keys() and user_name in self.lend_book_records.values():
            del self.lend_book_records[return_book]
            print(f"Book {return_book} is return by {user_name}")
            # print(self.lend_book_records)
        else:
            print(f"we can't found the book {return_book} in our Records")


if __name__ == '__main__':

    with open("List_of_book.txt", "rt+", encoding='utf-8') as books:
        bookList = {}
        for i in books.readlines():
            bookList[i.replace('\n', '').split("-")[1]] = i.split("-")[0]

    LibraryName = "Shweta Library"
    l1 = Library(bookList, LibraryName)

    while True:
        print(f"\n##### Welcome to {LibraryName} #####")
        print("Select the Operation:\n"
              " 1.) Display Books\n"
              " 2.) Lend Book\n"
              " 3.) Add Book\n"
              " 4.) Return Book\n"
              " 5.) Quit\n")
        op = int(input("Enter the Your choice: "))
        if op == 1:
            l1.DisplayBook()

            asking = input("if you want to continue press y: ")
            if asking == 'y':
                continue
            else:
                break

        elif op == 2:
            l1.LendBook()
            asking = input("if you want to continue press y: ")
            if asking == 'y':
                continue
            else:
                break

        elif op == 3:
            l1.AddBook()
            asking = input("if you want to continue press y: ")
            if asking == 'y':
                continue
            else:
                break

        elif op == 4:
            l1.ReturnBook()
            asking = input("if you want to continue press y: ")
            if asking == 'y':
                continue
            else:
                break

        elif op == 5:
            exit()
        else:
            print("Please enter valid input")
            continue
