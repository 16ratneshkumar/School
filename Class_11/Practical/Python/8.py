# TO CONVERT SIMPLE INTEREST AND COMPOUND INTEREST.
X=int(input("1.Simple Interest.\n2.Compound Interest.\nEnter A Number:: "))
P = float(input("Enter The Principal Amount : "))
N = float(input("Enter The Number Of Years : "))
R = float(input("Enter The Rate Of Interest : "))
if X==1:
    SI= P*R*N/100
    print("Simple Interest Is:",SI)
else:
    A = P * (pow((1 + R / 100), N))
    CI = A - P
    print("Compound Interest Is", CI)
