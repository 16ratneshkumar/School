# Write A Python Program To Implement A Stack Using List.
import time
name=input("Enter Your Name:")
print("Hello",name,"\n","Welcome To My Program")
def push(lst):
    num=int(input("enter a number:"))
    lst.append(num)
    program_main(lst)
    return lst
def pop(lst):
    if lst==[]:
        print("underflow")
        program_main(lst)
    else:
        print('Your deleted element is:',lst.pop())
        program_main(lst)
def peek(lst):
    if lst==[]:
        print("underflow")
        program_main(lst)
    else:
        print('Your Top Most Element Is:',lst[len(lst)-1])
        program_main(lst)
def display_stack(lst):
    if lst==[]:
        print("empty stack")
        program_main(lst)
    else:
        print('Your Top Most Element Is->',lst[len(lst)-1])
        for i in range(len(lst)-2,-1,-1):
            print('Your Other Element Is:',lst[i])
        program_main(lst)
def Exit():
    print("Thank You For Using My Program")
def program_main(lst):
    print("1.push:","\n","2.pop:",'\n','3.peek:','\n',
"4.display_stack:",'\n','5.Exit:')
    user_input=input("enter your choice:")
    if user_input=="1":
        push(lst)
    elif user_input=="2":
        pop(lst)
    elif user_input=="3":
        peek(lst)
    elif user_input=="4":
        display_stack(lst)
    elif user_input=="5":
        Exit()
    else:
        print("wrong input!")
        user=input("do you access again(y/n):").lower()
        while user=="y":
            program_main(lst)
lst=[]
program_main(lst)