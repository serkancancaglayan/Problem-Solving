class Node:
    data = None
    left = None
    right = None
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def printNode(self):
        print(self.data)

    def insert(self, data):
        if data <= self.data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def printTree_inorder(self):
        if self.left != None:
            self.left.printTree_inorder()
        print(self.data)
        if self.right != None:
            self.right.printTree_inorder()

    def printTree_preorder(self):
        print(self.data)
        if self.left != None:
            self.left.printTree_preorder()
        if self.right != None:
            self.right.printTree_preorder()

    def find(self,data):
        if self.data == data:
            print("found")
            exit()
        elif data < self.data:
            if self.left is not None:
                self.left.find(data)
            else:
                print("bulamadik abi")
        else:
            if self.right is not None:
                self.right.find(data)
            else:
                print("bulamadik abi")
    
    def leafNode(self):
        if self.left == None and self.right == None:
            return 1
        if self.right != None:
            return self.right.leafNode()
        if self.left != None:
            return self.left.leafNode()
        else:
            return self.left.leafNode() + self.right.leafNode()

    def height(self):
        if self.left != None and self.right != None:
            return max(self.left.height(), self.right.height())

        elif self.left == None and self.right != None:
            return 1 + self.right.height()

        elif self.left != None and self.right == None:
            return 1 + self.left.height()

        else:
            return 1



def LCA(n1, n2,root):
    if root == None:
        return None
    elif root.data > n2.data and root.data > n1.data:
        if root.left != None:
            return LCA(n1, n2, root.left)
    elif root.data < n2.data and root.data < n1.data:
        if root.right != None:
            return LCA(n1, n2, root.right)
    return root

x = Node(8)
x.insert(3)
x.insert(10)
x.insert(11)
x.insert(6)
x.insert(4)
x.insert(7)
x.insert(14)
x.insert(13)

print(LCA(Node(10), Node(14), x).data)
