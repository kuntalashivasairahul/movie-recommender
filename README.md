# 🎬 Movie Recommender CLI

A simple command-line application that recommends movies based on user ratings and genres, powered by Python and SQLite.

---

## 🚀 Features

- ⭐ Rate movies as a user
- 🔍 View movies by genre
- 🎯 Get personalized recommendations
- 🧠 Smart genre-based filtering from past ratings

---

## 📂 Folder Structure

```
movie-recommender/
│
├── data/
│   └── movies.csv         # Sample movie dataset
│
├── database/
│   └── movies.db          # SQLite database (auto-created)
│
├── db.py                  # Handles DB operations
├── recommender.py         # Recommender logic
├── main.py                # CLI interface
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md              # You're reading it!
```

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/kuntalashivasairahul/movie-recommender.git
cd movie-recommender
```

2. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
python main.py
```

---

## 🧪 Sample Interaction

```bash
🎬 Welcome to the Movie Recommender CLI 🎬
Enter your user ID: 1

Options:
1. Rate a Movie
2. Recommend by Genre
3. Personalized Recommendation
4. Exit
Choose an option: 2
Enter genre (e.g., Drama, Action): Drama

  ID  Title                   Genre
----  --------------------   --------
  1   The Shawshank...       Drama
  5   Forrest Gump           Drama
```

---

## 🧠 Technologies Used

- Python 🐍
- SQLite 🗃️
- Pandas 🧮
- Tabulate 📊

---

## 📘 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Author

**Kuntala Shiva Sai Rahul**

GitHub: [@kuntalashivasairahul](https://github.com/kuntalashivasairahul)

---
