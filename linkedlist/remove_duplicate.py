#Remove duplicates from unsorted linked list
#Without using bufffer time complexity will be O(N)*2

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
    
    def RemoveDuplicate(self):
        n = self.startnode
        while n is not None:
            prev = n
            curr = n.next
            while curr is not None:
                if curr.item == n.item:
                    print(curr.item,'--',n.item)
                    prev.next = curr.next
                prev = curr
                curr = curr.next    
            n = n.next
    def RemoveDuplicateWithBuffer(self):
        ItemList = []
        n    = self.startnode
        prev = None
        while n is not None:
            if n.item in ItemList:
                prev.next = n.next    
                n = n.next
            else:
                ItemList.append(n.item)
                prev = n
                n = n.next
        return

newlist = LinkedList()
newlist.TraverseList()
#newlist.RemoveDuplicate()
newlist.RemoveDuplicateWithBuffer()
newlist.TraverseList()