from queries import *
from db_util import initialize_database
import os

if __name__ == "__main__":
    if not os.path.exists("library_inventory.db"):
        initialize_database()
    while(True):
        response = input("What would you like to do?:")
        if response == "add":
            title = input("Title: ")
            author = input("Author: ")
            add_book(title, author)
            print("Book added.")
        elif response == "delete":
            title = input("Title: ")
            remove_book(title)
            print("Book deleted")
        elif response == "quit":
            exit()
        elif response == "add user":
            name = input("name:")
            add_user(name)
            print("user added")
        elif response == "remove user":
            name = input("name:")
            remove_user(name)
            print("user removed")
        elif response == "search":
            title = input("Title:")
            print(search_book(title))
        else:
            print("Option not recognized.")
