# TO CALCULATE BMI(BODY MASS INDEX).
X=float(input("Enter Weight In Kg :"))
Y=float(input("Enter Height In Centimeters :"))/100
BMI=X/(Y*Y)
print(f"Your BMI Is:{BMI}\nAnd You Are ",end="")
if BMI<=18.5:
    print("...Underweight")
elif BMI<=25:
    print("...Normal")
elif BMI<=30:
    print("...Overweight")
else:
    print("...Obese")