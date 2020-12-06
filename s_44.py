# arranging the numbers in incresing order
x = int(input("Enter First number: ")) 
y = int(input("Enter Second number: "))
z = int(input("Enter Third number: "))

min = mid = max = None
if x<y and x<z:
    if y<z:
        min,mid,max = x,y,z
    else:
        min,mid,max = x,z,y    

elif y<x and y<z:
    if x<z:
        min,mid,max = y,x,z
    else:
        min,mid,max = y,z,x
elif z<x and z<y:
    if x<y:
        min,mid,max = z,x,y
    else:
        min,mid,max = z,y,x 

print("Number in Incresing Order:",min,mid,max)                      