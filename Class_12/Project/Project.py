#IMPORT MODULE
import time
import pickle
import mysql.connector as sql
import random
from PIL import Image,ImageDraw,ImageFont
import qrcode

#EXIT
def Exit():
    print("THANK YOU FOR USING MY PROJECT")
    print("1.Sign Up",'\n',"2.Sign In/Login")
    while True:
        wish=int(input("Enter You Choice::"))
        if wish==1:
            sign_up()
        elif wish==2:
            sign_in()
            break
        else :
            print ('Invalid Input!,Enter Again.')
            continue

#START
def Start():
    while True:
        print("1.Sign Up",'\n',"2.Sign In/Login",'\n','3.Forgot Password')
        wish=int(input("Enter You Choice::"))
        if wish==1:
            sign_up()
        elif wish==2:
            sign_in()
            break
        elif wish==3:
            forgot_password()
        else :
            print ('Invalid Input!,Enter Again.')
            continue

#MAIN MENU
def main_menu():
    print("YOU ARE WELCOME IN MY PROJECT.")
    print("What Do You Want??",'\n',"1.Create Health Card",'\n','2.Update Card','\n',"3.Diseases Related Work",'\n',"4.Download Card",'\n',"5.Logout")
    while True:
        Wish=int(input("Enter Your Choice::"))
        if Wish==1:
            print('Wait Few Second.....','\n','Your Work In Process...')
            time.sleep(1)
            add_citizen_data ()
            break
        elif Wish==2:
            print('Wait Few Second.....','\n','Your Data In Loading...')
            time.sleep(1)
            update()
            break
        elif Wish==3:
            print('Wait Few Second.....','\n','Your Work In Process...')
            time.sleep(1)
            diseases()
            break
        elif Wish==4:
            print('Wait Few Second.....','\n','Your Work In Process...')
            time.sleep(1)
            DisplayCard()
            break
        elif Wish==5:
            print('Wait Few Second.....','\n','For Logout Your Account ...')
            break
            time.sleep(1)
            Exit()
        else:
            print('Invalid Input!,Enter Again.')
            continue
            
#SIGN UP
def sign_up():
    with open("C:\\PROJECT\\user_id_password.txt",'ab+') as baghat:
        phoneno=False
        passw=False
        name=input('Enter Your Full Name::')
        father_name=input("Enter Your Father's Name::")
        print('YOUR EMAIL ID IS YOUR USER ID')
        user_id=VerifyEmail()
        S_Question=input('Enter Your Memorable Monuments::')
        phone_no=VerifyPhoneNo()
        password=input('Enter Your Password::')
        confirm_password=input('Confirm Your Password::')
        while passw!=True:
            if password!=confirm_password:
                print('Invalid Input!,Enter Again.')
                password=input('Enter Your Password::')
                confirm_password=input('Confirm Your Password::')
                continue
            if password==confirm_password:
                passw=True
                break
        dic={}
        dic['Name']=name
        dic['father_name']=father_name
        dic['Phone_no']=phone_no
        dic['Email_id']=user_id
        dic['password']=password
        dic['Question']=S_Question
        pickle.dump(dic,baghat)


#SIGN IN/LOGIN
def sign_in():
    dict={}
    flag=False
    Email_id=input('Enter Your Email Id::')
    password=input('Enter Your Password::')
    with open("C:\\PROJECT\\user_id_password.txt",'rb+') as baghat:
        try:
                while True:
                    dict=pickle.load(baghat)
                    while dict['Email_id']==Email_id:
                        if dict['password']==password:
                            flag=True
                            print('Wait Few Second.....','\n','Login.......')
                            time.sleep(1)
                            main_menu()
                            break
                        else:
                            print('Your Password Is Incorrect Enter Your Choice.')
                            print('1.Try Again(Enter Password)','\n','2.Forgot Password')
                            choice=input('Enter You Choice::')
                            if choice=='1':
                                password=input('Enter Again Your Password::')
                                continue
                            elif choice =='2':
                                forgot_password()
                            else:
                                print('Invalid Input,Enter Again.')
                                continue
        except EOFError:
            if flag==False:
                print('Your Are Not Register User Please Register Your Self.')
                Start()

