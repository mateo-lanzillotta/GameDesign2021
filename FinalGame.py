#Mateo Lanzillotta
#6/22/2021
#First draft of final project
import math, random, sys, time, os

def replay():
    print("Do you want to play again?")
    level = input()
    level = level.lower()
    if "y" in level:
        return True
    else:
        return False
def menu():
    print("*"*28)
    print("*"," "*6,"Mateo's Game"," "*4,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"Level 1-Easy"," "*8,"*")
    print("*"," "*2,"Level 2-Medium"," "*6,"*")
    print("*"," "*2,"Level 3-Hard"," "*8,"*")
    print("*"," "*2,"Level 4-Scores"," "*6,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")
    print("Enter one of 1,2,3,4, or EX".title(), end = " ")
    varChoice = input()
    varChoice = varChoice.lower()
    print(varChoice)
    return varChoice
def score():
    print("Your scores:")
    print("23,457  Peter")
    print("1,534   Maria")
    print("798    Lucas")
    print("22     Ben")
score()
varChoice = menu()
while varChoice != "":
    if varChoice == "1":
        convert = True
        while convert:
            print("Level 1")
            convert = replay()
    if varChoice == "2":
        convert = True
        while convert:
            print("Level 2")
            convert = replay()
    if varChoice == "3":
        convert = True
        while convert:
            print("Level 3")
            convert = replay()
    if varChoice == "4":
        convert = True
        while convert:
            print("Scores")
            convert = replay()
    varChoice = menu()
print("Goodbye, have a nice day:)".center(100))
