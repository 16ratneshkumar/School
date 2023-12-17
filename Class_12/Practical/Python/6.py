# Write A Random Number Generator That Generatesrandom Numbers Between 1 And 6 (Simulates A Dice).
import random
import time
name=input("Enter Your Name:").capitalize()
print("Hello",name,"\n","Welcome To My Program")
def make_dice():
    choice="y"
    while choice=='y':
        print("Your Dice Is Rolling.....",'\n',"Please Wait A Few Second")
        time.sleep(1)
        dice=random.randint(1,6)
        print("Your Dice Show:",dice)
        choice=input("Do You Access Again(Y/N):").lower()
    print("Thank You For Coming To My Program")
make_dice()