class Post:
    def __init__(self, postId, user_id, body, rating, dateCreated):
        self.id = postId
        self.user_id = user_id
        self.body = body
        self.rating = rating
        self.dateCreated = dateCreated
      
    def __str__(self):
      return f"Post ID: {self.id} \nUser ID: {self.user_id} \nBody: {self.body} \nRating: {self.rating} \nDate Created: {self.dateCreated}\n"
