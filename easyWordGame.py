#Mateo Lanzillotta
#06/11/2021
#Word game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed
# play as long as the user has turns or has guessed the word
import random

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
print(name, end =" ")
answer = input("Do you wanna play").upper()
print("\n ",gameWords)  #delete when code works properly
while "Y" in answer:
    print(name," Good luck")
    word=random.choice(gameWords)
    print(word)
    turns=10 # find better way to create turns
    guesses=' '
    counter=len(word)
    while turns >0 and counter>0:
        for char in word:
            if char in guesses:
                print(char, end='')
            else:
                print('_', end='')
        newGuess=input("\n Give me a letter ")
        if newGuess in word:
            counter -=1
            guesses += newGuess   #guesses= guesses+newGuesses
            print("You are Right!!", )
        else:
            turns -= 1
            print ("Sorry that is wrong, you still have ", turns," turns")
    answer="n"
    print("Goodbye")

