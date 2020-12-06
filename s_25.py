# finding volume of cone
def cone_volume(h, r):
	return round(3.14*r*r*h/3,2)

val_h = float(input("Enter the height of the cone in decimal: "))
val_r = float(input("Enter the radius of the cone in decimal: "))
result = cone_volume(val_h,val_r)
print(f"The volume of cone is {result}")
