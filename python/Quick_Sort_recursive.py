def partition(arr,l,h):
    i = l - 1
    pivet = arr[h]
    for j in range(l,h):
        if arr[j] < pivet:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return(i+1) 

def QuickSort(arr,l,h):
    if l<h:
        pi = partition(arr,l,h)
        
        QuickSort(arr,pi+1,h)
        QuickSort(arr,l,pi-1)
 
if __name__ == '__main__':
    arr =[1,3,5,7,9,4,12,6,2,8,0]
    n  = len(arr)
    QuickSort(arr,0,n-1)
    print("Sorted list:")
    print(arr)
           
    