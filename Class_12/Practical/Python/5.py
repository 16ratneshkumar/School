# Create A Binary File With Roll Number, Name And Marks. Input A Roll Number And Update The Marks.
import pickle
import time
name=input("Enter Your Name:") .capitalize()
print("Hello",name,"\n","Welcome To My Program")
time.sleep(1)
def make_binaryfile():
    dic={}
    choice='y'
    with open(r".\Class_12\Practical\Python\Marks_file.dat", "ab")as file:
        while choice=='y':
            time.sleep(1)
            roll_no=int(input("Enter Roll No:"))
            name=input("Enter Name:")
            marks=float(input("Enter Your Total Marks:"))
            dic['Roll_no']=roll_no
            dic['Name']=name
            dic['Marks']=marks
            pickle.dump(dic,file)
            print("Your Work Is Done",'\n','Your Data is:',dic)
            choice=input("Do You Want To Access Again(Y/N)...:").lower()
    program_main()
def update_marks():
    dic={}
    Roll_no=int(input("Enter Roll No:"))
    Marks=float(input("Enter Your Total Marks:"))
    print("Wait Few Second.........","\n","Your Work In Progress......")
    time.sleep(1)
    with open(r".\Class_12\Practical\Python\Marks_file.dat", "rb+")as file:
        try:
            while True:
                location=file.tell()
                dic=pickle.load(file)
                if dic['Roll_no']==Roll_no:
                    dic['Marks']=Marks
                    file.seek(location)
                    pickle.dump(dic,file)
        except EOFError:
            print("Your Record Is Updated")
    program_main()
def display_file():
    dic={}
    with open(r".\Class_12\Practical\Python\Marks_file.dat", "rb+")as file:
        try:
            while True:
                dic=pickle.load(file)
                print(dic)
                time.sleep(1)    
        except EOFError:
            #By Ratnesh kumar
            program_main()
def Exit():
    print("Thank You For Coming To My Program")

def program_main():
    print("1.Create File:","\n","2.Update Maks By Roll No:","\n","3.Display File","\n",'4.Exit')
    user_input=input("Enter Your Choice:")
    if user_input=="1":
        make_binaryfile()
    elif user_input=="2":
        update_marks()
    elif user_input=="3":
        display_file()
    elif user_input=="4":
        Exit()
    else:
        print("Wrong Input!")
        program_main()
program_main()
