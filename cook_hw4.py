#!/usr/bin/env python3

#import the regex library
import re
#import Counter from collections
from collections import Counter
#import sys module to pass command line argument for file
import sys

def analyze(file):
    with open(file, 'r') as inFile:
        text = inFile.read()
        
        #separate letters
        letters = [char for char in text if char.isalpha()]
        #Counter() generates ordered dict from letters with count as the value
        total = Counter(letters)
        #use the .most_common() function to pull out the most frequent letter & count of that letter
        mostFreq = total.most_common(1)[0][0]
        mostFreqCount = total.most_common(1)[0][1]
        print(f'{mostFreq} is the most common letter. It occurs {mostFreqCount} times.')
        
        #count total words using regex based on whitespace
        wordMatch = re.compile(r'\b[\w+\'-]+\b')
        #Turn text to lower case while matching so all of "the"s are the same
        wordsFound = wordMatch.findall(text.lower())
        #get total for percentage calculation
        totalWords = len(wordsFound)
        #count the number of 'the' occurances
        theCount = wordsFound.count('the')
        thePercent = (theCount / totalWords) * 100
        print(f'\'The\' is {theCount} out of {totalWords} or {thePercent: .2f}% of words ')
        #print(Counter(wordsFound))
        
        #Print 10 lines to a new file
        words = wordMatch.findall(text)
        firstTen = words[0:10]
        with open('ten_words.txt', 'w') as outFile:
            outFile.write(' '.join(firstTen))

file = sys.argv[1]
analyze(file)