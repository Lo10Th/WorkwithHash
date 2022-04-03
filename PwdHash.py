import hashlib
from time import sleep
pwd = input("Which password would you like to choose? Enter here:   ")
pwdhash = hashlib.md5(pwd.encode('utf-8')).hexdigest()
sleep(2)
pwdrequest = input("What is your password?  Enter here:   ")
pwdrequesthash = hashlib.md5(pwdrequest.encode('utf-8')).hexdigest()
if pwdrequesthash == pwdhash:
    print("Login successful!")
else:
    print("Wrong password")