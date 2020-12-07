# decimal to binary convert
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

# decimal number
number = int(input("Enter any decimal number: "))

print("The Binary Number of",number ,'is: ')
decimalToBinary(number)