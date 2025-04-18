from database.db import connect_db

def get_all_genres():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT genre FROM movies")
    genres = cursor.fetchall()
    conn.close()
    return [genre[0] for genre in genres]

def get_movies_by_genre(genre):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE LOWER(genre) = ?", (genre.lower(),))
    return cursor.fetchall()

def recommend_based_on_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT genre FROM movies
        JOIN ratings ON ratings.movie_id = movies.id
        WHERE ratings.user_id = ?
        GROUP BY genre
        ORDER BY AVG(ratings.rating) DESC
        LIMIT 1
    ''', (user_id,))
    row = cursor.fetchone()
    if row:
        return get_movies_by_genre(list(row[0]))
    return []
