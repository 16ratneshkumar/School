# Create A Binary File With Name And Roll Number. Search For A Given Roll Number And Display The Name, If Not Found Display Appropriate Message.
import pickle
import time
name=input("Enter Your Name:").capitalize()
print("Hello",name,"\n","Welcome To My Program")
def make_binaryfile():
    dict={}
    choice='y'
    with open(r".\Class_12\Practical\Python\Name_file.dat", "ab")as file:
        while choice=='y':
            roll_no=int(input("Enter Roll No:"))
            name=input("Enter Name:")
            dict['Roll_no']=roll_no
            dict['Name']=name
            pickle.dump(dict,file)
            choice=input("Do You Access Again(Y/N)……….").lower()
    program_main()
def find_rollno():
    dict={}
    flag=False
    Roll_no=int(input("Enter Roll No For Find:"))
    with open(r".\Class_12\Practical\Python\Name_file.dat", "rb")as file:
        try:
            while True:
                dict=pickle.load(file)
                if dict['Roll_no']==Roll_no:
                    flag=True
                    break
        except EOFError:
            pass
        if flag==True:
            print("Your Record Is Found")
            time.sleep(1)
            print(dict)
        else:
            print("Your Record Doesn't In File")
        program_main()
def Exit():
    print("Thank You For Coming To My Program")
def program_main():
    print("1.Create File:","\n","2.Find Roll_No:","\n",'3.Exit')
    user_input=input("Enter Your Choice:")
    if user_input=="1":
        make_binaryfile()
    elif user_input=="2":
        find_rollno()
    elif user_input=="3":
        Exit()
    else:
        print("Wrong Input!")
        program_main()
program_main()
