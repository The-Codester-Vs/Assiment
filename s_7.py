# factorail finder
def factorail(n):
    if n == 0:
        return 1
    return n * factorail(n-1)

n =  int(input("Enter the number: "))
result = f"The factorail of {n} is {factorail(n)}"
print(result)

