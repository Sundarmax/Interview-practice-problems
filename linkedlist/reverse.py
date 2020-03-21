# Reverse a sinly linked list 
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.startnode = None
        self.insert_at_last(1)
        self.insert_at_last(2)
        self.insert_at_last(3)
        self.insert_at_last(4)
        self.insert_at_last(5)

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

    def ReverseLinkedlist(self):
        current = self.startnode
        temp = None
        prev = None
        while current is not None:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        self.startnode = prev

newlist = LinkedList()
newlist.ReverseLinkedlist()
newlist.TraverseList()

