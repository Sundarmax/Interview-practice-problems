# Implementation of three stacks in single array. 

info    = [] # Array is used to store stack objects. 
values  = [0] * 9 # Which is used to store actual Stack values. 
class StackInfo:
    
    size = 0
    
    def __init__(self,start,capacity):
        self.start = start
        self.capacity = capacity

    def isEmpty(self):
        return True if self.size == 0 else False

    def IsFull(self):
        return True if self.size == self.capacity else False

def expand(stackNumber):
    # check if next stack is full or not. 
    stackNumber+=1
    if info[stackNumber].IsFull():
        print('Next stack is also full')
    # Move stack elements by one.
    StartIndex =    info[stackNumber].start
    EndIndex   =    info[stackNumber].start + info[stackNumber].size -1
    while EndIndex >= StartIndex:
        TempIndex = EndIndex+1
        Index = TempIndex % 9
        values[Index] = values[EndIndex]
        EndIndex-=1
    # Decrease stack size 
    info[stackNumber].capacity-=1
    info[stackNumber].start+=1

def push(stackNumber,item):
    if info[stackNumber-1].IsFull():
        #print('current stack is overflow')
        print('Shifting next stack elements')
        expand(stackNumber-1)
        # insert an item to current stack
        GetIndex = info[stackNumber-1].start + info[stackNumber-1].size
        values[GetIndex] = item
        # Increase capacity and size of current stack.
        info[stackNumber-1].capacity+=1
        info[stackNumber-1].size+=1
        #print(info[stackNumber-1].capacity)

    else:
        GetIndex = info[stackNumber-1].start + info[stackNumber-1].size
        values[GetIndex] = item
        info[stackNumber-1].size+=1

def pop(stackNumber):
    if info[stackNumber-1].isEmpty():
        print('Stack is underflow')
    else:
        GetIndex = info[stackNumber-1].size * info[stackNumber-1].start
        #del values[GetIndex]
        values[GetIndex] = 0
        info[stackNumber-1].size-=1

def MultiStack(NumberOfStack = 3,DefaultSize = 3):
    for i in range(NumberOfStack):
        info.append(StackInfo(i*NumberOfStack,DefaultSize))

def DispalyStack():
    for i in info:
        print('-------')
        print("start_value",i.start)
        print("stack_size",i.size)
        print("stack_capacity",i.capacity)
    print(values)

MultiStack()
push(2,11)
push(2,12)
push(2,13)
push(1,5)
push(3,22)
#push(3,23)
push(2,14)
print('Test-case-2')
push(2,15)
push(2,16)
DispalyStack()
