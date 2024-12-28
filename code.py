import random
name=input("Enter your name:")
print("Welcome ",name," !")
score=0
while True:
    print("Do you want to roll your die?")
    ans=input("y for yes/ n for no:").lower()
    if ans=='y':
        print("Rolling your die...")
        op=random.randint(1,6)
        print(op)