#FORGOT PASSWORD
def forgot_password():
    dict={}
    Email_id=input('Enter Your Email Id::')
    phone_no=input('Enter Your Phone No::')
    with open("C:\\PROJECT\\user_id_password.txt",'rb+') as baghat:
        try:
            while True:
                dict=pickle.load(baghat)
                while dict['Email_id']==Email_id:
                            if dict['Phone_no']==phone_no:
                                time.sleep(1)
                                print('Your Password Is',dict['password'])
                                break
                            else:
                                print('1.Try Again(Enter Phone Number)','\n','2.Another Way')
                                choice=input('Enter You Choice::')
                                if choice=='1':
                                    phone_no=input('Invalid Phone No,Enter Again::')
                                    continue
                                elif choice=='2':
                                     S_Question=input('Enter Your Memorable Monuments::')
                                     if dict['Question']==S_Question:
                                         time.sleep(1)
                                         print('Your Password Is',dict['password'])
                                         break
                                else:
                                     print('Invalid Input,Enter Again.')
                                     continue
        except EOFError:
             #BY RATNESH KUMAR
             Start()
             
#STORE DATA
def add_citizen_data():
    Data=sql.connect(host="localhost",user="root",passwd= "Ratnesh#123",database="project")
    cursor=Data.cursor()
    print("PLEASE FILL DATA CAREFULLY.")
    IMAGE=input('Enter Image Name With Path::')
    Name=input('Enter Name Of Applicent::')
    Fathername=input("Enter Father's Name Of Applicent::")
    Gender= input(" Enter You Gender::")
    D_O_B=input('Enter Date Of Birth Of Applicent::')
    print("NOTE:-IF YOU ARE OBC THEN ALSO MENTION YOUR ARE BELONG FROM CREAMY LAYER OR NOT LIKE OBC(NCL).")
    Caste=input("Enter Applicent Caste(General/OBC(CL/NCL)/SC/ST)::")
    Bloodgroup=input('Enter Blood Group Of Applicent(Like -A)::')
    Address=input ("Enter Current Address Of Applicent::")
    phone=input ("Enter your phone number::")
    Card_number=genratecardnumber()
    q="insert into citizen_data(IMAGE,NAME,FATHERNAME,GENDER,DOB,CASTE,BLOODGROUP,ADDRESS,CARDNUMBER,PHONENO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value=(IMAGE,Name,Fathername,Gender,D_O_B,Caste,Bloodgroup,Address,Card_number,phone)
    cursor.execute(q,value)
    print("YOUR CARD NUMBER IS:",Card_number)
    print("your data will be recorded.",'\n',"you can download your card after 3 to 4 days.")
    Data.commit()
    Data.close()
    time.sleep(1)
    main_menu()

    
#GENRATE CARD NUMBER
def genratecardnumber():
    Card_Number=random.randint(100000000,999999999)
    with open("C:\\PROJECT\\user_id_password.txt",'ab+') as raj:
        try:
            while True:
                Read=pickle.load(raj)
                if Read==Card_Number:
                    Card_Number=random.randint(100000000000,999999999999)
                    continue
        except EOFError:
                    pickle.dump(Card_Number,raj)
    return Card_Number
    
