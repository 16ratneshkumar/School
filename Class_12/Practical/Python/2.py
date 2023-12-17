# Read A Text File And Display The Number Of Vowels/Consonants/Uppercase/Lowercase Characters In The File.
import time
name=input("Enter Your Name:").capitalize()
print("Hello",name,"\n","Welcome To My Program")
def total_letters(x):
    count0=0
    for i in x:
        count0+=1
    return count0
def count_vowels_consonants(x):
    count=0
    count1=0
    con=0
    for a in x:
        if a.isalpha():
            i=a.lower()
            if a in 'aeiou':
                count+=1
            else:
                count1+=1
        else:
            con+=1
    return count,count1,con
def count_uppercase(x):
    count2=0
    for i in x:
        if i.isupper():
            count2+=1
    return count2
    
def count_lowercase(x):
    count3=0
    for i in x:
        if i.islower():
            count3+=1
    return count3
with open(".\Class_12\Practical\Python\myfile.txt", "r")as file:
    x=file.read()
    d=total_letters(x)
    a,e,q=count_vowels_consonants(x)
    b=count_uppercase(x)
    c=count_lowercase(x)
    print("Wait Few Second.........","\n","Your Work In Progress.......","\n")
    time.sleep(1)
    print("IN THIS FILE TOTAL LETTERS ARE :",d,'\n',"UPPERCASE:",b,"\n","LOWERCASE:",c,"\n","VOWELS:",a,"\n","CONSONANTS:",e,"\n","SPECIAL CHARACTERS:",q)
    print('\n',"Thank You For Coming To My Program")