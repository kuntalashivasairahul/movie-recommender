from database.db import initialize_db, load_movies_from_csv
from recommender import get_movies_by_genre, recommend_based_on_user, get_all_genres
import sqlite3
from tabulate import tabulate

def show_available_genres():
    genres = get_all_genres()
    print("\n🎬 Available Genres:")
    for genre in genres:
        print(f"- {genre}")

def show_all_movies():
    conn = sqlite3.connect("database/movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    print(tabulate(movies, headers=["ID", "Title", "Genre"]))

def rate_movie(user_id):
    show_all_movies()

    movie_id = int(input("Enter movie ID to rate: "))

    conn = sqlite3.connect("database/movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies WHERE id = ?", (movie_id,))
    movie = cursor.fetchone()
    conn.close()

    if movie:
        movie_title = movie[0]
        rating = int(input(f"Enter rating (1-5) for '{movie_title}': "))
    else:
        print("❌ Movie not found!")
        return

    conn = sqlite3.connect("database/movies.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ratings (user_id, movie_id, rating) VALUES (?, ?, ?)",
                   (user_id, movie_id, rating))
    conn.commit()
    conn.close()
    print("✅ Thanks for rating!")

def main():
    print("🎬 Welcome to the Movie Recommender CLI 🎬")
    user_id = int(input("Enter your user ID: "))

    while True:
        print("\nOptions:\n1. Rate a Movie\n2. Recommend by Genre\n3. Personalized Recommendation\n4. Show All Movies\n5. Show Available Genres\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            rate_movie(user_id)
        elif choice == '2':
            show_available_genres()
            genre = input("Enter genre (e.g., Drama, Action): ")
            movies = get_movies_by_genre(genre)
            if movies:
                print(tabulate(movies, headers=["ID", "Title", "Genre"]))
            else:
                print("❌ No movies found for this genre.")
        elif choice == '3':
            recommendations = recommend_based_on_user(user_id)
            print("🎯 Recommended for you:")
            print(tabulate(recommendations, headers=["ID", "Title", "Genre"]))
        elif choice == '4':
            show_all_movies()
        elif choice == '5':
            show_available_genres()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    initialize_db()
    load_movies_from_csv("data/movies.csv")
    main()
