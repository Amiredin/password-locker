class User:
  """
  class that generates new instances of user

  """

  user_detail = [] # Empty contact list 

  def __init__(self,account_name, user_name,password , confirm_password):

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.confirm_password = confirm_password

  def save_detail(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_detail.append(self)