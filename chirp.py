import random
import time
from writer import *
from birdyboard import *
from user import *
import pickle

class Chirp:

    def __init__(self, message, sender, receiver=None, private=False):
        self.sender = sender
        self.receiver = receiver
        self.private = private
        self.message = message
        self.chirp_id = str(random.randint(0,200)*1000)
        # self.timestamp = time.time()



    def public_chirp(chirps, message, sender):
        chirp = Chirp(message, sender)
        chirps.append(chirp)
        Writer.save_public_chirp(chirps)

    def private_chirp(chirps, message, sender, receiver, private=True):
        chirp = Chirp(message, sender, receiver, private)
        chirps.append(chirp)
        Writer.save_private_chirp(chirps)
        # print(message)

    def view_chirp(chirps, private_chirps, sender):
        key = 0
        print('Private chirps..........')
        for key,i in enumerate(private_chirps):
            if i.sender == sender or i.receiver == sender:
                print(str(key + 1) + '. From ' + i.sender + ' to '
                      + i.receiver + ': ', i.message)
        print('--------------------------')
        print('Public chirps.........')
        for key,i in enumerate(chirps):
            print(str(key+1) + '. ' + i.sender + '', i.message)
        print('------------------------')

        # get_user = input("> ")
        # the_user = [user for user in enumerate(users)
        #     if (user[0]+1) == int(get_user)][0][1]
        #
        # print(the_user.user_name)
        # print('----------------------------')
        # return the_user
