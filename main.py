import create
import sqlite3
import os
from users import UsersService

def main():
    if not os.path.exists('mydb.db'):
        conn = sqlite3.connect('mydb.db')
        create.main(conn)
    else:
        conn = sqlite3.connect('mydb.db')
    userService = UsersService(conn)
    # add friend service
    # add post service

    userInput = ""
    while userInput != "exit":
        userInput = input("What would you like to do? ")
        if userInput == "get all users":
            users = userService.get_all_users()
            for user in users:
                print(user)
        if userInput == "get user by id":
            user_id = input("What is the user id? ")
            user = userService.get_user(user_id)
            print(user)
        if userInput == "get user by email":
            email = input("What is the email? ")
            user = userService.get_user_by_email(email)
            print(user)
        if userInput == "get user by name":
            name = input("What is the name? ")
            user = userService.get_user_by_name(name)
            print(user)
        
        else:
            print("Invalid input. Please try again. " + userInput)


    return 0


if __name__ == '__main__':
    main()