# printing odd number
odd_numbers = []
max = int(input('Enter the number: '))

for i in range(max):
    if i % 2 == 1:
        odd_numbers.append(i)

print(f"Odd numbers between 0 to {max} are:{odd_numbers }")