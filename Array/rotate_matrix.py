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

mat = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
RotateMatrix(mat,R=4,C=4)