#INPUT A LIST OF NUMBERS AND SWAP ELEMENTS AT THE EVEN LOCATION WITH THE ELEMENTS AT THE ODD LOCATION.
List=[]
n = int(input("How Many Numbers You Want To Enter?:"))
for i in range(1,n+1):
    num = int(input(f"Enter {i} Number:"))
    List.append(num)
print("Your List Is",List)
for i in range(0,len(List)-1,2):
    List[i],List[i+1]=List[i+1],List[i]
print("After Swaping List Is:",List)