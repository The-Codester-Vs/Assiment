# calculating the length of string
string = input("Enter the String:\n")
print(f"The string which you entered: {string}")
def length(str):
    count = 0
    for i in range(len(str)):
        count += 1
    return f'The length of string is {count}'


print(length(string))