#!/usr/bin/env python3.8
from password import User
from password import Credentials

#Create an account
def create_user(username,password):
    '''
    Function to create a new user account.
    '''

    new_user = User(username,password)
    return new_user


#Create a new credential
def create_credentials(aname,ausername,apassword):
    '''
    Function to create a new credential.
    '''

    new_credentials = Credentials(aname,ausername,apassword)
    return new_credentials


#Save credentials
def save_credentials(credentials):
    '''
    Function to save credentials.
    '''

    credentials.save_credentials()


#Delete credentials
def delete_credentials(credentials):
    '''
    Function to delete credentials.
    '''

    credentials.delete_credentials()


#Finding credentials
def find_credential(aname):
    '''
    Function that helps users to find a credential by name and return the credentials.
    '''

    return Credentials.find_credentials_by_account_name(aname)


#Checking if credentials exist
def check_existing_credentials(aname):
    '''
    Function that allows users to check if credentials exist with the account name and return a Boolean.
    '''
    return Credentials.credentials_exist(aname)


#Displaying all credentials
def display_credentials():
    '''
    Function that returns all the saved credentials.
    '''
    return Credentials.display_credentials()

#Function to call the other functions
def main():
    print("Hello, Welcome to your Password Manager. Kindly input your username and password")
    username = input()

    print(f"Hello {username}. What would you like to do?")
    print('/n')

    while True:
        print("Use these short codes: cc - create new credentials, dc - display credentials, dlc - delete existing credentials, fc - find credentials, ex -exit the credentials list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*20)

            print("Account name .......")
            a_name = input()

            print("Account Username .....")
            a_username = input()

            print("Account Password .....")
            a_password = input()


            save_credentials(create_credentials(a_name, a_username, a_password)) #Create and save new credentials
            print('/n')
            print(f"New Credential {a_name} {a_username} {a_password} created")
            print('/n')


        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('/n')

                for credentials in display_credentials():
                    print(f"{credentials.account_name} {credentials.account_username} {credentials.account_password}")
                    print('/n')

            else:

                print('/n')
                print("Password Manager does not contain any saved credentials")
                print('/n')

        elif short_code == 'fc':
            print("Enter the account name you want to search for")

            search_account_name = input()
            if check_existing_credentials(search_account_name):
                search_credentials = find_credential(search_account_name)
                print(f"{search_credentials.account_name}")
                print('-'*20)

                print(f"Account Username ....... {search_credentials.account_username}")
                print(f"Account Password ....... {search_credentials.account_password}")

            else:
                print("Those credentials don't exist")


        elif short_code == 'dlc':
            print("Enter the account name you want to delete")

            search_account_name = input()
            if check_existing_credentials(search_account_name):
                search_credentials = find_credential(search_account_name)
                delete_credentials(search_credentials)
                print(f"The credentials for {search_credentials.account_name} has been deleted!")

            else:
                print("The credential with that account name does not exist")


        elif short_code == 'ex':
            print("Thanks for choosing PasswordManager!")
            break

        else: 
            print("PasswordManager really did not get that. Please use the short codes")


if __name__ == '__main__':
    main()