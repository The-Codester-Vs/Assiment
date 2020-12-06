# perfect number
def perfect_number(n):
    sum1 = 0
    for i in range(1,n):
        if (n % i == 0):
            sum1 = sum1 + i
    if(sum1==n):
        print("-->Its is a Perfect Number.")
    else:
        print("-->Not a Perfect Number.")

num = int(input("Enter the number: "))        
perfect_number(num)