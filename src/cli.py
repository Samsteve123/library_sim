from queries import *
from db_util import initialize_database
import os

if __name__ == "__main__":
    if not os.path.exists("book_borrowing.db"):
        initialize_database()
    while(True):
        print("What would you like to do?:")
        response = input("add or delete?:")
        if response == "add":
            title = input("Title: ")
            author = input("Author: ")
            add_book(title, author)
            print("Book added.")
        elif response == "delete":
            title = input("Title: ")
            author = input("Author: ")
            remove_book(title, author)
            print("Book deleted")
        elif response == "quit":
            exit()
        elif response == "add user":
            name = input("name:")
            add_user(name)
            print("user added")
        else:
            print("Option not recognized.")
