#!/usr/bin/env python3
#Create function
from time import sleep
def passwordTest():
    pword = str(input('Please enter your desired password: '))
    #the first check is for length. The function is recursive until proper length is achieved.
    while len(pword) <= 13:
        print("Your password is not long enough. Enter at least 14 characters.")
        sleep(3)
        passwordTest()
    #sort the password characters by upper/lower/digit/special
    uCase = []
    lCase = []
    num = []
    special = []
    #sort and check password characters by type using ASCII values
    for i in pword:
        #sort printable special characters
        if 33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
            special.append(i)
        #sort digits
        elif 48 <= ord(i) <= 57:
            num.append(i)
        #sort upper case
        elif i.isupper():
            uCase.append(i)
        #sort lower case
        elif i.islower():
            lCase.append(i)
        #exclude invalid characters, restart function if passed invalid character
        else:
            print('Invalid character entered in password. Try again.')
            sleep(3)
            passwordTest()
   #Check to make sure none of the sorted lists are empty - reprompt for new password if it doesn't meet requirements
    if not uCase:
        print('Password must contain at least one upper case character. Try again.')
        sleep(3)
        passwordTest()
    elif not lCase:
        print('Password must contain at least one lower case character. Try again.')
        sleep(3)
        passwordTest()
    elif not num:
        print('Password must contain at least one number. Try again.')
        sleep(3)
        passwordTest()
    elif not special:
        print('Password must contain at least one special character. Try again.')
        sleep(3)
        passwordTest()
    else:
        print('Password accepted. Please do not forget your password.')
        sleep(5)
        print('Password Test function will now shutdown. Thank you.')
        sleep(5)
        exit()

#set the function to autorun
passwordTest()