#UPDATE
def update():
    Data=sql.connect(host="localhost",user="root",passwd= "Ratnesh#123",database="project")
    cur=Data.cursor()
    print("update:-",'\n',"1.Name",'\n','2.Image','\n',"3.Fathername",'\n',"4.Gender",'\n',"5.Date of birth",'\n',"6.caste",'\n',"7.Blood Group",'\n',"8.Address")
    choice=int(input('Enter Your Choice::'))
    Card_number=cardnum()
    while True:
        if choice==1:
            Name=input('Enter Name Of Applicent::')
            query="Update citizen_data set NAME=%s where CARDNUMBER=%s"
            value=(Name,Card_number)
            cur.execute(query,value)
            print("Your Name Is Updated.")
            Data.commit()
            break
        elif choice ==2:
            IMAGE=input('Enter Image Name With Path::')
            query="Update citizen_data set IMAGE=%s where CARDNUMBER=%s"
            value=(IMAGE,Card_number)
            cur.execute(query,value)
            print("Your Image Is Updated.")
            Data.commit()
            break
        elif choice==3:
            Fathername=input("Enter Father's Name Of Applicent::")
            query="Update citizen_data set FATHERNAME=%s where CARDNUMBER=%s"
            value=(Fathername,Card_number)
            cur.execute(query,value)
            print("Your Father Name Is Updated.")
            Data.commit()
            break
        elif choice==4:
            Gender= input(" Enter You Gender::")
            query="Update citizen_data set GENDER=%s where CARDNUMBER=%s"
            value=(Gender,Card_number)
            cur.execute(query,value)
            print("Your Gender Is Updated.")
            Data.commit()
            break
        elif choice==5:
            D_O_B=input('Enter Date Of Birth Of Applicent(Like Oct4,2004)::')
            query="Update citizen_data set DOB=%s where CARDNUMBER=%s"
            value=(D_O_B,Card_number)
            cur.execute(query,value)
            print("Your Date Of Birth Is Updated.")
            Data.commit()
            break
        elif choice==6:
            print("NOTE:-IF YOU ARE OBC THEN ALSO MENTION YOUR ARE BELONG FROM CREAMY LAYER OR NOT. ")
            Caste=input("Enter Applicent Caste(General/OBC(CL/NCL)/SC/ST::")
            query="Update citizen_data set CASTE=%s where CARDNUMBER=%s"
            value=(Caste,Card_number)
            cur.execute(query,value)
            print("Your Caste Is Updated.")
            Data.commit()
            break
        elif choice==7:
            Bloodgroup=input('Enter Blood Group Of Applicent(Like -A)::')
            query="Update citizen_data set BLOODGROUP=%s where CARDNUMBER=%s"
            value=(Bloodgroup,Card_number)
            cur.execute(query,value)
            print("Your Blood Group Is Updated.")
            Data.commit()
            break
        elif choice==8:
            Address=input ("Enter Current Address Of Applicent::")
            query="Update citizen_data set ADDRESS=%s where CARDNUMBER=%s"
            value=(Address,Card_number)
            cur.execute(query,value)
            print("Your Address Is Updated.")
            Data.commit()
            break
        else:
              print('Invalid Input Try Again.')
              continue
        Data.close()
    main_menu()
              
#ADD & DISPLAY DISEASES
def diseases():
    cardnumber=cardnum()
    Data=sql.connect(host="localhost",user="root",passwd= "Ratnesh#123",database="project")
    cur=Data.cursor()
    Choice='y'
    while True:
        print("1.Add Diseases",'\n',"2.View Diseases")
        choice=int(input("Enter Choice::"))
        if choice==1:
            while Choice=='y':
                diseases=input("Enter Diseases Name::")
                query="insert into data_diseases(CARDNUMBER,DISEASES) values (%s,%s)"
                value=(cardnumber,diseases)
                cur.execute(query,value)
                Choice=input("Do You Add More(Y/N)::").lower()
                Data.commit()
            Data.close()
            main_menu()
        elif choice==2:
            value=str(cardnumber)
            query="select DISEASES from data_diseases where CARDNUMBER="+value
            cur.execute(query)
            _data=cur.fetchall()
            for i in _data:
                print(i)
            main_menu()
        else:
            print("Invalid Input,Try Again.")
            continue
             
#DATA RETRIVE
def data_gain():
    Data1=sql.connect(host="localhost",user="root",passwd= "Ratnesh#123",database="project")
    cur=Data1.cursor()
    cardnumber=cardnum()
    value=str(cardnumber)
    query="select * from citizen_data where CARDNUMBER="+value
    cur.execute(query)
    data=cur.fetchone()
    Data=list(data)
    Data1.close()
    return Data
    
