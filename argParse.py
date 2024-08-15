#!/usr/bin/python3

#pip install argparse
#pip3 install argparse

import argparse

house = argparse.ArgumentParser()

house.add_argument("address", metavar='ADDRESS', help = 'this is the address we want to check the status on.')

#optional argument
house.add_argument('--damage','-d-', metavar='DAMAGE', help='This is the type of damage you have')

args = house.parse_args()

if args.damage is not None:
    print(f'you have some {args.damage} damage')