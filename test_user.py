import unittest
from user import *


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    user = User("John", "Deer", "Tracktor")
    self.assertEqual("John", user.first_name)
    self.assertEqual("Deer", user.last_name)
    self.assertEqual("Tracktor", user.user_name)
    self.assertIsNotNone(user.user_id)
    self.assertIsInstance(user, User)



if __name__ == '__main__':
    unittest.main()
