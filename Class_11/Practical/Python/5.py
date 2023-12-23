# CREATE A DICTIONARY WITH THE ROLL NUMBER,NAME AND MARKS OF n STUDENTS IN A CLASS AND DISPLAY THE NAMES OF STUDENTS WHO HAVE SCORED MARKS ABOVE 75.
num = int(input("Enter The Number Of Student Whose Data To Be Stored:"))
count = 1
Student ={}
while count <= num:
    name = input("Enter The Name Of The Student:")
    rollno = int(input("Enter The Roll No:"))
    mark=int(input("Enter The Marks:"))
    Student[name] =rollno,mark
    count += 1
print("NAME",'\t\t',"ROLL NO.",'\t',"MARKS")
for k in Student:
    if Student[k][1] >= 75:
        print(k,'\t\t',Student[k][0],'\t\t',Student[k][1])
    else:
        print("Not Found")