# sum of naturals number
num=int(input("Enter a number: "))
def sum_natural(n):
    sum1 = 0
    while(n > 0):
        sum1=sum1+n
        n=n-1
    return sum1    
print(f"The sum of first {num} natural numbers is",sum_natural(num))