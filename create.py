import sqlite3

def createTables():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY, body TEXT, user_id INTEGER, created_at DATETIME, FOREIGN KEY(user_id) REFERENCES users(id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS friends
                    (user_id INTEGER, friend_id INTEGER, following BOOL, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(friend_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()