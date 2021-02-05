def partition(arr,l,h):
    i = (l - 1)
    x = arr[h] #pivet
    
    for j in range(l,h):
        if arr[j] <= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1) 

def quick_sort_iterative(arr,l,h):
    size = h -l + 1
    stack= [0]*(size)
    
    top = -1
    
    top = top+1
    stack[top] = l
    top = top + 1
    stack[top] = h 
    
    while top >= 0:
        h = stack[top]
        top = top-1
        l = stack[top]
        top= top - 1
        
        p = partition(arr,l,h)
        
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1


        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
  
  
def print_iterative(arr):
    print("\n-----Iterative Quick Sort----")
    n = len(arr)
    quick_sort_iterative(arr, 0, n-1)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    
    
arr = [9,8,7,6,5,4,3,2,1,10,12]
print_iterative(arr)