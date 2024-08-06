#!usr/bin/env python3
import re
addr = (
'192.168.254.1',
'867.53.0.9',
'192.168.254.1',
'255.255.255.257',
'10.10.100.1',
'172.16.0.1',
'192.168.254.1',
'10.10.100.2',
'8.8.8.8',
'1337.4150.4444.07'
)
#Generate a set to de-dup
s = set(addr)

#Open an empty dictionary to store count
newDict = {}

#for each unique address in the set, count number of occurances in the original tuple
#add the unique address and the count of said address as a k/v pair to the dictionary
for i in s:
    x = addr.count(i)
    newDict[i] = x
print(newDict)

#Open empty list for matched IPs
goodIP = []

#for loop to check each element of the tuple
for i in addr:
    #filer for valid IPs - uses a series of "OR" tests to make sure each octet is in [0:255]
    validIP = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    matchObject = validIP.search(i)
    #Add matched IPs to the list
    if matchObject:
        goodIP.append(matchObject.group())
#Print list of valid IPs - will be in order of apperance due to iteration
print(goodIP)
#use a set to isolate unique IPs
print(set(goodIP))
#sort the set
print(sorted(set(goodIP)))