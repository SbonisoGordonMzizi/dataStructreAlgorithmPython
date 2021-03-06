import queue

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right_node =  None
        self.left_node = None


rootNode = TreeNode(100)
node110 = TreeNode(110)
node105 = TreeNode(105)
node170 = TreeNode(170)
node90 = TreeNode(90)
node80 = TreeNode(80)
node50 = TreeNode(50)


rootNode.right_node = node90
rootNode.left_node = node110
node110.right_node = node105
node110.left_node = node170
node90.left_node = node80
node90.right_node = node50

queue_ = []


def travesal_pre_order(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.value)
        travesal_pre_order(rootNode.right_node)
        travesal_pre_order(rootNode.left_node)


#Using PYTHON LIST 
def travesal_level_order_python_list(rootNode):
    if rootNode is None:
        return
    else:
        queue_.append(rootNode)
        while len(queue_) != 0:
            root = queue_.pop(0)
            print(root.value)
            if root.right_node is not None:
                queue_.append(root.right_node)
            if root.left_node is not None:
                queue_.append(root.left_node)


#Using LINK LIST 
def travesal_level_order_link_list(rootNode):
    if rootNode is None:
        return
    else:
        queue_link_list = queue.MyQueue()
        queue_link_list.enqueue(rootNode)
        while queue_link_list.isEmpty() == False:
            root = queue_link_list.dequeue()
            print(root.value)
            if root.right_node is not None:
                queue_link_list.enqueue(root.right_node)
            if root.left_node is not None:
                queue_link_list.enqueue(root.left_node)
            

           
        

       
#travesal_level_order(rootNode)