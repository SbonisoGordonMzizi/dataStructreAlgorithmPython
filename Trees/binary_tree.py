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


def travesal_pre_order(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.value)
        travesal_pre_order(rootNode.right_node)
        travesal_pre_order(rootNode.left_node)

def travesal_level_order(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = queue.MyQueue()
        customQueue.enqueue(rootNode)
        while customQueue.isEmpty() != True:
            root = customQueue.dequeue()
            print(root)
            if root.value.right_node is not None:
                customQueue.enqueue(rootNode)
            if root.value.left_node is not None:
                customQueue.enqueue(rootNode)

travesal_level_order(rootNode)