import random
from birdyboard import *
from writer import Writer

class User:

    def __init__(self, first_name, last_name, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.user_id = self.first_name[:3] + str(random.randint(0,10) * 73)

    def new_account():
        print("What's your first name?")
        first_name = input('>')
        print("What's your last name?")
        last_name = input('>')
        print('what do you want as your user name?')
        user_name = input('>')

        new_account = User(first_name, last_name, user_name)
        # Writer.save_user(new_account)
        return new_account
