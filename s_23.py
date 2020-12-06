# inches to feet 
def inches_to_feet(inches):
        if inches < 12:
            return 0
        return inches/12

inch = int(input("Enter the inches: "))
result = inches_to_feet(inch)
print(f"{inch} inches are {result} feet")