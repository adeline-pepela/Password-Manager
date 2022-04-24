# PasswordManager
This application allows users to manage and generate new passwords when needed.

#### By Adeline Makokha

## Description
PasswordManager enables users to manage passwords for numerous accounts. A user can create a password locker account using their username and password details. Additionally, they can store credentials for existing accounts, create credentials for new accounts, generate passwords for new accounts, and allow users to put their password. Also, users can view the credentials and passwords of their accounts, and delete credentials for accounts that they no longer need.

## Setup/Installation Requirements
* Visual Studio (VS) Code or Atom Editor will be essential.
* One must also clone the github repository.

## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Owiti-Charles/Password-Locker.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x password.py
        $ ./password.py
* To run test for the application
        $ python3 password_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./password.py```|Hello Welcome to your Accounts Password Manager... <br>* cc ---  Create New Account * |
|Select  cc| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>|
|Display all stored credentials | Enter ```dc```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```fc```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```dlc```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```ex```| The application exits|


## Known Bugs
The current application contains no bugs

## Technologies
* Python

## Suport and Contact Details
Email:adelinemakokha@gmail.com



### License
[GNU GPL v3.0](./LICENSE)

Copyright (c) [2022] **Adeline Makokha**
