# Python Program to Check Number is Divisible by 5 and 11

number = int(input(" Please Enter any Positive Integer : "))

if((number % 5 == 0) and (number % 11 == 0)):
    print("Given Number",number,"is Divisible by 5 and 11")
else:
    print("Given Number",number,"is Not Divisible by 5 and 11")