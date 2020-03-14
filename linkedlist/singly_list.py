# Implementation of singly linked list 

class Node:
    def __init__(self,data):
        self.item = data
        self.next  = None

class LinkedList:

    def __init__(self):
        self.start_node = None

    def TraverseList(self):
        if self.start_node is None:
            print('List has no element')
            return 
        else:
            current = self.start_node
            while current is not None:
                print(current.item , " ")
                current = current.next
    
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_at_end(self,data):
        new_data    = Node(data)
        if self.start_node is None:
            self.start_node = new_data
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_data
    
    def insert_after_item(self,x,data):
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.next
        if n is None:
            print('element is not in the list')
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
    
    def insert_before_item(self,x,data):
        if self.start_node is None:
            print('Linkedlist has no element')
            return
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None: #learn difference between n.next is none and n is none . 
            if n.next.item == x:
                break
            n = n.next
        if n.next is None:
            print('Element is not in the list')
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
    
    def SearchList(self,x):
        if self.start_node is None:
            print('Linkedlist has no element')
            return
        n = self.start_node
        while n is not None:
            if n.item ==  x:
                print('Search element exists')
                return
            n = n.next
        print('Element is not exist')
        return

new_list = LinkedList()
new_list.insert_at_end(1)
new_list.insert_at_end(2)
new_list.insert_at_start(0)
new_list.insert_after_item(1,1.5)
new_list.insert_before_item(1,0.5)
new_list.SearchList(4)
new_list.TraverseList()