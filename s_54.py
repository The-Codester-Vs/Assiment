# Finding element form a list of element along with its index in the list.
pos = -1

def search(list,n):
    l = 0
    u = len(list) - 1


    while l <= u :
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l  = mid + 1
            else:
                u = mid -1
    return False

list = [2,3,5,7,9,10,11,12,14,16,18,20]
n = int(input("Enter the number: "))

if search(list,n):
    print("Your number",n,"is in the list at position",pos + 1)
else:
    print("Your number",n,"is not in the list.")