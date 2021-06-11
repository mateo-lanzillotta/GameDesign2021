#Mateo Lanzillotta
#I am very lost
#Code from Maria Suarez
myNumber=[1,2,37,8,9]
myCities=["Dallas", "Austin", "San_Antonio", "Houston"]
myCity=["Dallas"]
myCity=["Austin"]
myCity=["San_Antonio"]
myCity=["Houston"]
print(myCity)
myCity.append("Waco")
for city in myCities:   # for each element in your array get the value
    print(city, end= " , ")
print()
counter=len(myCities)   #len of Array is one more than the last index
#for loop limit your array order
for x in range(0,counter-1):
    print(myCities[x], end= " , ")
print(myCities[counter-1])
myCities[1]="Dallas"
print (myCities[1:3])
if "Dallas" in myCities:
    print("I have arrived in Dallas, TX")
else:
    print ("I want to go to Dallas, TX")
counter=len(myCities)
if "Austin"in myCities:
    print("I have arrived in Austin, TX")
else:
    print("I want to go to Austin, TX")
if "San_Antonio"in myCities:
    print("I have arrived in San_Antonio, TX")
else:
    print("I want to go to San_Antonio, TX")
if "Houston"in myCities:
    print("I have arrived in Houston, TX")
else:
    print("I want to go to Houston, TX")


varChoice=" "
def menu():
    print("*"*28)
    print("*"," "*6,"Cities"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Dallas, Austin, San_Antonio, Houston"," "*4,"*")
    print("*"," "*2,"L2- Dallas, Austin, San_Antonio"," "*5,"*")
    print("*"," "*2,"L3- Dallas, Austin"," "*7,"*")
    print("*"," "*2,"L4- Dallas"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or L4", end= " ")
    varChoice =input()  #local variable
    return varChoice
    
#myCities
arr = ["Dallas, Austin, San_Antonio, Houston"]
print("Array is :", arr)

res = arr[::-1] 
print("Resultant new reversed array: [Houston, San_Antonio, Austin, Dallas",res)