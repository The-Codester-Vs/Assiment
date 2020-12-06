# multiples genrator
def list_of_multiples (num):
	return list(range(num, num*10+1,num))

n = int(input("Enter the number :"))
result = list_of_multiples(n)
print(f"The multiples of {n} are : {result}")
