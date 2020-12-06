# counting the length of numbers
def number_length(num):
    length = 0
    for i in str(num):
        length += 1
    return length
n = int(input("Enter the number: "))
print(f"The of this {n} number is {number_length(n)}")

        