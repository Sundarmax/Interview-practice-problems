# Modify Matrix 
# 10.03.2020
# Time Complexity O(N*M)
# Space Complexity O(N+M)
class BooleanMatrix:
    def __init__(self,R,C,Matrix):
        self.array = Matrix
        self.rows  = R
        self.cols  = C
        self.RArray = [0] * R
        self.CArray = [0] * C
        self.IntitializeArray()

    def IntitializeArray(self):
        for i in range(self.rows):
            self.RArray[i] = 0
        for j in range(self.cols):
            self.CArray[j] = 0

    def TraverseMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] == 1:
                    self.RArray[i] = 1
                    self.CArray[j] = 1
        print(self.RArray)
        print(self.CArray)

    def MatrixModification(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.RArray[i] == 1 or self.CArray[j] == 1:
                    self.array[i][j] = 1
        print(self.array)

mat = [[1,0,0],
       [0,0,1],
       [0,0,0]]
#Obj = BooleanMatrix(3,3,mat)
#Obj.TraverseMatrix()
#Obj.MatrixModification()

#Second approach # Space is optimized with O(1)

def MatrixModification(mat,R,C):
    rowFlag = False
    colFlag = False

    for i in range(R):
        for j in range(C):
            if i ==0 and mat[i][j] == 1: #first row
                rowFlag = True
            if j ==0 and mat[i][j] == 1: #first column
                colFlag = True
            if mat[i][j] == 1:
                mat[0][j] = 1
                mat[i][0] = 1
    print(mat)
    
    for i in range(1,R):
        for j in range(1,C):
            if mat[i][0] == 1 or mat[0][j] == 1:
                mat[i][j] = 1
    print(mat)

    for i in range(R): # update first row
        if rowFlag == True:
            mat[i][0] = 1
        
    for j in range(C): # update first column
        if colFlag == True:
            mat[0][j] = 1
    print(mat)


mat = [[1,0,0,1],
       [0,0,1,0],
       [0,0,0,0] ] # 3*4

MatrixModification(mat,R=3,C=4)