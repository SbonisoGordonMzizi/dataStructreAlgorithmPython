
#double link list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.back = None

class DoubleLinklist:
    def __init__(self):
        self.head = None
        self.tail = None

                
    def insert(self,value,location=0):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head.back = new_node
                self.head = new_node
            elif location == -1:
                self.tail.next = new_node
                new_node.back = self.tail
                self.tail = new_node


    def get_forward(self):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


    def get_back(self):
        if self.tail is None:
            print("Empty Link List")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.back
    
    def search(self,value,direction=0):
        if self.head is None:
            print("Empty Link List")
        else:
            if direction == 0:
                print("forward")
                node = self.head
                while node is not None:
                    if node.value == value:
                        print(node.value)
                        break
                    node = node.next
                else:
                    print(f"{value} not found")

            elif direction == 1:
                print("back")
                node = self.tail
                while node is not None:
                    if node.value == value:
                        print(node.value)
                        break
                    node = node.back
                else:
                    print(f"{value} not found")

    def delete_all(self):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            self.head = None
            while node is not None:
                next_ = node.next
                node.back = None
                node = next_
            self.tail = None


    def delete(self,value):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    if node.back is None:
                        self.head = node.next
                        self.head.back = None
                    elif node.next is None:
                        self.tail = node.back
                        self.tail.next = None
                    else:
                        node.back.next = node.next
                        node.next.back = node.back
                node = node.next


dd = DoubleLinklist()
dd.insert(100)
dd.insert(101)
dd.insert(102)
dd.insert(103)
dd.insert(104)
#dd.get_forward()
#print("##################")
#dd.get_back()

dd.delete(103)
dd.delete(102)
dd.get_forward()
