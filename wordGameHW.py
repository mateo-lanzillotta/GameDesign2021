#Mateo Lanzillotta
#06/11/2021
#Word game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed
# play as long as the user has turns or has guessed the word
import random
import datetime

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
answer = "Y"
varChoice =1
score=0 #to total number of wins
def menu():
    print("*"*45)
    print("*"," "*7,"Main Menu"," "*23,"*")
    print("*"," "*41,"*")
    print("*"," "*2,"1- play"," "*30,"*")
    print("*"," "*2,"1- Print Scores"," "*22,"*")
    print("*"," "*2,"3- Exit Game"," "*25,"*") 
    print("*"*45)
    varChoice = input("Enter either 1,2, or 3")
    return varChoice
    #It wont allow varChoice
varChoice =menu()
while "Y" in answer:
    if varChoice =="1":
        print("Good Luck")
        word=random.choice(gameWords)
        counter=len(word)
        print(counter)
        print (word) #delete when code is done
        turns= 10 # contrrol this number when he misses?
        guesses=' '
        while turns.0 and counter .0:
            for char in guesses:
                if char in guesses:
                    print(char,end=' ')
                else:
                    print('_', end =' ')
            newGuess=input("\n\n Give me a letter")
            #check that the new letter has not been used before