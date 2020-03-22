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

    def GetLengthOfList(self,head):
        length = 0
        while head is not None:
            head = head.next
            length+=1
        return length

    def GetIntersectNode(self,head1,head2,AbsIndex): # keep head1 is always larger list
        while AbsIndex > 0 and head1 is not None:
            head1 = head1.next
            AbsIndex-=1
        newhead = head1
        while head1 is not None and head2 is not None:
            if head1.item == head2.item:
                print('intersected node is ', head2.item)
                break
            head2 = head2.next
            head1 = head1.next

    def GetAbsoluteValue(self,head1,head2):
        c1 = self.GetLengthOfList(head1)
        c2 = self.GetLengthOfList(head2)
        if c1 > c2:
            diff = abs(c1-c2)
            self.GetIntersectNode(head1,head2,diff)
        else:
            diff = abs(c2-c1)
            self.GetIntersectNode(head2,head1,diff)

newList = LinkedList()
newList.startnode = Node(3)
newList.startnode.next = Node(6)
newList.startnode.next.next =Node(9)
newList.startnode.next.next.next =Node(15)
newList.startnode.next.next.next.next =Node(30)

secondlist = LinkedList()
secondlist.startnode = Node(10)
secondlist.startnode.next = newList.startnode.next.next.next
resultlist = LinkedList()
resultlist.GetAbsoluteValue(newList.startnode,secondlist.startnode)


#newList.TraverseList()
#secondlist.TraverseList()