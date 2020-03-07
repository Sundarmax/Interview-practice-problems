# segregate 0's and 1's in array 
# first approach we can't track order of elements and Time complexity is 0(N)
# Time complexity of secon approach is O(N)

a = [1,0,1,1,1,1,0,0,0,1]

def BinarySort():
    first = 0
    last = len(a) -1 
    while first < last:
        if a[first] == 0:
            first+=1
        if a[last] == 1:
            last-=1
        if a[first] == 1 and a[last] == 0:
            a[first], a[last] =  a[last], a[first]

    print(a)

def BucketSort():
    bucketArray  = [0] * 2 # size of this array depends upon input array
    c = k = 0
    if len(a) > 0 :
        for num in a:
            bucketArray[num] = bucketArray[num] + 1
    # BucketArray keeps the count of 1's and 0's then rewrite them into a list.
        while c < len(bucketArray):
            count = bucketArray[c]
            while count > 0:
                a[k] = c
                k+=1
                count-=1
            c+=1
        print(bucketArray)
        print(a)

#BinarySort()
BucketSort()