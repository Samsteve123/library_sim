from db_util import get_connection

def add_book(title, author):
    with get_connection() as conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

def remove_book(title, author):
    with get_connection() as conn:
        conn.execute("DELETE FROM books WHERE title=(?) AND author=(?)", (title, author))

def add_user(name):
    with get_connection() as conn:
        conn.execute("INSERT INTO users (name) VALUES (?)", (name,))


# def checkout_book(title, author):
#     with get_connection() as conn:
