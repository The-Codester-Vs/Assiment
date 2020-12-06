# finding the number of consonants in the string.
vowels = 'aeiou'
input1 = input("Enter the string: ")


def count_consonants(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() not in vowels and input_string[i].isalpha():
            count += 1 
    return count


print(f'The number of Consonants in string are {count_consonants(input1)}')
