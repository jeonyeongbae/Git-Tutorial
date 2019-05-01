#!/usr/bin/env python3

import random

def good():
    print("I had a good year.")

def bad():
    print("I had a good year.")

def main():
    '''program entry point
    '''
    
    lifespan = 80
    age = 1
    good_year_count = 0


    while age <= lifespan:
        print("I'm {age} year(s) old.".format(age = age))

        goodyear = random.choice([True, False])

        if goodyear:
            good_year_count += 1
            print("I had a good year.")
        else:
            print("I had a bad yera.")

        age += 1
    
    print("I'm dying. I had {} good years in my entire life.".format(good_year_count))

    bad_year_count = lifespan - good_year_count

    if bad_year_count == good_year_count:
        print("My life was boring.")
    elif bad_year_count < good_year_count:
        print("My life was good.")
    else:
        print("My life was bad.")

if __name__ == '__main__':main()

