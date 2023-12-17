# Read A Text File Line By Line And Display Each Word Separated By A #.
import time
name=input("Enter Your Name:") .capitalize()
print("Hello",name,"\n","Welcome To My Program",'\n',"Wait Few Second.........","\n","Your Work In Progress......")
time.sleep(1)
def Readfile():
    with open(r".\Class_12\Practical\Python\myfile.txt", "r")as file:
        x=' '
        while x:
            x=file.readline()
            for i in x:
                if i==" ":
                    a = i.replace(" ", "#")
                    print(a,end="")
                else:
                    print(i,end="")
    print('\n',"Thank You For Coming To My Program")
Readfile()

