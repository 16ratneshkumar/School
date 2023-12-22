#TO CHECK NUMBER or STRING IS PALINDROME OR NOT.
Input=input("Enter Your Number Or String:: ")
if str(Input) == str(Input)[::-1]:
    print(f"The Given Input {Input} Is Palindrome.")
else:
    print(f"The Given Input {Input} Is Not Palindrome.")