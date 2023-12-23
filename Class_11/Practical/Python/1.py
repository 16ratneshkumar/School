# FIND THE LARGEST AND SMALLEST NUMBER IN A TUPLE.
numbers = tuple() 
n = int(input("How Many Numbers You Want To Enter?:"))
for i in range(1,n+1):
    num = int(input(f"Enter {i} Number:"))
    numbers = numbers +(num,)
print("The Numbers In The Tuple Are:",numbers)
print("The Maximum Number Is:",max(numbers))
print("The Minimum Number Is:",min(numbers)) 