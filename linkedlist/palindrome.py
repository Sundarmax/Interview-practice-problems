# To check if a linked list is a palindrome. 
# Load data into stack and compare it with linked list.
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.startnode = None
        self.insert_at_last(1)
        self.insert_at_last(2)
        self.insert_at_last(1)
        self.insert_at_last(2)
        self.insert_at_last(1)

    def insert_at_last(self,data):
        if self.startnode is None:
            new_node = Node(data)
            new_node.item = data
            new_node.next = self.startnode
            self.startnode = new_node
        else:
            n = self.startnode
            while n.next is not None:
                n = n.next
            new_node = Node(data)
            new_node.item = data
            n.next = new_node
    
    def TraverseList(self):
        n = self.startnode
        while n is not None:
            print(n.item, end = " ")
            n = n.next
        print(' ')

    def CheckPalindrome(self):
        Stack = []
        n = self.startnode
        while n is not None:
            Stack.append(n.item)
            n = n.next
        n = self.startnode
        # calculate stack length 
        lengthOfStack = len(Stack) - 1
        # Start comparing stack top with linked list
        while lengthOfStack >=0 and n is not None:
            if Stack[lengthOfStack] == n.item:
                pass
            else:
                return False
            lengthOfStack = lengthOfStack - 1
            n = n.next
        return True

newlist = LinkedList()
#newlist.TraverseList()
Output = newlist.CheckPalindrome()
print(Output)