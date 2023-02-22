from post import Post

class PostsService:
    def __init__(self, db):
        self.db = db

    def INTERNAL_get_all_posts(self): # TODO: fix this to use POST objects
        return self.db.execute('SELECT * FROM posts').fetchall()

    def INTERNAL_get_post(self, post_id): # TODO: fix this to use POST objects
        return self.db.execute(
            'SELECT * FROM posts WHERE id = ?', (post_id,)
        ).fetchone()

    def add_post(self, user_id, body):
        self.db.execute(
            'INSERT INTO posts (user_id, body) VALUES (?, ?)',
            (user_id, body)
        )
        self.db.commit()
    
    def upvote_post(self, post_id):
        self.db.execute(
            'UPDATE posts SET rating = rating + 1 WHERE id = ?', (post_id,)
        )
        self.db.commit()

    def downvote_post(self, post_id):
        self.db.execute(
            'UPDATE posts SET rating = rating - 1 WHERE id = ?', (post_id,)
        )
        self.db.commit()

    def get_posts_for_user(self, user_id):
        posts = []
        for post in self.db.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,)).fetchall():
            tempPost = Post(post[0], post[1], post[2], post[3], post[4])
            posts.append(tempPost)
        return posts
