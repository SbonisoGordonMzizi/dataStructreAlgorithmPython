#Stack Using double Link List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class MYStack:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node


    def pop(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.next
            self.head.back = None
    

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value 


    def isEmpty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False     

    def deleteStack(self):
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = None
            while node is not None:
                next_ = node.next
                node.back = None
                node = next_
            self.tail = None

    
dd = MYStack()
dd.push(10)
dd.push(20)
dd.push(30)
dd.push(40)
dd.push(50)
dd.push(60)

print([v.value for v in dd])
dd.pop()
print([v.value for v in dd])
print(dd.peek())
print([v.value for v in dd])
print(dd.isEmpty())
dd.deleteStack()
print(dd.isEmpty())


