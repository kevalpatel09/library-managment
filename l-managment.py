class library:
    def __init__(self):
        self.books = ["DSA", "PYTHON FOR BEGINNERS",
                             "COMMPLETE JAVA", "DATA VISUALIZATION", "PYTHON FOR ML"]

    def listOfBooks(self):
        print("Total number of books available :-")
        for i, j in enumerate(self.books):
            print("\t {} {}".format(i, j))

    def bookBorrowed(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You borrowed {book} from the library.")
        else:
            print(
                "Please enter a valid book name OR it has been borrowed by someone else:")

    def bookReturned(self, book):
        if book in self.books:
            print("This book is already present in their :) ")
        else:
            self.books.append(book)
            print(f"You added {book} book in library.")


class student:
    def stuBookBorrowed(self):
        self.b = input("Enter a book name you want to borrow? ---> ")
        return self.b

    def stuReturnedBook(self):
        self.b = input(
            "Enter a book you want to donate or return to libbrabry! : ")
        return self.b


if __name__ == "__main__":

    centralLibrary = library()
    students = student()

    while(True):
        welcomeMsg = '''\n
        --------- WELCOME TO CENTRAL LIBRARY ---------
            i. SELECT '1' TO SEE ALL THE BOOKS
           ii. SELECT '2' TO BORROW A BOOK
          iii. SELECT '3' TO RETURN/DONATE A BOOK
           iv. SELECT '4' TO EXIT THE LIBRARY

        '''
        print(welcomeMsg)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            centralLibrary.listOfBooks()
        elif choice == 2:
            centralLibrary.bookBorrowed(students.stuBookBorrowed())

        elif choice == 3:
            centralLibrary.bookReturned(students.stuReturnedBook())

        elif choice == 4:
            exit()
        else:
            print("Enter a valid book name")
