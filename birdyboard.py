import sys
from account import *
''' Menu for Birdyboard copyright infringement and IP theft CLI Application.
'''
class Menu:

    def __init__(self):
        pass



    def main_menu(self):
        while True:
            print('1. New User Account')
            print('2. Select User')
            print('3. View Chirps')
            print('4. Public Chirp')
            print('5. Private Chirp')
            print('6. Exit')
            choice = input('>')

            if choice == '1':
                user = Account.new_account()
                print('user ID is: ' + user.user_id + '\n')

            if choice == '2':
                user = user()

            if choice == '3':
                view_chirp = view_chirp()

            if choice == '4':
                public_chirp = public_chirp()

            if choice == '5':
                private_chirp = private_chirp()

            if choice == '6':
                break


if __name__ == '__main__':
    menu = Menu()
    menu.main_menu()
