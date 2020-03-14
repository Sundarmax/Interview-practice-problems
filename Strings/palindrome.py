#Check if a permutation of a string is palindrome or not 
tempString = "aab" # aa # racecar
CharCount = [0]*122

def CheckPalindrome():
    count = 0
    for i in tempString:
        charIndex = ord(i) #returs ascill value of letter
        #count+=CharCount[charIndex] % 2
        CharCount[charIndex]+=1
    print(CharCount)
    for c in range(len(CharCount)):
        count = count + CharCount[c] % 2
        if count > 1: # if count zero and one means it's fine. 
            return False
    return True

res = CheckPalindrome()
if res == False:
    print('Palindrome not exists')
else:
    print('Palindrome exists')