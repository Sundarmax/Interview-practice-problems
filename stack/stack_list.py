#Stack implementation by using linked list 

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class StackList:

    def __init__(self):
        self.startNode = None

    def PrintStack(self):
        n = self.startNode
        while n is not None:
            print(n.data)
            n = n.next
    
    def PushNode(self,data):
        newNode = Node(data)
        if self.startNode is None:
            self.startNode = newNode
        else:
            newNode.next = self.startNode
            self.startNode = newNode

    def PopNode(self):
        if self.startNode is None:
            print('List is empty')
        else:
            temp = self.startNode
            self.startNode = self.startNode.next
            print('Node is deleted')

newStack = StackList()
newStack.PushNode(7)
newStack.PushNode(6)
newStack.PushNode(5)
newStack.PrintStack()
newStack.PopNode()
newStack.PrintStack()