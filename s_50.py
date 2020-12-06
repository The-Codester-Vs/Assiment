# program to input an integer and check if it contains any 0 in it
n = int(input("Enter the number: "))
s = str(n)

if "0" in s:
    print("There is an zero(0) in",n)
else:
    print("There is no zero(0) in",n)  
      