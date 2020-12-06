print("_____________Calculator_____________")

while (True):
    print("Enter the first number:")
    num1=int(input())
    print("Enter the second number:")
    num2 = int(input())
    num3=input("select the operators(+,-,/,*) and for exit() type out:\n")
    if num3 == '+' :
        add = num1+num2
        print(add)
        print("|-------x------------------x--------------------x-----|")
        continue
    elif num3 =='-':
        sub = num1 - num2
        print(sub)
        print("|-------x------------------x--------------------x-----|")

        continue
    elif num3=='*':
        multi = num1*num2
        print(multi)
        print("|-------x------------------x--------------------x-----|")

        continue
    elif num3=='/':
        divide=num2/num1
        print(divide)
        print("|-------x------------------x--------------------x-----|")

        continue
    elif num3=='out':
        print("see you later")

        break
    else:
        print("try again")
        continue
        











