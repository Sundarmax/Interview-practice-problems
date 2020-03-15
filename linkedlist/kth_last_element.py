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

    def kthElementbyRecursion(self, Node, k):
        if Node is None:
            return 0
        i = self.kthElementbyRecursion(Node.next, k) + 1
        if i == k:
            print(Node.item)
        return i
    
    def kthElementbyIteration(self, Node, k):
        current = Node # iterate till kth distance
        while k>0:
            current = current.next
            k-=1
        second = Node
        while second is not None and current is not None:
            current = current.next
            second  = second.next
        print(second.item)
new_list = LinkedList()
new_list.TraverseList()
#new_list.kthElementbyRecursion(new_list.startnode,k = 3)
new_list.kthElementbyIteration(new_list.startnode,k = 2)