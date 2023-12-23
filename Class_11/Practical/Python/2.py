# INPUT A LIST OF ELEMENTS, SEARCH FOR A GIVEN ELEMENT IN THE LIST.
List=[]
n = int(input("How Many Numbers You Want To Enter?:"))
for i in range(1,n+1):
    num = int(input(f"Enter {i} Number :"))
    List.append(num)
i=int(input("Enter Those Number You Are Find:"))
if i in List:
    print("Given Number Is Found")
else:
    print("Given Number Is Not Found")