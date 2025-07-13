import sqlite3

def connect_to_db():
    """Connect to a SQLite database."""
    conn = sqlite3.connect("db/prosit_init.db")
    return conn

def create_table(conn, table_name, columns):
    """Create a table in the database."""
    cursor = conn.cursor()
    columns_with_types = ", ".join(columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
    conn.commit()

def insert_data(conn, table_name, data):
    """Insert data into a table."""
    cursor = conn.cursor()
    placeholders = ", ".join(["?"] * len(data))
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
    conn.commit()

def query_data(conn, table_name, condition=None):
    """Query data from a table."""
    cursor = conn.cursor()
    if condition:
        cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}")
    else:
        cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()