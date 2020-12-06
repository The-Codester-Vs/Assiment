# password checker
password = "1234"
pw = ""
count = 0
max_count = 5
auth = False

while pw != password:
    count = count + 1
    if count > max_count:
        break
    pw = input(f"{count}:What is the password?")
else:
    auth = True

if auth:
    print("Authorized")  
else:
    print("Account Locked")      
     