# Bubble sort
list = [1,3,2,6,8,5,7,9,10,0,4]

def bubble(list):
    for i in range(len(list)- 1, 0, -1):
        for j in range(i):
            if list[j+1] < list[j]:
                list[j],list[j+1] = list[j+1],list[j]
    return list     


result = bubble(list)
print(list)
