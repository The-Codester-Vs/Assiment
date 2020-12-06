# prime and composite number
while(1):
    num = int(input("Enter the number:"))
    for i in range(2, num):
        if(num % i == 0):
            print("It is a Composite Number")
            print("-----------------------------------------")
            break
        continue
    else:
        print("It is a Prime number")
        print("-----------------------------------------")

        continue
