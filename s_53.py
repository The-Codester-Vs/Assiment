# password generator

import random
print("1 for 4 Digit password.\n2 for 6 Digit password.\n3 for Alphabet password.")
n = int(input("Enter your choice(1,2 or 3): "))
if n == 1:
    s="1234567890"
    result =  "".join(random.sample(s,4))
    print ("Your 4 Digit password:",result)
elif n==2:
    s="1234567890"
    result =  "".join(random.sample(s,6))
    print ("Your 6 Digit password:",result)    
elif n == 3:
    alphabet = int(input("Enter the length of alphabet password: "))
    s="abcdefgQWERTYUIhijklmnopqrstOPSDFGHJKLZXCVBNM"
    result =  "".join(random.sample(s,alphabet))
    print ("Your alphabet password:",result) 
else:
    print("Invalid Input!")       