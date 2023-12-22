#INPUT A LIST OF NUMBERS AND FIND THE SMALLEST AND LARGEST NUMBER FROM THE LIST.
List=[]
n = int(input("How Many Numbers You Want To Enter?:"))
for i in range(1,n+1):
    num = int(input(f"Enter {i} Number:"))
    List.append(num)
print("The Numbers In The List Are:",List)
print("The Maximum Number Is:",max(List))
print("The Minimum Number Is:",min(List))