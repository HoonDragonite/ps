'''
이진탐색트리 (BST)

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

class Tree:
    def __init__(self):
        self.root = None

    