# program thats prints minimum and maximum of five numbers entered by the user
n = int(input("Enter the number: "))
mn,mx = n,n

for i in range(4):
    n = int(input("Enter the number: "))
    if mx < n:
        mx = n
    elif mn > n:
        mn = n
print("----------------------------------------")
print("Maximum of numbers entered:",mx)
print("Minimum of numbers entered:",mn)
            