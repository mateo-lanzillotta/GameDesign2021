#Mateo Lanzillotta
#I am making a code for a game menu
print("**************************")
print("*       My game              *")
print("*         Menu                  *")
print("*                                    *")
print("*    1.- level1                 *")
print("*    2.- level2                 *")
print("*    3.- Print scores        *")
print("*    4.- Exit Game          *")
print("**************************")

answer=int(input())
while answer is not 4:
    if answer==1:
        print("I am in Level 1")
    if answer==2:
        print("I am in Level 2")
    if answer==3:
        print("1- Mateo (100), 2- John(80), 3- Steve(75)")
    if answer==4:           #Ask why this doesn't work
        print("Play again another time!")
    print ("I am here")
    print("**************************")
    print("*       My game          *")
    print("*         Menu           *")
    print("*                        *")
    print("*    1.- level1          *")
    print("*    2.- level2          *")
    print("*    3.- Print scores    *")
    print("*    4.- Exit Game       *")
    print("**************************")
    answer=int(input())


print ("Done")

