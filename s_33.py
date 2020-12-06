def Palindrome(s):
    return s == s[::-1]
 
string  = input("Input the string:")
print(" You Entered:",string)
ans = Palindrome(string)
 
if ans:
    print("--> It is a Palindrome. ")
else:
    print("--> It is not a Palindrome.")