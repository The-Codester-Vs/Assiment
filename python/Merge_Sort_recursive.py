def Merge(left,right):
    index_R, index_L = 0 , 0
    result = []
    
    while index_L < len(left) and index_R < len(right):
        if left[index_L] < right[index_R]:
           result.append(left[index_L])
           index_L += 1 
        else:   
            result.append(right[index_R])
            index_R += 1
    
    result += left[index_L:]
    result += right[index_R:] 
    return result

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
     
    mid = len(arr) // 2
    L = MergeSort (arr[:mid])
    R = MergeSort(arr[mid:])
    
    return Merge(L,R)

    
if __name__ == '__main__':
    arr = [0,7,8,5,6,9,3,4,2,1,10]
    r = MergeSort(arr)
    print(r)
    