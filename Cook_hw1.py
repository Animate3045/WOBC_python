#!/usr/bin/env python3
# Collect the user's age, first name, and last name & assign as variables
from datetime import datetime
age = int(input("Please enter your age: "))
fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")

#Get current datetime, convert age input to int, calculate birthyear, and report back to user
currentDatetime = datetime.now()
birthyear = currentDatetime.year - age
print(f'The user\'s birth year is {birthyear}')

#Generate and print usernames
uName1 = fName + "." + lName
uName2 = fName + "." + lName[0]
uName3 = fName[0] + "." + lName
print(f'Possible usernames: {uName1}, {uName2}, {uName3}')

#Calculate and print possible HS grad years
grad1 = birthyear + 18
grad2 = birthyear + 19
print(f'You graduated high school in {grad1} or {grad2}')

#Generate and print possible email addresses
emailDomain = "@gmail.com"
print(f'Your possible email addresses are {uName1+emailDomain} or {uName2+emailDomain} or {uName3+emailDomain}')

#Calculate and print percentage of life expectancy elapsed
expectedLife = 73.4
percentage = age / expectedLife * 100
print(f'You\'ve lived {percentage: .2f} of your life')