def numpat(n): 
      
    # initialising starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 

        num = 1
      
        for j in range(0, i+1): 
          
            print(num, end=" ") 
          
            num = num + 1
        print("\r") 
  
# Driver code 
n = int(input("Enter the number: "))
numpat(n) 