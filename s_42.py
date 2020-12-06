# cheching divisibility of a number

number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))
remainder = number1%number2
if remainder == 0:
    print(f"{number1} is divisible by {number2}")
else:
    print(f"{number1} is not divisible by {number2}")
        