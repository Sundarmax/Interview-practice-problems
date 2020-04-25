# Queue implementation with two stacks

stack_1 = [] # Which can be used for enque operation.
stack_2 = [] # which can be used for Deque operation.

def Insert(item):
    stack_1.append(item)

def Remove():
    # Check if stack_2 is having any items. 
    if len(stack_2) > 0:
        stack_2.pop()
    else:
        # Copy item from stack_1 to stack_2
        while len(stack_1) > 0:
            TopValue = stack_1.pop()
            stack_2.append(TopValue)
        # Now remove top value of stack-2
        stack_2.pop()
        # Push back values to stack_1 # Not need to move back. 
        # while len(stack_2) > 0:
        #     TopValue = stack_2.pop()
        #     stack_1.append(TopValue)

def DisplayQueue():
    print("stack--> I ",stack_1)
    print("stack--> II ",stack_2)

Insert(1)
Insert(2)
Insert(3)
DisplayQueue()
Remove()
Remove()
DisplayQueue()
Insert(4)
Insert(5)
DisplayQueue()
Remove()
DisplayQueue()
Remove() #Copying element from s1 to s2
DisplayQueue()
