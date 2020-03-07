def CheckOneEditInsert(s1,s2):
    i = j =  0
    while i < len(s1): # keep large string in s1 
        if s1[i] != s2[j]:
            if i != j:
                return False
            i+=1
        else:
            i+=1
            j+=1
    return True

def CheckoneEditReplace(s3,s4):
    i    = 0
    Flag = False
    while i < len(s3):
        if s3[i] != s4[i]:
            if Flag :
                return False
            Flag = True
        i+=1
    return True

def OneEditAway(s1,s2): #wrapper function 
    if len(s1) == len(s2):
        return CheckoneEditReplace(s1,s2)
    elif len(s1) +1 == len(s2):
        return CheckOneEditInsert(s1,s2)
    elif len(s1) -1 == len(s2):
        return CheckOneEditInsert(s1,s2)
    else:
        return False

s1 = "apple"
s2 = "aple"
s3 = "apple"
s4 = "apble"
result = OneEditAway(s1,s2) # Remove 
output = OneEditAway(s2,s1) # Insert
print(result)
