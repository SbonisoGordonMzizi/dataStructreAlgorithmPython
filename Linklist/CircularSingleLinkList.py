#Circular Single Link List

class Node:
    def __init__(self,value):
        self.ref = None
        self.value = value


class CircularSingleLinklist:
    def __init__(self):
        self.head = None
        self.tail = None
    

    def __iter__(self):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            while node:
                yield node
                if node.ref == self.head:
                    break
                node = node.ref

    def insert(self,value,location=0):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.ref = new_node
        else:
            if location == 0:
                self.tail.ref = new_node
                new_node.ref = self.head
                self.head = new_node
            elif location == -1:
                new_node.ref = self.tail.ref
                self.tail.ref = new_node
                self.tail = new_node
    def search(self,value):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            count = 0
            while node:
                if node.value == value:
                    print(value)
                    break

                if node.ref == self.head:
                    print(f"{value} not found")
                    break
                node = node.ref
                count += 1

    def get_all(self):
        if self.head is None:
            print("Empty Link List")
        else:
            node = self.head
            count = 0
            while node:
                print(f"{count} <> {node.value}")
                if node.ref == self.head:
                    break
                node = node.ref
                count += 1


    def delete_all(self):
        self.head = None
        self.tail.ref = None
        self.tail = None

ll = CircularSingleLinklist()
ll.insert(1)
ll.insert(2,-1)
ll.insert(3)
ll.insert(4)
j = [v.value for v in ll]
print(j)
ll.search(2)
ll.get_all()
ll.delete_all()
ll.get_all()
