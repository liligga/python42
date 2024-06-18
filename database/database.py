import aiosqlite
from database.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            # создание всех таблиц
            await conn.execute(Queries.CREATE_SURVEY_TABLE)
            await conn.execute(Queries.DROP_GENRES_TABLE)
            await conn.execute(Queries.DROP_BOOKS_TABLE)
            await conn.execute(Queries.CREATE_GENRES_TABLE)
            await conn.execute(Queries.CREATE_BOOKS_TABLE)
            await conn.execute(Queries.POPULATE_GENRES)
            await conn.execute(Queries.POPULATE_BOOKS)
            # здесь может быть создание других таблиц
            # которые нам нужны
            await conn.commit()

    async def execute(self, query: str, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()


    async def fetch(self, query: str, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            conn.row_factory = aiosqlite.Row
            data = await conn.execute(query, params)
            result = await data.fetchall()
            return [dict(row) for row in result]

        # connection = sqlite3.connect("db.sqlite")
        # cursor = connection.cursor()
        # query = cursor.execute("SELECT * FROM books WHERE genre_id = 2")
        # books = query.fetchall()