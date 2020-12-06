# Convert Hours and Minutes into Seconds

def convert(hours, minutes):
	return hours*60*60 + minutes*60

hour = int(input("Enter hours: "))
min = int(input("Enter minutes: "))

result = convert(hour,min)

print(f"{hour} hour and {min} minutes are {result} seconds")

