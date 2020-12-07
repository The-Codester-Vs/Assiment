
List = [9,6,4,8,3,2,0,12,7,10]
print(f"Original List:{List}")

def sort(num):
    n = len(num)
    for i in range (n-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num 

n = sort(List)
print("Sorted List:",n)           
    
