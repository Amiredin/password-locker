import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("facebook", "amiredin" ,"123456", "123456") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account_name,"facebook")
        self.assertEqual(self.new_user.user_name,"amiredin")
        self.assertEqual(self.new_user.password,"123456")
        self.assertEqual(self.new_user.confirm_password,"123456")



    