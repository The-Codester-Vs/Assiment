def Merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[mid:]
        r = arr[:mid]
        
        Merge(l)
        Merge(r)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(l) and j < len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            arr[k] =  l[i]
            i += 1
            k += 1
                    
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1  

if __name__ == '__main__':
    arr = [0,9,7,8,5,6,4,3,1,2]
    Merge(arr)
    print(arr)                 