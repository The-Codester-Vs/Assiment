# finding larger number

x = y = z = 0
x = float(input("Enter First number: "))
y = float(input("Enter Second number: "))
z = float(input("Enter Third number: "))

max = x
if y > max:
    max = y
elif z > max:
    max = x

print("The larget number is: ",max)
    