#Partition a linkedList
#Don't care about original order 

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.startnode = None
    
    def TraverseList(self):
        n = self.startnode
        while n is not None:
            print(n.item, end = " ")
            n = n.next
        print(' ')
    
    def ParitionALinkedlist(self):
        x = 3 # partition value
        tail = self.startnode
        curr = self.startnode
        while curr is not None:
            next = curr.next
            if curr.item < x:
                curr.next = self.startnode
                self.startnode = curr #first node 
            else:
                tail.next = curr
                tail = curr # last node 
            curr = next
        tail.next = None

newList = LinkedList()
newList.startnode = Node(3)
newList.startnode.next = Node(5)
newList.startnode.next.next =Node(1)
newList.startnode.next.next.next =Node(2)
newList.startnode.next.next.next.next =Node(4)

newList.TraverseList()
newList.ParitionALinkedlist()
newList.TraverseList()