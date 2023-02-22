
class UsersService:

    def __init__(self, db):
        self.db = db

    def get_all_users(self):
        return self.db.execute('SELECT * FROM users').fetchall()

    def get_user(self, user_id):
        return self.db.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()
    
    def get_user_by_email(self, email):
        return self.db.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

    def get_user_by_name(self, name):
        return self.db.execute(
            'SELECT * FROM users WHERE name = ?', (name,)
        ).fetchone()

    def add_user(self, name, password):
        self.db.execute(
            'INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
            (name, name + "@user.com", password)
        )
        self.db.commit()  
        return self.get_user_by_name(name)  