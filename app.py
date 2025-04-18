from flask import Flask, render_template, request
from recommender import get_all_genres, get_movies_by_genre, recommend_based_on_user

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    genres = get_all_genres()
    recommendations = []
    selected_genre = ""
    user_id = ""

    if request.method == 'POST':
        if 'genre' in request.form and request.form['genre']:
            selected_genre = request.form['genre']
            recommendations = get_movies_by_genre(selected_genre)

        elif 'user_id' in request.form and request.form['user_id']:
            user_id = request.form['user_id']
            recommendations = recommend_based_on_user(user_id)

    return render_template('index.html', genres=genres, recommendations=recommendations,
                           selected_genre=selected_genre, user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)
