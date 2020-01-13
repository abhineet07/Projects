import Login
import Encryption
from datetime import datetime

class Journal:
    def __init__(self):
        self.login = Login.Login()
        self.encryption = Encryption.Encryption()

    def start(self):

        isLoggedIn = self.login.runLogin()

        if not isLoggedIn:
            print("You are out of portal\n")
            quit()

        self.username = self.login.getUsername()

        while True:
            print("\nPress 1 : For showing all entries")
            print("Press 2 : For Creating a new entry")
            print("Press 3 : For exit")

            answer = int(input())

            # show all entries
            if answer == 1:
                fileName = (self.username) + ".txt"
                file = open(fileName, 'r')
                lines = file.readlines()
                limit = 50
                print("\nShowing latest 50 entries : ")
                for i in range(len(lines)-1, max(len(lines)-51, -1), -1):
                    data = lines[i].strip()
                    data = self.encryption.decryptText(data.encode())
                    print(data)
                file.close()

            # create a new entry
            elif answer == 2:
                fileName = (self.username) + ".txt"
                file = open(fileName, 'a')
                enterText = str(input("\nEnter text for journal : "))
                now = datetime.now()
                timestamp = now.strftime("%d %B %Y %I.%M%p")
                data = timestamp + " - " + enterText
                data = (self.encryption.encryptText(data)).decode('utf-8') + "\n"
                file.write(data)
                file.close()

            # exit
            else:
                break


ob = Journal()
ob.start()
