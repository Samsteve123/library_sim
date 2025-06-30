import sqlite3

DB_PATH = "library_inventory.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    with get_connection() as conn:
        with open("db/schema.sql") as f:
            conn.executescript(f.read())
