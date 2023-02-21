

class FriendsService(object):
    def __init__(self, db):
        self.db = db

    def get_friends(self, user_id):
        friends = []
        for friend in self.db.execute('SELECT * FROM friends WHERE user_id = ?', (user_id,)).fetchall():
            friends.append(friend)
        return friends

    def add_friend(self, user_id, friend_id):
        self.db.execute(
            'INSERT INTO friends (user_id, friend_id) VALUES (?, ?)',
            (user_id, friend_id)
        )
        self.db.commit()

    def unfollow_friend(self, user_id, friend_id):
        self.db.execute(
            'UPDATE friends SET following = 0 WHERE user_id = ? AND friend_id = ?',
            (user_id, friend_id)
        )
        self.db.commit()

    def remove_friend(self, user_id, friend_id):
        self.db.execute(
            'DELETE FROM friends WHERE user_id = ? AND friend_id = ?',
            (user_id, friend_id)
        )
        self.db.commit()

    def INTERNAL_get_friends_for_user(self, user_id):
        friends = []
        for friend in self.db.execute('SELECT * FROM friends WHERE user_id = ? and following = 1', (user_id,)).fetchall():
            friends.append(friend[1])
        return friends