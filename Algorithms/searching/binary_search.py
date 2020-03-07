a   = [11,12,13,14,15]
key =  14 # Search element

#Iterative way  
def BinarySearch(start,last):
    while start <= last:
        mid = start + (last - start) //2 # BODMAS
        if a[mid] == key:
            return mid
        if key > a[mid] : # 15 > 13
            start = mid + 1
        else:
            last = mid - 1
    return -1

def RecursiveBinarySearch(start,last):
    if start <= last:
        mid = start + (last - start) //2
        if a[mid] == key:
            return mid
        if key > a[mid]:
            return RecursiveBinarySearch(mid+1,last)
        else:
            return RecursiveBinarySearch(start,mid-1)
    else:
        return -1 
#result = BinarySearch(start=0,last=len(a)-1)
result = RecursiveBinarySearch(start=0,last=len(a)-1)
if result == -1:
    print('search element was not found')
else:
    print('search element was found')