# Get Minimum Element from Stack in Constant O(1) time complexity

Stack = [] 
supportStack = []

def push(item):
    if len(Stack) == 0:
        Stack.append(item)
        supportStack.append(item)
    else:
        Stack.append(item)
        TopValue = supportStack[-1]
        if item < TopValue:
            supportStack.append(item)

def StackDisplay():
    print(Stack)
    print(supportStack)

def GetMinStack():
    return supportStack[-1]

def pop():
    if len(Stack) > 0:
        TopValue = Stack.pop()
        if TopValue == supportStack[-1]:
            supportStack.pop()
    else:
        print('Stack is empty')

push(11)
push(22)
push(33)
push(7)
StackDisplay()
pop()
StackDisplay()
pop()
StackDisplay()
push(3)
StackDisplay()
result = GetMinStack()
print(result)