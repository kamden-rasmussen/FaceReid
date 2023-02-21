from post import Post

class PostsService:
    def __init__(self, db):
        self.db = db

    def get_all_posts(self):
        return self.db.execute('SELECT * FROM posts').fetchall()

    def get_post(self, post_id):
        return self.db.execute(
            'SELECT * FROM posts WHERE id = ?', (post_id,)
        ).fetchone()

    def get_post_by_user_id(self, user_id):
        return self.db.execute(
            'SELECT * FROM posts WHERE user_id = ?', (user_id,)
        ).fetchone()

    def add_post(self, body, user_id):
        self.db.execute(
            'INSERT INTO posts (body, user_id) VALUES (?, ?)',
            (body, user_id)
        )
        self.db.commit()
    
    def upvote_post(self, post_id):
        self.db.execute(
            'UPDATE posts SET votes = votes + 1 WHERE id = ?', (post_id,)
        )
        self.db.commit()

    def downvote_post(self, post_id):
        self.db.execute(
            'UPDATE posts SET votes = votes - 1 WHERE id = ?', (post_id,)
        )
        self.db.commit()

    def get_posts_for_user(self, user_id):
        posts = []
        for post in self.db.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,)).fetchall():
            tempPost = Post(post[0], post[1], post[2], post[3], post[4])
            posts.append(tempPost)
        return posts