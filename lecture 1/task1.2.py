#!/usr/bin/python3

take_letter = input("please enter a letter : ")

voel = ['a','e','i','o','u']

def check_letter():
    if take_letter.lower().strip() in voel:
        print("letter you entered is voel")
    else :
        print("letter you entered is not voel") 

check_letter()