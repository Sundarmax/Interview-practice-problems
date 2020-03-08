#Dynamic array implementation


class DynamicArray:

    def __init__(self):
        self.array = [0] * 2
        self.capacity = 2
        self.currentIndex = 0

    def AddNewElement(self,item):
        if self.capacity == self.currentIndex:
            self.ReSizeArray()
        self.array[self.currentIndex] = item
        self.currentIndex+=1
    
    def RemoveElement(self,item):
        if self.capacity == 0:
            print('you can\'t remove from empty list')
        #self.array.remove(item)
        self.capacity -=1

    def ReSizeArray(self):
        self.capacity *=2
        newArray = [0] * self.capacity
        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        self.array = newArray
    
    def getLength(self):
        return len(self.array)

    def getArrayData(self,index):
        if index < 0 or index > self.capacity:
            print('Index out of bounds')
            return -1
        return self.array[index]
test = DynamicArray()
test.AddNewElement(7)
test.AddNewElement(8)
length = test.getLength()
print(length)
test.AddNewElement(6)
length = test.getLength()
print(length)
#test.RemoveElement()