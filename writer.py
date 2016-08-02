from birdyboard import *
from account import *

class Writer:
    def save_user(new_account):
        with open('users.txt', 'a+') as newFile:
            newFile.write('*** ' + new_account.first_name + ' ' + new_account.last_name + ' ***\n')
            newFile.write('user name: ' + new_account.user_name + '\n')
            newFile.write('user ID: ' + new_account.user_id + '\n')
