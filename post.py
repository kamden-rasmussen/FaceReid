class Post:
    def __init__(self, postId, user_id, body, rating, dateCreated):
        self.id = postId
        self.user_id = user_id
        self.body = body
        self.rating = rating
        self.dateCreated = dateCreated

    def printPost(self):
        print("Post ID: " + str(self.id))
        print("User ID: " + str(self.user_id))
        print("Body: " + self.body)
        print("Rating: " + str(self.rating))
        print("Date Created: " + str(self.dateCreated))
        print()