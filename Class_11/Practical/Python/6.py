# TO CHECK NUMBER IS PALINDROME OR NOT.
num=int(input("Enter A Number:: "));
rev=0
nnum=num
while (nnum !=0):
    digit = nnum%10;
    nnum = nnum//10
    rev = rev*10+digit
if rev ==num:
    print(f"The Given Input {num} Is Palindrome.")
else:
    print(f"The Given Input {num} Is Not Palindrome.")