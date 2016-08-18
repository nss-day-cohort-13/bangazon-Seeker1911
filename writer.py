import time
import pickle

class Writer:
    def save_user(users):
        with open('users.txt', 'wb+') as newFile:
            pickle.dump(users, newFile)

    def save_public_chirp(chirps):
        with open('chirps.txt', 'wb+') as newFile:
            pickle.dump(chirps, newFile)

    def save_private_chirp(chirps):
        with open('private_chirps.txt', 'wb+') as newFile:
            pickle.dump(chirps, newFile)
