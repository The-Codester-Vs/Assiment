# program to print wheather a given character is an uppercase
# or a lower character or a digit or any other character
ch = input("Enter a single character: ")

if ch >= 'A' and ch <= 'Z':
    print("You entered upper case character")
elif ch >='a' and ch <= 'z':
    print("You entered a lower case character")
elif ch >='0' and ch <= '9':
    print("You entered a digit") 
else:
    print("You entered a special character")
                