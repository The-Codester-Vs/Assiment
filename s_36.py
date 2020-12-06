# palindrome number
def palindrome_number(n):
    
    temp1 = n#local variable
    rev = 0
    while(n>0):
        d = n%10
        rev = rev*10+d
        n=n//10
    if (temp1==d):
        print("-->Its is a Palindrome Number.")
    else:
        print("-->Not a Palindrome Number.")  
 
num = int(input("Enter the number: "))
palindrome_number(num)        
