def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum
  
  
n = int(input("Enter the number: "))
print("cube first",n,"natural numbers are:",sumOfSeries(n)) 