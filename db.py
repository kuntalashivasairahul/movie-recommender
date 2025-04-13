import sqlite3
import pandas as pd

def connect_db():
    return sqlite3.connect("database/movies.db")

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            user_id INTEGER,
            movie_id INTEGER,
            rating INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def load_movies_from_csv(csv_path):
    conn = connect_db()
    df = pd.read_csv(csv_path)
    df.to_sql("movies", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
