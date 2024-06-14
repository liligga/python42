class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT
        )
    """
    DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres"
    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"
    CREATE_GENRES_TABLE = """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    CREATE_BOOKS_TABLE = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            image TEXT,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        ) 
    """
    POPULATE_GENRES = """
        INSERT INTO genres (name)
        VALUES ("Фантастика"),
        ("Драма"),
        ("Ужас"),
        ("Комедия")
    """
    POPULATE_BOOKS = """
        INSERT INTO books (name, price, image, genre_id)
        VALUES ("В конце они умрут", 200, "image/book1.jpg", 2),
        ("Портрет Дариан Грея", 2000, "image/book2.jpg", 3),
        ("Оно", 2000, "image/book2.jpg", 4)
    """
