# Create A CSV File By Entering User-Id And Password, Read And Search The Password For Given User - Id
import csv
import time
name=input("Enter Your Name:") .capitalize()
print("Hello",name,"\n","Welcome To My Program")
def create_csv_file():
    lst=[]
    choice="y"
    with open(r".\Class_12\Practical\Python\Id_password.txt", "a",newline="")as file:
        x=csv.writer(file)
        while choice=="y":
            time.sleep(1)
            user_id=input("Enter Your User_Id:")
            password=input("Enter Your Password:")
            lst=[user_id,password]
            x.writerow(lst)
            choice=input("Do You Want To Access Again(Y/N)...:").lower()
    program_main()
def find_id_password():
    choice="y"
    with open(r".\Class_12\Practical\Python\Id_password.txt", "r",)as file:
        y=dict(csv.reader(file))
        while choice=="y":
            user_id=input("Enter Your User_Id:")
            print("Wait Few Second.........","\n","Your Work In Progress......")
            time.sleep(1)
            if user_id in y:
                a=y.get(user_id)
                print("Your Password Is :",a)
            else:
                print("Not Found")
            choice=input("Do You Want To Access Again(Y/N).....:").lower()
    program_main()
def Exit():
    print("Thank You For Coming To My Program")
def program_main():
    print("1.Save Id Password:","\n","2.Find Password:","\n",'3.Exit')
    user_input=input("Enter Your Choice:")
    if user_input=="1":
        create_csv_file()
    elif user_input=="2":
        find_id_password()
    elif user_input=="3":
        Exit()
    else:
        print("Wrong Input!")
        program_main()
program_main()