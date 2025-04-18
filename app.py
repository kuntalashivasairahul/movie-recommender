from flask import Flask, render_template, request, redirect
from database.db import connect_db
from recommender.recommender import get_all_genres, get_movies_by_genre, recommend_based_on_user
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    genres = get_all_genres()
    selected_genre = request.form.get('genre')
    genre_movies = get_movies_by_genre(selected_genre) if selected_genre else []

    user_id = request.form.get('user_id')
    user_recommendations = recommend_based_on_user(user_id) if user_id else []

    # Fetch all movies for the rating dropdown
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM movies")
    movies = cursor.fetchall()
    conn.close()

    return render_template('index.html',
                           genres=genres,
                           genre_movies=genre_movies,
                           user_recommendations=user_recommendations,
                           movies=movies)

@app.route('/rate', methods=['POST'])
def rate_movie():
    user_id = request.form['user_id']
    movie_id = request.form['movie_id']
    rating = request.form['rating']

    # Connect to the database and insert the new rating
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ratings (user_id, movie_id, rating)
        VALUES (?, ?, ?)
    ''', (user_id, movie_id, rating))

    # After inserting the rating, get updated recommendations for the user
    user_recommendations = recommend_based_on_user(user_id)

    # Fetch ratings for the user (for display purposes)
    cursor.execute("SELECT * FROM ratings WHERE user_id = ?", (user_id,))
    user_ratings = cursor.fetchall()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Pass user recommendations and ratings to the template
    return render_template('index.html', user_ratings=user_ratings, user_recommendations=user_recommendations)



    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
