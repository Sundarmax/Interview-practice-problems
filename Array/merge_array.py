# Merge two sorted arrays with O(N+M) space complexity
# Time complexity O(N+M)
a = [55,77,88,99,101,105] # SIZE N
b = [11,22,33,66] # SIZE M 
size = len(a) + len(b)

def MergeTwoArray():
    c = []
    i = j = 0
    while i <len(a) and j < len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    
    while i < len(a):
        c.append(a[i])
        i+=1
    
    while j < len(b):
        c.append(b[j])
        j+=1
    print(c)
MergeTwoArray()