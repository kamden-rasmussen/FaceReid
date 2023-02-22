

class FriendsService(object):
    def __init__(self, db):
        self.db = db

    def get_friends(self, user_id):
        friends = []
        for friend in self.db.execute('SELECT * FROM friends WHERE user_id = ?', (user_id,)).fetchall():
            friends.append(friend)
        return friends

    def add_mutual_friendship(self, user_id, friend_id):
        self.db.execute('''
        INSERT INTO friends (user_id, friend_id) 
        select ?, ?
        where not exists 
            (select 1 
            from friends 
            where user_id = ? 
            and friend_id = ?); 
        ''',(user_id, friend_id, user_id, friend_id)
        )
        self.db.commit()

    def add_friend(self, user_id, friend_id):
        self.add_mutual_friendship(user_id, friend_id)
        self.add_mutual_friendship(friend_id, user_id)

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

    def INTERNAL_get_friends_of_friends(self, user_id):
        friendsOfFriends = []
        random = self.db.execute(
            '''
            SELECT f2.friend_id
            FROM users u1
            join friends f1
            on u1.id = f1.user_id
            join friends f2
            on f1.friend_id = f2.user_id
            where u1.id != f2.friend_id
            and u1.id = ?
            ''', (user_id,))

        for friend in random.fetchall():
            friendsOfFriends.append(friend[0])

        return friendsOfFriends
