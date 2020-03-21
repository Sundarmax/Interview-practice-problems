class TwoDArray:

    def __init__(self):
        rows, cols = (3,3)
        self.array = [ [0 for i in range(rows)] for j in range(cols)]
        self.rows  = rows
        self.cols  = cols 

    def AddNewItem(self):
        for i in range(self.rows):
            for j in range(self.cols):
                item = input()
                self.array[i][j] = item
            print(i+1,'Row added')

    def DeleteItem(self):
        pass

    def GetData(self):
        for row in self.array:
            print(row)

TestObj = TwoDArray()
TestObj.AddNewItem()
TestObj.GetData()
