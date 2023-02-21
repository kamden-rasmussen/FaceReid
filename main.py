import create
import sqlite3
import os
from users import UsersService
from posts import PostsService

def main():
    if not os.path.exists('mydb.db'):
        conn = sqlite3.connect('mydb.db')
        create.main(conn)
    else:
        conn = sqlite3.connect('mydb.db')
    userService = UsersService(conn)
    postsService = PostsService(conn)
    # add friend service
    # add post service

    userInput = ""
    while userInput != "exit":
        userInput = input("What would you like to do? ")
        match userInput:
            # -------------------- USERS --------------------
            case "get all users":
                users = userService.get_all_users()
                for user in users:
                    print(user)
            case "get user by id":
                user_id = input("What is the user id? ")
                user = userService.get_user(user_id)
                print(user)
            case "get user by email":
                email = input("What is the email? ")
                user = userService.get_user_by_email(email)
                print(user)
            case "get user by name":
                name = input("What is the name? ")
                user = userService.get_user_by_name(name)
                print(user)
            
            # -------------------- POSTS --------------------

            case "get all posts":
                posts = postsService.get_all_posts()
                for post in posts:
                    print(post)
            case "get post by id":
                post_id = input("What is the post id? ")
                post = postsService.get_post(post_id)
                print(post)
            case "get post by user id":
                user_id = input("What is the user id? ")
                posts = postsService.get_post_by_user_id(user_id)
                for post in posts:
                    print(post)
            
            
            # -------------------- Mangement --------------------
            
            case "exit":
                print("Goodbye!")
            
            case _:
                print("Invalid input. Please try again. " + userInput)

    return 0


if __name__ == '__main__':
    main()