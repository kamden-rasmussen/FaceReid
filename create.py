import sqlite3
from inject_names import *
import random

inject_users = injectUsers()

def createTables():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        email TEXT UNIQUE, 
        password TEXT
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        body TEXT, user_id INTEGER, 
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY(user_id) REFERENCES users(id)
        )''')

    c.execute('''CREATE TABLE IF NOT EXISTS friends(
        user_id INTEGER, 
        friend_id INTEGER, 
        following BOOL, 
        FOREIGN KEY(user_id) REFERENCES users(id), 
        FOREIGN KEY(friend_id) REFERENCES users(id)
        )''')

    print("Tables created successfully")

    conn.commit()
    conn.close()

def insertUsers():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.executemany('''INSERT INTO users (name, email, password) VALUES (?, ?, ?)''', inject_users)

    print( "Users inserted successfully")

    conn.commit()
    conn.close()

def insertFriends():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    for i in range(100):
        user1 = random.randint(1, 200)
        user2 = random.randint(1, 200)
        while user1 == user2:
            user2 = random.randint(1, 200)
        c.execute('''INSERT INTO friends (user_id, friend_id, following) VALUES (?, ?, 1)''', (user1, user2))
        c.execute('''INSERT INTO friends (user_id, friend_id, following) VALUES (?, ?, 1)''', (user2, user1))

    print("Friends inserted successfully")

    conn.commit()
    conn.close()

def insertPosts():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()

    file = open('quotes.csv', 'r')

    for line in file:
        post = line
        user = random.randint(1, 200)
        c.execute('''INSERT INTO posts (body, user_id) VALUES (?, ?)''', (post, user))
    
    conn.commit()
    conn.close()

def main():
    # createTables()
    # insertUsers()
    # insertFriends()
    insertPosts()



