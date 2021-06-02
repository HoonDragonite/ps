'''
이진탐색트리 (BST)

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

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
        
    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

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
        
    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BST()
for num in array:
    bst.insert(num)

print(bst.root)
bst.preOrderTraversal(bst.root)
print()
bst.inOrderTraversal(bst.root)
print()
bst.postOrderTraversal(bst.root)
print()

node = bst.find(15)
print(node)

node = bst.find(17)
print(node)

# https://geonlee.tistory.com/78?category=318965