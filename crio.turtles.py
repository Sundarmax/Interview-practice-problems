def CheckTurlesCommunication(NumArray,m,n):
    TotalCount = 0
    # loop through 2d array 
    row = 0 
    col = 0
    for row in range(int(m)):
        for col in range(int(n)):
            CurrValue = NumArray[row][col]
            Flag = False
            R = row
            C = col 
            # Check horizontally 
            # Next element
            if CurrValue == 1 and C+1 < int(n):
                #print("Horizontal-->left",row,col)
                if NumArray[R][C+1] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True
            #Prev element
            if CurrValue == 1 and C-1 >= 0:
                #print("Horizontal-->right",row,col)
                if NumArray[R][C-1] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True
            # Check vertically 
            # bottom next element
            if CurrValue == 1 and R+1 < int(m): 
                #print("vertical-->bottom",row,col)
                if NumArray[R+1][C] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True
            # top element 
            if CurrValue == 1 and R-1 >= 0: 
                #print("vertical-->top",row,col)
                if NumArray[R-1][C] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True
            # check diagnally
            if CurrValue == 1 and C+1 < int(n) and R+1 < int(m):
                #print("diagnally-->bottom",row,col)
                if NumArray[R+1][C+1] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True
            if CurrValue == 1 and C-1 >= 0 and R-1 >=0:
                #print("diagnally-->bottom",row,col)
                if NumArray[R-1][C-1] == 1 and Flag == False:
                    TotalCount+=1
                    Flag =  True

    return TotalCount

def GetInput():
    # read user input
    m,n = input().split()
    # initialize an array 
    NumArray = [[None for i in range(int(m))] for j in range(int(n))]
    # store values in an array .
    for row in range(int(m)):
            InputList = list(input().split())
            for col in range(len(InputList)):
                CurrValue = InputList[col]
                NumArray[row][col] = int(CurrValue)
    #print(NumArray)
    
    #print(NumArray)
    # Call func to check turtle communication
    result = CheckTurlesCommunication(NumArray,m,n)
    print(result)
    
GetInput()
