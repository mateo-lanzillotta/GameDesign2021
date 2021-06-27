#Mateo Lanzillotta
#6/22/2021
#Final draft of final project
#Historical Quiz game
#INSTRUCTIONS:
#This game has 3 levels, each getting harder and containing 3 questions.
#20 points are given for a correct answer, and 20 taken for an incorrect one.
#At the end, you may see your score as compared to others.
#Jadon helped me with the scoreboard
import random, sys, time, os, datetime
score = 0
#Return to menu
def replay():
    print("Do you want to return to menu?")
    level = input()
    level = level.lower()
    if "y" in level:
        return False
    else:
        return True
#update score
def updateScore(score):
    FileWrite=open("scoresheet.txt",'a') 
    line=str(score)+ name 
    FileWrite.write("\n"+line)
    FileWrite.close() 
#print score
def printScore(): #function to read the scoreboard file
    TOP=[] #list of highest scores
    page = open("scoresheet.txt") #opens text files
    rs = page.readlines() 
    sortedscore = sorted(rs, reverse= True) #sort scores from highes to lowest
    for line in range(6):
        mateo =(str(sortedscore[line])) #gets the scores that are in top 7
        TOP.append(mateo) # puts them into the list
    page.close()
    for i in range(5):
        print(TOP[i])

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
    print("Enter one of 0,1,2,3,4, or ex".title(), end = " ")
    varChoice = input()
    varChoice = varChoice.lower()
    print(varChoice)
    return varChoice
print("Welcome to Mateo's Historical Quiz!")

#Scoreboard
def totalScore(score, var):
    score += var
    #print("Your scores:")
    #How do I get my scores to update on this

#More variables
name = input("what is your name")
os.system('cls')
varChoice = menu()
wordList = ["fun", "enjoyable", "great", "easily playable"]

#Setting up what happens if you press 0
while varChoice != "ex":
    if varChoice =="0":
        print ("Mateo's game is...")
        for i in range(0,4):
            print (wordList[i])
        print("Type in any level, and get ready for a historical mind-reckoning!")


#Setting up what happens if you press 1
    if varChoice == "1":
        convert = True
        while convert:
            print("Level 1")
            print("Here is your question:")
            var = str(input("What year was the United States founded in?"))
            if var == "1776":
                print("You are correct!")
                print("You get 20 points")
                score +=1
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score-=1
            var2 = str(input("What was Ghandi's first name?"))
            if var2 == "mahatma":
                print("You are correct!")
                print("You get 20 points")
                score+=1
                
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score-=1
            var3 = str(input("How many states are in the U.S?"))
            if var3 == "50":
                print("You are correct!")
                print("You get 20 points")
                score+=1
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score-=1
            convert = replay()


#Setting up what happens if you press 2
    if varChoice == "2":
        convert = True
        while convert:
            print("Level 2")
            print("Here is your question:")
            var = str(input("Who was the 8th president of the U.S?")).lower()
            if var == "martin van buren":  #make all lowercase
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            var2 = str(input("What country did the colonies break free from to become the U.S?"))
            if var2 == "england":
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            var3 = str(input("What was the first name of America's first black president?"))
            if var3 == "barack":
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            convert = replay()


#Setting up what happens if you press 3
    if varChoice == "3":
        convert = True
        while convert:
            print("Level 3")
            print("Here is your question:")
            var = str(input("How many countries are in Central America?"))
            if var == "8" or "eight":
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            var2 = str(input("Who won the first World Cup?"))
            if var2 == "uruguay":
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            var3 = str(input("What year did WWI start in?"))
            if var3 == "1914":
                print("You are correct!")
                print("You get 20 points")
                score += 20
            else:
                print("Try again later:(")
                print("You lose 20 points")
                score -= 20
            convert = replay()
    updateScore(score)

#Setting up what happens if you press 4
    if varChoice == "4":
        #update the file scores
        convert = True
        while convert:
            printScore()
            convert = replay()
    varChoice = menu()


#Exit game
print("Goodbye, have a nice day:)")