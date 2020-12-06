# displaying all prime numbers
end = int(input("Enter the number:"))
print(f"Prime Numbers between 0 to {end} are:")
for i in range(0,end):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i,end =" ")
  