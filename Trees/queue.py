#Create Queue Using Double Link List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.back


    def enqueue(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.back = new_node
            self.head = new_node


    def dequeue(self):
        if self.tail is None:
            return None
        else:
            if self.tail.back is None:
                data = self.tail.value
                self.head = None
                self.tail = None
            else:
                data = self.tail.value
                self.tail = self.tail.back
                self.tail.next = None
            return data
            
    

    def peek(self):
        if self.tail is None:
            return None
        else:
            return self.tail.value 


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



