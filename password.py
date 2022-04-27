class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empty user list

    def __init__(self, username, password):

        '''
        __init__ method that enables the definition of properties for the user objects.

        Args:
            username: User's name for login.
            password: User's password to authenticate login.
        '''

        self.username = username
        self.password = password

    pass


class Credentials:
    '''
    Class that generates new instances of credentials.
    '''

    credentials_list =[] #Empty credentials list

    def __init__(self, account_name, account_username, account_password):
        '''
        Args:
            account_name: The name of the account.
            account_password: The password for the corresponding account.
        '''

        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password


    def save_credentials(self):
        '''
        save_credentials method enables the saving of existing account credentials objects into credentials_list.
        '''

        Credentials.credentials_list.append(self)


    def delete_credentials(self):
        '''
        delete_credentials method allows user to delete saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)


    @classmethod
    def find_credentials_by_account_name(cls,account_name):
        '''
        Method that takes in a number and returns a credential that matches that account's_name.

        Args:
            account_name: Account name to search for.

        Returns:
            Credentials of an account tat matches the account_name. 
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials


    @classmethod
    def credentials_exist(cls,account_name):
        '''
        Method checks if a credentials object exists from the credentials_list.

        Args:
            account_name: Account name to search for.

        Returns:
            Boolean: True or false depending if the credential exists.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True


    @classmethod
    def display_credentials(cls):
        '''
        Method returns the entire credentials list
        '''

        return cls.credentials_list

        pass