import unittest
from user import *


class TestChirps(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_reply_public_chirp_creation(self):
    pass


  def test_new_public_chirp_creation(self):
    origin = User("John", "Deer", "Joh317")
    chirp = Chirp(message="Hello", user=origin.user_id, private=False)

    self.assertEqual(chirp.message, "Hi everyone")
    self.assertEqual(chirp.user_id, origin.user_id)
    self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)


  def test_private_chirp_creation(self):
    origin = User("John", "Deer", "Joh317")
    target = User("No", "Body", "No426")
    chirp = Chirp(message="I has all your bases", user=origin.user_id, private=True,
                  receiver=target.user_id)

    self.assertIsInstance(chirp, Chirp)




if __name__ == '__main__':
    unittest.main()
