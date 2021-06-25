#Mateo Lanzillotta
#6/22/2021
#First draft of final project
#Historical Quiz game

import math, random, sys, time, os

#Return to menu
def replay():
    print("Do you want to return to menu?")
    level = input()
    level = level.lower()
    if "y" in level:
        return False
    else:
        return True

#Menu creation
def menu():
    print("*"*28)
    print("*"," "*1,"Mateo's History Quiz"," "*1,"*")
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
print("Welcome to Mateo's Historical Quiz!")

#Scoreboard
def totalScore(var):
    score = 0
    score += var
    print("Your scores:")
    #How do I get my scores to update on this

#Printing levels
varChoice = menu()
while varChoice != "ex":
    if varChoice == "1":
        convert = True
        while convert:
            print("Level 1")
            print("Here is your question:")
            var = str(input("What year was the United States founded in?"))
            if var == "1776":
                print("You are correct!")
                print("You get 20 points")
                totalScore(20)
            else:
                print("Try again later:(")
                print("You lose 20 points")
                totalScore(-20)
            convert = replay()
    if varChoice == "2":
        convert = True
        while convert:
            print("Level 2")
            print("Here is your question:")
            var = str(input("Who was the 8th president of the U.S?"))
            if var == "Martin Van Buren":
                print("You are correct!")
                print("You get 20 points")
                totalScore(20)
            if var =="martin van buren":
                print("You get 10 points")
                totalScore(10)
            else:
                print("Try again later:(")
                print("You lose 20 points")
                totalScore(-20)
            convert = replay()
    if varChoice == "3":
        convert = True
        while convert:
            print("Level 3")
            print("Here is your question:")
            var = str(input("How many countries are in Central America?"))
            if var == "8" or "eight":
                print("You are correct!")
                print("You get 20 points")
                totalScore(20)
            else:
                print("Try again later:(")
                print("You lose 20 points")
                totalScore(-20)
            convert = replay()
    if varChoice == "4":
        #update the file scores
        convert = True
        while convert:
            print("Your final score is:")
            convert = replay()
    varChoice = menu()
print("Goodbye, have a nice day:)".center(100))





