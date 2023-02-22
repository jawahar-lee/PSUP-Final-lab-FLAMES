def getNames():
    while(True):                #running a loop until the user enters name with only alphabets
        global name1
        name1 = input("Enter your name: ")
        name1=name1.replace(" ","")       #ignoring all spaces
        if not(name1.isalpha()):
            print("Name should contain only alphabets!")
        else: break
    while(True):                #running a loop until the user enters name with only alphabets
        global name2
        name2 = input("Enter your crush's name: ")
        name2=name2.replace(" ","")       #ignoring all spaces
        if not(name2.isalpha()):
            print("Name should contain only alphabets!")
        else: break

getNames()                                  #calling the function to get names from the user
name1,name2 = name1.upper(),name2.upper() #converting all upperCase for easy comparison
listOfN1,listOfN2 = list(name1),list(name2) #creating list of each letters

if len(listOfN1)<len(listOfN2):            #filtering the short and long names among them for easy looping afterwards
    shortOfTwo = listOfN1
    longOfTwo = listOfN2
else:
    shortOfTwo = listOfN2
    longOfTwo = listOfN1

commonLetters=0                            #initializing the common letters to zero

for letter in shortOfTwo:                  #counts the number of common letters between the names
    if letter in longOfTwo:
        commonLetters+=1
        longOfTwo.remove(letter)           #removing already matched common letters to avoid repetative confused matching

uncommon = len(name1)+len(name2)-(2*commonLetters)    #counting all the unmatched letters to start executing flames

flames = ["F","L","A","M","E","S"]            

flamesCount=0                                 #initializing a flame count which will increament for every loop in the upcomming while loop

while(len(flames)>1):                         #running a loop till there is only one element left in flames list
    for i in flames:
        flamesCount+=1
        if flamesCount%uncommon==0:
            flames.remove(i)                  #removing the element that gets striked out in flames

result=flames[0]                              #getting the result of last element remaining in the flames list

if result=="F":                                                #printing some output based on the results
    print(name1," and ",name2," can be good friends.")
elif result=="L":
    print("OMG! ",name1," and ",name2," are meant for each other. Pickup some guts and ask him/her for a date.")
elif result=="A":
    print("Hey, ",name1," and ",name2," are affectionate towards each other.")
elif result=="M":
    print(name1," and ",name2,"can have a future together. Talk to him/her about this.")
elif result=="E":
    print("Sorry...the compatability between ",name1," and ",name2," is not so good. But you can give it a try.")
elif result=="S":
    print(name1," and ",name2," are like brother and sister.")
else: print("There is an problem calculating your compatability...Please try again.")