def getNames():
    while(True):                #running a loop until the user enters name with only alphabets
        global name1
        name1 = input("Enter your name: ")
        name1=name1.replace(" ","")
        if not(name1.isalpha()):
            print("Name should contain only alphabets!")
        else: break
    while(True):                #running a loop until the user enters name with only alphabets
        global name2
        name2 = input("Enter your crush's name: ")
        name2=name2.replace(" ","")
        if not(name2.isalpha()):
            print("Name should contain only alphabets!")
        else: break

getNames()
name1,name2 = name1.upper(),name2.upper() #converting all upper for easy comparison
listOfN1,listOfN2 = list(name1),list(name2) #creating list of each letters

if len(listOfN1)<len(listOfN2):
    shortOfTwo = listOfN1
    longOfTwo = listOfN2
else:
    shortOfTwo = listOfN2
    longOfTwo = listOfN1

commonLetters=0

for letter in shortOfTwo:
    if letter in longOfTwo:
        commonLetters+=1
        longOfTwo.remove(letter)

uncommon = len(name1)+len(name2)-(2*commonLetters)

flames = ["F","L","A","M","E","S"]

flamesCount=0

while(len(flames)>1):
    for i in flames:
        flamesCount+=1
        if flamesCount%uncommon==0:
            flames.remove(i)

result=flames[0]

if result=="F":
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