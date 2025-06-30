# Book Borrowing System

A mini SQL + Python CLI project to manage books, users, and borrow records.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

```bash
python src/db_utils.py  # To initialize the database
python src/cli.py        # To run the simple CLI
```

## Features
- Add books and users
- Track borrowed books
- Query overdue returns
