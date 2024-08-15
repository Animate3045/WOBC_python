#!/usr/bin/python3
import sys
try:
    age = int(sys.argv[1])
#except Exception as new_error:
    #print('This is your error: {new_error}.')
except ValueError as te:
    print (f"You need to provide an integer for an age. This is the python error, ---> 'print({te})' <---")
except IndexError as ie:
    print(f"You need to provide an argument. Here's your error, ---> '{ie}' <---")
else:
    print(f"You are {age} yeaars old. You were born maybe in {2024-age}.")
finally:
    print('We always print this no matter what.')