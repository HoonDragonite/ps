'''
전위(PREORDER) : Me - Left - Right
중위(INORDER) : Left - Me - Right
후위(POSTORDER) : Left - Right - Me
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preOrderTraversal(self, node):
        print(node, end='')
        if node.left != None:  self.preOrderTraversal(node.left)
        if node.right != None: self.preOrderTraversal(node.right)
    
    def inOrderTraversal(self, node):
        if node.left != None:  self.inOrderTraversal(node.left)
        print(node, end='')
        if node.right != None: self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node.left != None:  self.postOrderTraversal(node.left)
        if node.right != None: self.postOrderTraversal(node.right)
        print(node, end='')
