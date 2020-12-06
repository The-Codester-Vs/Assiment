# program to calculate the mean of given list
lst = [1,2,3,5,8,7,9]
length = len(lst)
mean = sum = 0
for i in range(0,length):
    sum+= lst[i]

mean = sum/length
print("Given list: ",lst)
print("The mean of given list: ",mean)