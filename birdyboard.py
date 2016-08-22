import sys
from user import *
from allUsers import *
from chirp import *
import pickle
''' Menu for Birdyboard copyright infringement and IP theft CLI Application.
'''
users = list()
private_chirps = list()
chirps = list()
class Menu:

    def deserialize_lists(self):
        global users
        with open('users.txt', 'rb+') as f:
            try:
                users = pickle.load(f)
            except:
                users = []

        global private_chirps
        with open('private_chirps.txt', 'rb+') as f:
            try:
                private_chirps = pickle.load(f)
            except:
                private_chirps = []

        global chirps
        with open('chirps.txt', 'rb+') as f:
            try:
                chirps = pickle.load(f)
            except:
                chirps = []

        self.main_menu()

    def main_menu(self):
        global users
        global private_chirps
        global chirps

        while True:
            print('1. New User Account')
            print('2. Select User')
            print('3. View Chirps')
            print('4. Chirp')
            print('5. Send a DM')
            print('6. Exit')
            choice = input('>')

            if choice == '1':
                user = User.new_account(users)

            if choice == '2':
                user = User.get_account(users)

            if choice == '3':
                receiver = user
                view_chirp = Chirp.view_chirp(chirps, private_chirps, user.user_id, users)

            if choice == '4':
                message = input('Type message: ')
                print('')
                Chirp.public_chirp(chirps, message, user.user_id)

            if choice == '5':
                message = input('Type message: ')
                print(' ')
                receiver = User.get_account(users)
                Chirp.private_chirp(private_chirps, message, user.user_id, receiver.user_id)

            if choice == '6':
                break


if __name__ == '__main__':
    menu = Menu()
    menu.deserialize_lists()
