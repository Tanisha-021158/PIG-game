import random
name=input("Enter your name:")
print("Welcome",name,"!")
lives=3
score=0
while lives>0:
    print("Do you want to roll your die?")
    ans=input("y for yes/ n for no:").lower()
    if ans=='y':
        print("Rolling your die...")
        op=random.randint(1,6)
        print("You got:",op)
        if op==1:
            print("You lose! Your score becomes zero")
            score=0
            lives-=1
            print("You have",lives,"lives left!")
        else:
            score=score+op
            print("Your score:",score)
    elif ans=='n':
        print("Your score:",score)
        break
    else:
        print("Wrong choice")
print("Thank you!")
