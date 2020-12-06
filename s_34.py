# armstrong number
def armstrong(n):
    sum2 = 0
    temp2  = n
    while (temp2>0):
        digit = temp2 % 10
        sum2 += digit**3
        temp2//=10
    if sum2==n:
        print("-->It is a Armstrong Number.")
    else:
        print("-->Not a Armstrong Number.")
 
num = int(input("Enter the number: "))        
armstrong(num)