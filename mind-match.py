import random
print ("WELCOME TO GUESS ME PUZZLE")
print("BETWEEN 1 TO 20")
print("Your Probabilty to Win ~ less than 0.1")
def game(num,a):
    l1=a-2
    l2=a-1
    l3=a
    l4=a+1
    l5=a+2
    list=[l1,l2,l3,l4,l5]
    if num==l2 or num==l4:
        print(" Good Try, You Are Too Close")
    elif num==l1 or num==l5:
       print("Nice Try,")
    elif num==l3:
       print("Thats IMPOSSIBLE YOU BEAT ME ")
    else:
         print("Try Again")
tryagain="yes"
while tryagain=="yes":
    start=input("Press S to Start")
    if start=='S'or start=='s':
        num=int(input("Enter Your Guess"))
        a=random.randint(1,20)
        print("My number =", a)
        result=game(num,a)
        b=input("play Again y (Yes)/n (No)")
        if b=="n":
            tryagain="no"
        


