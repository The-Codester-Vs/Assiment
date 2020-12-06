# displaying odd numbers
def Odd(n):
    print(f"Odd numbers between 1 and {n} are:",end =" ")
    for i in range(1,n+1):
        if i%2 != 0:
            print(i,end = " ")
            
num = int(input("Enter the number: "))
Odd(num)            