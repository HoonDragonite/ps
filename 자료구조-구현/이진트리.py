'''
이진트리

순회
1. 전위(PREORDER) : Me - Left - Right
2. 중위(INORDER) : Left - Me - Right
3. 후위(POSTORDER) : Left - Right - Me
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrderTraversal(self, node):
        if node == None : return
        print(node, end=' ')
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)
    
    def inOrderTraversal(self, node):
        if node == None : return
        self.inOrderTraversal(node.left)
        print(node, end=' ')
        self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node == None : return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node, end=' ')

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l,r) + 1


tree = BinaryTree()

tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")

newNode1 = Node("D")
newNode2 = Node("E")
node = tree.root.left
node.left = newNode1
node.right = newNode2

newNode1 = Node("F")
newNode2 = Node("G")
node = tree.root.right
node.left = newNode1
node.right = newNode2

'''
     a
    b c
  d e f g
'''
print(tree.root)
tree.preOrderTraversal(tree.root)
print()
tree.inOrderTraversal(tree.root)
print()
tree.postOrderTraversal(tree.root)