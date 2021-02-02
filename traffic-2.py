#!/usr/bin/env python3

import time

green_green=15
green_amber=5
green=40
amber=10
red=110

while 1:
    j=0
    i=0
    while i < red:
        print("Red for ", i)
        i=i+1
        j=j+1
        time.sleep(1)

    i=0
    while i < amber:
        print("Amber for ", i)
        i=i+1
        j=j+1
        time.sleep(1)

    i=0
    while i < green:
        print("Green for ", i)
        i=i+1
        j=j+1
        time.sleep(1)

    i=0
    while i < green_green:
        print("Green green for ", i)
        i=i+1
        j=j+1
        time.sleep(1)

    i=0
    while i < green_amber:
        print("Green amber for ", i)
        i=i+1
        j=j+1
        time.sleep(1)
    
    print("Total time in loop ", j)

