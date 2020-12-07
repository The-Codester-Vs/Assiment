# square and cube the each elements of the list
num = [2,3,4,5,6,7,8,9,12]
def square(n):
    return n*n
def cubic(n):
    return n*n*n
sq = list(map(square,num)) 
cub = list(map(cubic,num))  
print("Original List:",num)
print("Squared list:",sq)
print("Cubic List:",cub)
