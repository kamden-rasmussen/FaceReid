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

    userInput = input("What would you like to do? ")
    while userInput != "exit":
        userInput = input("What would you like to do? ")
        if userInput == "get all users":
            users = userService.get_all_users()
            for user in users:
                print(user)


    return 0


if __name__ == '__main__':
    main()