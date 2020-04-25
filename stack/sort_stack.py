class stack:

    stack = []
    
    def push(self,item):
        self.stack.append(item)

    def TopValue(self):
        return self.stack[-1]

    def IsEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.IsEmpty():
            print('Stack underflow')
            exit(1)
        return self.stack.pop()
    
    def displayStack(self):
        print(self.stack)

def SortStack():
    Stack = stack()
    Stack.push(3)
    Stack.push(5)
    Stack.push(1)
    Stack.push(4)
    Stack.push(2)
    Stack.push(8)
    Stack.displayStack()
    # Just assume it is act like stack
    tempstack = []
    #tempstack = stack()
    #check = tempstack.IsEmpty()

    while Stack.IsEmpty() == False: #Exit when this conditin fails.. 
        TopValue = Stack.pop()

        while ((len(tempstack) > 0) and (int(TopValue) < int(tempstack[-1]))):
            tempTop = tempstack.pop()
            Stack.push(tempTop)
        tempstack.append(TopValue) # Push input value if it is greater than top value of temporary stack. 

    print(tempstack)

SortStack()
