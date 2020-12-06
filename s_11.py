# finding the leap year
print("Leap year finder")
num = int(input("Enter the year: "))
def leap_year(year):
    if year%4==0:
        print("--> This is a leap year")
    else:
        print("--> This year was not a leap year")    

leap_year(num)