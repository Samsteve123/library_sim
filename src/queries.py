from db_util import get_connection

def add_book(title, author):
    with get_connection() as conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.execute("UPDATE books SET num_copies=num_copies+1 WHERE title=(?)", (title,))

def remove_book(title):
    with get_connection() as conn:
        conn.execute("DELETE FROM books WHERE title=(?)", (title,))

def add_user(name):
    with get_connection() as conn:
        conn.execute("INSERT INTO users (name) VALUES (?)", (name,))

def remove_user(name):
    with get_connection() as conn:
        conn.execute("DELETE FROM users WHERE  name=(?)", (name,))

def search_book(title):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, num_copies FROM books WHERE title=(?)", (title,))
        return cursor.fetchall()



# def checkout_book(title, author):
#     with get_connection() as conn:
