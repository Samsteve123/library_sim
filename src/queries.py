from db_util import get_connection

def add_book(title, author):
    with get_connection() as conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

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
        cursor.execute("SELECT title, author, COUNT(title) FROM books WHERE title=(?) GROUP BY title", (title,))
        return cursor.fetchall()

def list_all_books():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, author, COUNT(title) FROM books GROUP BY title, author")
        return cursor.fetchall()
#"SELECT DISTINCT title, author, COUNT(title) FROM (SELECT DISTINCT author, title FROM books) GROUP BY author"
