import sqlite3 as sq

# Функция, которая создает бд с таблицами
async def create_db():
    print('Creating database...')

    global db, cur
    db = sq.connect('database.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT
    )""")

    db.commit()

# Функция, которая записывает user_id и username в бд
async def insert_user(user_id, username):
    cur.execute("INSERT OR REPLACE INTO users VALUES(?, ?)", (user_id, username))
    db.commit()