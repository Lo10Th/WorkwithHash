import hashlib
from time import sleep
#Here we ask for the password which the computer should hash
pwd = input("Which password would you like to choose? Enter here:   ")
#The entered is hashed and saved as variable 'pwdhash'.
pwdhash = hashlib.md5(pwd.encode('utf-8')).hexdigest()
sleep(2)
#We ask the user for his own password from before
pwdrequest = input("What is your password?  Enter here:   ")
#The requested password is hashed and then compared with the correct password
pwdrequesthash = hashlib.md5(pwdrequest.encode('utf-8')).hexdigest()
if pwdrequesthash == pwdhash:
    print("Login successful!")
else:
    print("Wrong password")
