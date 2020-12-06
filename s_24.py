# kilometers to miles
def km_to_miles(kilometers):
	return round(kilometers * 0.621371, 5)

km = int(input("Enter the kilometers: "))
result = km_to_miles(km)
print(f"{km} kilometers are {result} miles")

