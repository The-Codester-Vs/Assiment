# counting vowels in string
def countVowels(string):
        vowels = ['a','e','i','o','u']
        total = 0
        for s in string:
            if s in vowels:
                total += 1
        return total
    
str1 = input("Enter the string: ")
result = countVowels(str1)
print(f"Total numbers of vowels in the string are {result}")    