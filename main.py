import create
import sqlite3
import os
from users import UsersService
from posts import PostsService
from friends import FriendsService

def main():
    if not os.path.exists('mydb.db'):
        conn = sqlite3.connect('mydb.db')
        create.main(conn)
    else:
        conn = sqlite3.connect('mydb.db')
    userService = UsersService(conn)
    postsService = PostsService(conn)
    friendsService = FriendsService(conn)

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
            case "create user":
                name = input("What is the name? ")
                password = input("What is the password? ")
                user = userService.add_user(name, password)
                print(user)

            # ------------------- FRIENDS -------------------
            case "get my friends by user id":
                user_id = input("What is the user id? ")
                friends = friendsService.get_friends(user_id)
                for friend in friends:
                    print(friend)
            
            case "unfollow my friend by user id":
                user_id = input("What is the user id? ")
                friend_id = input("What is the friend id? ")
                friendsService.unfollow_friend(user_id, friend_id)
                friends = friendsService.get_friends(user_id)
                for friend in friends:
                    print(friend)

            case "add friend by user id":
                user_id = input("What is the user id? ")
                friend_id = input("What is the friend id? ")
                friendsService.add_friend(user_id, friend_id)
                friends = friendsService.get_friends(user_id)
                for friend in friends:
                    print(friend)
            
            # -------------------- POSTS --------------------
            case "get all posts":
                posts = postsService.INTERNAL_get_all_posts()
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

            case "get my feed by user id":
                user_id = input("What is the user id? ")
                friends = friendsService.INTERNAL_get_friends_for_user(user_id)
                for friend in friends:
                    print()
                    posts = postsService.get_posts_for_user(friend)
                    print("Posts from " + userService.get_user(friend)[1])
                    if posts is not None:
                        for post in posts:
                            print(post)

            case "downvote post by id":
                post_id = input("What is the post id? ")
                postsService.downvote_post(post_id)
            
            case "upvote post by id":
                post_id = input("What is the post id? ")
                postsService.upvote_post(post_id)

            case "get posts friends of friends":
                user_id = input("What is the user id? ")
                friends = friendsService.get_friends_of_friends(user_id)

            case "create post":
                user_id = input("What is the user id? ")
                content = input("What is the body? ")
                post = postsService.add_post(user_id, content)

            # -------------------- Management --------------------
            case "3":
                friends = friendsService.INTERNAL_get_friends_for_user(3)
                for friend in friends:
                    print()
                    posts = postsService.get_posts_for_user(friend)
                    print("Posts from " + userService.get_user(friend)[1])
                    if posts is not None:
                        for post in posts:
                            print(post)
            
            case "4":
                friends = friendsService.INTERNAL_get_friends_of_friends(3)
                for friend in friends:
                    posts = postsService.get_posts_for_user(friend)
                    for post in posts:
                        print(post)
                    
                    

            case "exit":
                print("Goodbye!")
            
            case _:
                print("Invalid input. Please try again. " + userInput)

    return 0


if __name__ == '__main__':
    main()
