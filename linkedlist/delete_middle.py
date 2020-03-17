#Delete the given node which is placed between first and last
#Head node access in not given 

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.startnode = None
        self.insert_at_last(6)
        self.insert_at_last(7)
        self.insert_at_last(8)
        self.insert_at_last(9)
        self.insert_at_last(10)

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

    def delete_middle(self):
        GivenNode = self.startnode.next.next
        n = GivenNode
        prev = None
        while n.next is not None:
            n.item = n.next.item
            prev = n
            n = n.next
        prev.next = None #Cut off link to last Node

new_list = LinkedList()
new_list.TraverseList()
new_list.delete_middle()
new_list.TraverseList()