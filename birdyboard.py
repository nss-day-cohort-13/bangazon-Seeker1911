import sys
from user import *
from allUsers import *
''' Menu for Birdyboard copyright infringement and IP theft CLI Application.
'''
class Menu:

    def __init__(self):
        self.allusers = Allusers()



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
                user = User.new_account()
                self.allusers.add_account(user)

                print('user ID is: ' + user.user_id + '\n')

            if choice == '2':
                pass

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
