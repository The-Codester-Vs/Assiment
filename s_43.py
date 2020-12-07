# calculating the area of the circle
radius = float(input("Enter the radius of the circle: "))
print("1 for Calculate Area.\n2 for Calculate Perimeter.")
choice = int(input("Enter your choice: "))
if choice == 1 :
    area = 3.14*radius*radius
    print("Area of Circle",area)
elif choice == 2:
    perimeter = 2 * 3.14 * radius
    print("Perimeter of Circle",perimeter)
else:
    print("Your choice is invalid")    