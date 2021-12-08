#create linklist of objects

class Node():
    def __init__(self,value,ref=None):
        self.value = value
        self.ref = ref


class single_link_list():
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.ref


    def insert(self,value):
        location = 0
        new_node = Node(value)
        if  self.head is None:
            self.head = new_node
            self.tail = new_node
            print(self.tail.value)
        else:
            if location == 0:
                new_node.ref = self.head
                self.head = new_node
                print(self.tail)
            
            
    def get_all(self):
        if self.head is None:
           print("Link List is Empty")
        else:
           node = self.head
           count = 0
           while node is not None:
                print(f"{count} <> node.value")
                node = node.ref
   
    def search(self,value):
        if self.head is None:
            return "Link List is Empty"
        else:
            node = self.head
            while node is not None:
                if value == node.value:
                    return node.value
                node = node.ref
            return f"{value} Not Found"

single_link_list = single_link_list()

node = Node(1)
single_link_list.head = node

single_link_list.insert(12)
single_link_list.insert(134)
single_link_list.insert(1000)
single_link_list.insert(9999)
single_link_list.insert(1234)


h = [node.value for node in single_link_list]
print(h)
print(single_link_list.search(9999))





