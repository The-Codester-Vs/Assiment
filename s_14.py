def triangle(n): 
    k = 2*n - 2

    for i in range(0, n): 
      
        for j in range(0, k): 
            print(end=" ") 
    
        k = k - 1
      
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = int(input("Enter the number: "))
triangle(n) 