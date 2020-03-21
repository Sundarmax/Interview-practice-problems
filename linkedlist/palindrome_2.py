#Check if a singly linked list is a palindrome or not. 
#Find mid node and Reverse the second half & compare it with initial head. 
#Handle case for odd and even apporach

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.startnode = None
        self.insert_at_last("R")
        self.insert_at_last("A")
        self.insert_at_last("C")
        self.insert_at_last("E")
        self.insert_at_last("C")
        self.insert_at_last("A")
        self.insert_at_last("R")

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
    
    def TraverseList(self,startNode):
        n = startNode
        while n is not None:
            print(n.item, end = " ")
            n = n.next
        print(' ')
    
    def CompareList(self,head1,head2):
        if head1 is None or head2 is None:
            return False
        while head1 is not None and head2 is not None:
            if head1.item == head2.item:
                pass
            else:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
    
    def ReverseLinkedlist(self,head):
        current = head
        temp = None
        prev = None
        while current is not None:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        return prev
    
    def CheckPalindrome(self):
        slow = self.startnode
        fast = self.startnode
        # Odd case
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        StartReversehead = slow.next
        prev.next = None # cut off link 
        middleNode = slow # save mid node .
        newhead = self.ReverseLinkedlist(head = StartReversehead)
        self.TraverseList(startNode=newhead)
        self.TraverseList(startNode=self.startnode)
        result = self.CompareList(head1=self.startnode,head2=newhead)
        # construct original list
        oldhead = self.ReverseLinkedlist(head = newhead)
        prev.next = middleNode
        middleNode.next = oldhead
        self.TraverseList(startNode=self.startnode)

newlist = LinkedList()
newlist.CheckPalindrome()
#newlist.TraverseList()