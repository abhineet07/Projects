import Encryption
import os

class Login:
    def __init__(self):
        self.encryption = Encryption.Encryption()

        # stores the current username and password
        self.__currentUsername = ""
        self.__currentPassword = ""

        # stores all the usernames and passwords
        self.__username = []
        self.__password = []

        self.accounts = []
        try:
            credentialsFile = open('Login.txt', 'r')
            self.accounts = credentialsFile.readlines()
            for account in self.accounts:
                uname, pwd = account.strip().split(":")
                # decrypting the username and password stored in Login.txt
                uname = self.encryption.decryptText(uname.encode())
                pwd = self.encryption.decryptText(pwd.encode())
                self.__username.append(uname)
                self.__password.append(pwd)
            credentialsFile.close()

        except:
            print("No accounts present\n")

    def runLogin(self):
        while(True):
            print("\nPress 1 : For Sign In")
            print("Press 2 : For Sign Up")
            print("Press 3 : Quit")

            answer = int(input())

            # Sign In
            if answer == 1:
                self.__currentUsername = str(input("\nEnter the username : "))
                self.__currentPassword = str(input("Enter the password : "))

                if (not self.__username.__contains__(self.__currentUsername)
                        or not self.__username.__contains__(self.__currentPassword)):
                    self.__currentUsername = ""
                    self.__currentPassword = ""
                    print("\nWrong Username or Password")
                    continue

                return True

            # Sign Up
            elif answer == 2:
                # before creating a new account checking whether we reached the accounts limit
                if len(self.accounts) == 10:
                    print("\nMaximum Limit for account reached. Cannot create account")
                    return False

                credentialsFile = open('Login.txt', 'a+')
                print()
                self.__currentUsername = str(input("Enter the username : "))
                self.__currentPassword = str(input("Enter the password : "))
                if self.__username.__contains__(self.__currentUsername):
                    print("Username already exist. Please try again.")
                    continue

                # encrypting the journal data for storing in a file
                data = (self.encryption.encryptText(self.__currentUsername).decode('utf-8') + ":" +
                                               self.encryption.encryptText(self.__currentPassword).decode('utf-8') + "\n")

                credentialsFile.write(data)
                credentialsFile.close()

                return True

            # quit
            elif answer == 3:

                return False

            else:
                print("\nPlease enter a valid choice")
                continue

    def getUsername(self):
        s = self.__currentUsername
        return s

    def getCurrentUserName(self):
        if self.__currentUsername == "":
            return "No User Signed In"
        return self.__currentUsername

    def showAllUsernames(self):
        print(self.__username)
