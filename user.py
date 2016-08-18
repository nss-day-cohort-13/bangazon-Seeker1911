import random
from birdyboard import *
from writer import Writer

class User:
    '''Create a new user and send dictionary to writer to save user'''
    def __init__(self, first_name, last_name, user_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_id = user_id

    def new_account(users):
        print("What's your first name?")
        first_name = input('>')
        print("What's your last name?")
        last_name = input('>')
        print('what do you want as your user name?')
        user_name = input('>')
        user_id = first_name[:3] + str(random.randint(0,10) * 73)
        new_user = User(first_name, last_name, user_name, user_id)
        users.append(new_user)
        Writer.save_user(users)
        return new_user

    def get_account(users):
        key = 0
        print('-------------------------')
        for key,i in enumerate(users):
            print(key + 1, i.user_name)
        print('--------------------------')

        get_user = input("> ")
        the_user = [user for user in enumerate(users)
            if (user[0]+1) == int(get_user)][0][1]

        print(the_user.user_name)
        print('----------------------------')
        return the_user
