#First approach for N*N MATRIX 
def PrintMatrix(mat,R,C):
    for i in range(R):
        for j in range(C):
            print(mat[i][j], end=" ")
        print()

def RotateMatrix(mat,R,C):
    #Reverse upside and down
    for i in range(R//2):
        for j in range(C):
            mat[i][j], mat[C-1-i][j] =  mat[C-1-i][j], mat[i][j]
    PrintMatrix(mat,R,C)
    print('-------------')
    #swap the symmatric values
    for i in range(R):
        for j in range(C):
            if i<=j:
                temp      = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
    PrintMatrix(mat,R,C)


#RotateMatrix(mat,R=4,C=4)
#Second apporach 
#Swap elements by cycle or layer 

def Rotate90ClockWise(mat,R,C):
    for i in range(R//2): #Refers Cycle or Sub-matrix
        for j in range(i,R-1-i):
            temp = mat[i][j] # save top
            # left -->top
            mat[i][j] = mat[R-1-j][i] # move from bottom to top
            # bottom --> left
            mat[R-1-j][i] = mat[R-1-i][R-1-j] #Move from Right to Left
            # right --> bottom 
            mat[R-1-i][R-1-j] = mat[j][R-1-i]  #move fro top to bottom.
            # top --> right 
            mat[j][R-1-i] = temp
            
mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

PrintMatrix(mat,R=4,C=4)
Rotate90ClockWise(mat,R=4,C=4)
PrintMatrix(mat,R=4,C=4)