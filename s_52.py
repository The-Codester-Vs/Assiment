# email maker
import random
s="1234567890"
p =  "".join(random.sample(s,4 ))
name1 = input("Enter first name: ")
name2 = input("Enter last name: ")
domain = "@gmail.com"
your_email = name1+name2+p+domain
print("---------------------------------")
print("Your email id:",your_email)