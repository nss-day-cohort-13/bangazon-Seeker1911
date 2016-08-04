from birdyboard import *

class Allusers:

    def __init__(self):
        self.users = dict()

    def add_account(self, new_account):
        self.users[new_account.user_id] = new_account
