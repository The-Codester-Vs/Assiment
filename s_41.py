# finding larger number
x = y = z = 0
x = float(input("Enter First number: "))
y = float(input("Enter Second number: "))
z = float(input("Enter Third number: "))
max = None
if x>y>z or x>z>y:
    max = x
elif y>x>z or y>z>x:
    max = y
elif z>x>y or z>y>x:   
    max = z 
    

print("The largest number is: ",max)
    