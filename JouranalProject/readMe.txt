This project has 3 python files
 - Encryption.py
 - Login.py
 - Journal.py
 
1) Encryption.py
		Here we defined a method, to encrypt the text data for writing in the file, so that if someone opens the file he/she will not understand the data.
		Another method to decrypt the same text written in the files.

2) Login.py
		It gives user 3 choices:
			1) to Sign In, by pressing key "1"
				and then vaidates that the login credentials by checking from the "Login.txt" are correct or not, and keep track of this user
			2) to Sign Up, by pressing key "2"
				and then check whether the limit of 10 accounts reached, if not only then you can create an account.
				It will store the encrypted credentials in "Login.txt" and keep track of current new user.
				
			3) to exit, by pressing "3"
			
			if any other key is pressed then, it will say wrong choice and asks the same three choices again.
			
3) Journal.py
		-The project start from this file.
		-First it calls the Login.py for user to get login and create journal
		-Then it gives choice to the current logged in user
			1) Show all journals, by pressing "1"
				it reads the encrypted data from the file with the current username's name
				and then decrypts the file data and show only the latest 50 journals of the current user
			2) Create a new journal, by pressing "2"
				it prompts the user to enter the data for the journal. After that a timestam is added to the data.
				and then the data is encrypted and stored in the file with the name of current user
			3) exit, by pressing "3"
			
			this will keep giving the same 3 choices until you press "3"
			
######################################################################################################################################################################
			
Requirements:
	Packages : 1) cryptography
				to install this package : pip install cryptography
			   2) datetime	
				
######################################################################################################################################################################

Sample Output:

Press 1 : For Sign In
Press 2 : For Sign Up
Press 3 : Quit
2

Enter the username : tim
Enter the password : tim

Press 1 : For showing all entries
Press 2 : For Creating a new entry
Press 3 : For exit
2

Enter text for journal : this is my fisrt entry

Press 1 : For showing all entries
Press 2 : For Creating a new entry
Press 3 : For exit
2

Enter text for journal : this is my seconf entry

Press 1 : For showing all entries
Press 2 : For Creating a new entry
Press 3 : For exit
1

Showing latest 50 entries : 
13 January 2020 10.41PM - this is my seconf entry
13 January 2020 10.41PM - this is my fisrt entry

Press 1 : For showing all entries
Press 2 : For Creating a new entry
Press 3 : For exit
3

Process finished with exit code 0
