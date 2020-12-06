def pypart(n):
    for i in range(0, n): 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        print("\r")  
n = int(input("Enter the number: "))
pypart(n) 