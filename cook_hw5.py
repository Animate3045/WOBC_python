#!/usr/bin/env python3
import re
import sys

def parser(file):
    li = []
    liPhone = []
#open file and read lines
    with open(file, 'r') as inFile:
        data = inFile.readlines()
        
        #Regex expressions to define matches
        question = re.compile(r'^.+\?$')
        phone = re.compile(r'\(?\d{3}(\)|\-)+\d{3}\-\d{4}$')
        comEmail = re.compile(r'^\b.+\@.+\.com$')
        
        #Identify lines that end with question marks
        for i in data:
            if question.match(i):
                li.append(i.strip())
        print(f'There are {len(li)} lines that end in a question mark.')
        for line in li:
            print(line)
        #identify phone numbers
        for i in data:
            if phone.match(i):
                #remove parens to make common format
                number = i.replace('(','').replace(')','')
                liPhone.append(number)
        for number in liPhone:
            print(number)
        #identify .com email addresses
        for i in data:
            if comEmail.match(i):
                user, domain = i.split('@')
                print(f'{user} uses {domain}')

file = sys.argv[1]
parser(file)