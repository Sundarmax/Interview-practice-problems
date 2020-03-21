# Add two number represented by linked list. 
# Single digit value is stored in each node of the list. 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self,new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def printList(self):
        n = self.head
        while n is not None:
            print(n.data, end=' ')
            n = n.next
        print('')

    def SumTwoList(self,first,second):
        carry = 0 
        prev = None
        temp = None
        while first is not None or second is not None:
            sumValue = carry + (first.data + second.data)
            carry    = 1 if sumValue >= 10 else 0 
            value    = sumValue % 10 
            temp     = Node(value)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            LastNode = Node(carry)
            temp.next = LastNode

first   = Linkedlist()
second  = Linkedlist()
result  = Linkedlist()
first.push(6)
first.push(1)
first.push(7)
second.push(6)
second.push(9)
second.push(5)
first.printList()
second.printList()
result.SumTwoList(first.head,second.head)
result.printList()