#DISPLAY CARD
def DisplayCard():
    DATA=data_gain()
    imagefront=Image.open("C:\\PROJECT\\health_card_front.png")
    imageback=Image.open("C:\\PROJECT\\health_card_back.png")
    imafront=ImageDraw.Draw(imagefront)
    imaback=ImageDraw.Draw(imageback)
    fnt =ImageFont.truetype('arial.ttf')
    imafront.text((115,95),DATA[1].upper(),Font=30,fill=(0,0,0))
    imafront.text((158,125),DATA[2].upper(),ImageFont=30,fill=(0,0,0))
    imafront.text((158,153),DATA[4].upper(),ImageFont=30,fill=(0,0,0))
    imafront.text((125,211),DATA[3].upper(),ImageFont=30,fill=(0,0,0))
    imafront.text((158,182),DATA[6].upper(),ImageFont=30,fill=(0,0,0))
    imafront.text((136,240),DATA[9],ImageFont=30,fill=(0,0,0))
    imaback.text((106,135),DATA[5],ImageFont=30,fill=(0,0,0))
    imaback.text((150,250),DATA[8],ImageFont=30,fill=(0,0,0))
    imaback.text((120,163),DATA[7].upper(),ImageFont=30,fill=(0,0,0))
    imafront.text((243,375),DATA[1],ImageFont=30,fill=(0,0,0))
    pic=Image.open(DATA[0])
    pic= pic.resize((60, 90))
    imagefront.paste(pic,(5,90))
    imgfront= qrcode.make(DATA)
    imgback= qrcode.make(DATA)
    imgfront= imgfront.resize((100,100))
    imgback= imgback.resize((150,150))
    imagefront.paste(imgfront,(300,150))
    imageback.paste(imgback,(330,150))
    image_front=imagefront.size
    imageback=imageback.resize(image_front)
    new_image = Image.new('RGB',(imagefront.width+imageback.width, imageback.height), (250,250,250))
    new_image.paste(imagefront,(0,0))
    new_image.paste(imageback,(imagefront.width,0))
    name=('C:\\PROJECT\\')+input('Enter You Card Name::')+'.pdf'
    new_image.save(name)
    main_menu()

    
#VERIFY CARD NUMBER
def cardnum():
    cardnumber=int(input("Enter Card Number::"))
    with open("C:\\PROJECT\\user_id_password.txt",'rb+') as taj:
                try:
                    while True:
                            Read=pickle.load(taj)
                            if cardnumber==Read:
                                break
                except EOFError:
                    print('Invalid Card Number!,Enter Again')
                    cardnum()
    return cardnumber
    
#VERIFY PHONE NUMBER
def VerifyPhoneNo():
    phoneno=False
    while phoneno!=True:
        phone_no=input('Enter You Phone Number::')
        if len(phone_no)!=10:
            print('Invalid Input!,Enter Again')
            continue
        if len(phone_no)==10:
            phoneno=True
    with open("C:\\PROJECT\\user_id_password.txt",'rb+') as bharat:
        dict={}
        try:
            while True:
                dict=pickle.load(bharat)
                if dict['Phone_no']==phone_no:
                    print('This Number Is Already Register .You Can Use Another Phone Number.')
                    VerifyPhoneNo()
        except EOFError:
              #RATNESH KUMAR
              return phone_no

#VERIFY EMAIL ID
def VerifyEmail():
    user_id=input('Enter Your Email Id::')
    with open("C:\\PROJECT\\user_id_password.txt",'rb+') as bharat:
        dict={}
        try:
            while True:
                dict=pickle.load(bharat)
                if dict['Email_id']==user_id:
                    print('This Email Id Is Already Register .You Can Use Another Email ID.')
                    VerifyEmail()
        except EOFError:
              #RATNESH KUMAR
              return user_id

Start()
