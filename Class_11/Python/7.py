# TO CONVERT CELSICS TO FAHRENHEIT AND FAHRENHEIT TO CELSICS.
X=float(input("1.Celsics To Fahrenheit.\n2.Fahrenheit To Celsics.\nEnter A Number:: "))
if X==1:
    A=float(input("Enter Temperature In Celsics:: "))
    B=A*9/5+32
    print("Temperature In Fahrenheit Is:: ",B)
else:
    A=float(input("Enter Temperature In Fahrenheit:: "))
    B=(A-32)*5/9
    print("Temperature In Celsius Is:: ",B)
