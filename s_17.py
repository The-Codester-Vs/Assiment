# displaying even numbers
def even(n):
    print(f"Even numbers between 1 and {n} are:",end = " ")
    for i in range(1,n + 1):   
        if i%2 == 0 :
            print(i,end =" ")

num = int(input("Enter the number: "))

result = even(num)

              
    